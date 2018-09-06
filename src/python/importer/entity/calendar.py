#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

from __future__ import print_function

import uuid
import json
import datetime

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

from utils import parity as prt


class Calendar(object):
    data = json.dumps({})
    service = None

    def __init__(self, *args, **kwargs):
        s = len(kwargs)
        if s is 1:
            if len(kwargs) > 0:
                self.config = kwargs.get('configuration', 0)
        else:
            raise SystemError()

        self.timedelta = 0

        print(self.config.data['path_to_creds'])

        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(self.config.data['path_to_creds'],
                                                  'https://www.googleapis.com/auth/calendar')
            creds = tools.run_flow(flow, store)
        self.service = build('calendar', 'v3', http=creds.authorize(Http()))

    def get_subject_time(self, day_number, number):
        start_time = 0
        end_time = 0

        date = datetime.datetime.now().date()
        day = str(date + datetime.timedelta(day_number + self.timedelta - date.weekday())) + 'T'

        if number == 1:
            start_time = day + '08:20'
            end_time = day + '09:50'
        elif number == 2:
            start_time = day + '10:00'
            end_time = day + '11:35'
        elif number == 3:
            start_time = day + '12:05'
            end_time = day + '13:40'
        elif number == 4:
            start_time = day + '13:50'
            end_time = day + '15:25'
        elif number == 5:
            start_time = day + '15:35'
            end_time = day + '17:10'
        elif number == 6:
            start_time = day + '17:20'
            end_time = day + '18:40'
        elif number == 7:
            start_time = day + '18:45'
            end_time = day + '20:05'
        elif number == 7:
            start_time = day + '20:10'
            end_time = day + '21:30'
        else:
            print(u'[ERROR] index is out of range')

        appendix = ':00.000000'

        return start_time + appendix, end_time + appendix

    def put_subj(self, subject, day_number, number, parity):
        if 'couple' in subject:
            if parity == 'числ.':
                subject = (subject['couple'])[0]
            else:
                subject = (subject['couple'])[1]

        print(parity)

        summary = '%s (%s)' % (subject['name'], subject['type'])
        location = subject['place']
        desc = subject['teacher']
        start_time, end_time = self.get_subject_time(day_number, number)

        if subject['type'] == 'лек.':
            color = self.config.data['color.lesson']
        elif subject['type'] == 'пр.':
            color = self.config.data['color.practice']
        elif subject['type'] == 'лаб.':
            color = self.config.data['color.laboratory_work']
        else:
            color = self.config.data['color.default']

        if subject['other'] == '':
            pass
        elif subject['other'] in self.config.data['include.specializations']:
            pass

        event = {
            'summary': summary,
            'location': location,
            'description': desc,
            'colorId': color,
            'start': {
                'dateTime': start_time,
                'timeZone': self.config.data['timezone'],
            },
            'end': {
                'dateTime': end_time,
                'timeZone': self.config.data['timezone'],
            },
            'recurrence': [
                "RRULE:FREQ=" + self.config.data['recurrence.freq'] + ";COUNT=" + self.config.data[
                    'recurrence.count'] + ";INTERVAL=" + self.config.data[
                    'system.calendar.interval']
            ],
            'attendees': [
                {'email': self.config.data['personal_email']},
            ],
            'iCalUID': str(uuid.uuid4()),
            'status': 'confirmed',
            'reminders': {
                'useDefault': self.config.data['reminder.useDefault'],
                'overrides': [
                    # {
                    #    'method': 'email',
                    #    'minutes': 24 * 60
                    # },
                    {
                        'method': 'popup',
                        'minutes': self.config.data['reminder.popup']
                    },
                ],
            },
        }

        event = self.service.events().import_(calendarId=self.config.data['calendarId'], body=event).execute()
        print('[INFO] Event created: %s' % (event.get('htmlLink')))

    def put_day(self, day, day_number, parity):
        for index in range(0, 9):
            if type(day[index]) is dict:
                self.put_subj(day[index], day_number, index, parity)

    def put_week(self, week):
        print('[INFO] Start loading schedule...')
        week = json.loads(week, encoding='utf-8')

        parity = prt.get()

        if (int)(self.config.data['recurrence.count']) > 1:
            self.config.update('system.calendar.interval', '2')

            for index in range(0, 6):
                self.put_day((((week['response'])['days'])[index])['subjects'], index, parity)

            self.timedelta = 7
            for index in range(0, 6):
                self.put_day((((week['response'])['days'])[index])['subjects'], index, prt.get_opposite())

            self.timedelta = 0
            self.config.update('system.calendar.interval', '1')
        else:
            for index in range(0, 6):
                self.put_day((((week['response'])['days'])[index])['subjects'], index, parity)
        print('[INFO] Loading is finished.')

    def clear_primary(self):
        self.clear('primary')

    def clear(self, calendar_id):
        print(calendar_id)
        print('[WARNING] Do you really want clean your %s calendar?(Y/N)' % calendar_id)
        answer = input()
        if answer == 'Y' or answer == 'YES' or answer == 'y' or answer == 'yes':
            print('[INFO] Clean started...')
            self.service.calendars().delete(calendarId=calendar_id).execute()
            print('[INFO] Clean finished.')
        else:
            print('[INFO] Clean cancelled.')
