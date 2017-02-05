#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

from __future__ import print_function

import json
import os

import httplib2
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

with open('config.json', 'r') as conf_file:
    CONFIG = json.load(conf_file)

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
# We can use https://www.googleapis.com/auth/calendar.readonly for readonly mode
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Import SSU subject to Google Calendar'


def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'credentials.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('[INFO] Storing credentials to ' + credential_path)
    return credentials


def insert(summary, location, color, desc, start_time, end_time, timezone=CONFIG['timezone']):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    event = {
        'summary': summary,
        'location': location,
        'description': desc,
        'colorId': color,
        'start': {
            'dateTime': start_time,
            'timeZone': timezone,
        },
        'end': {
            'dateTime': end_time,
            'timeZone': timezone,
        },
        'recurrence': [
            CONFIG['recurrence']
        ],
        'attendees': [
            {'email': CONFIG['personal_email']},
        ],
        'reminders': {
            'useDefault': CONFIG['reminders.useDefault'],
            'overrides': [
                #{
                #    'method': 'email',
                #    'minutes': 24 * 60
                #},
                {
                    'method': 'popup',
                    'minutes': CONFIG['reminder.popup']
                },
            ],
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('[INFO] Event created: %s' % (event.get('htmlLink')))


def delete_calendar(calendar_id):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    service.calendars().delete(calendar_id).execute()


def clean_primary_cal():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    service.calendars().clear('primary').execute()

