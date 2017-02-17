#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

from __future__ import print_function

import datetime
import json

import cal_api as ca
import config_control as cfg
from parity import get_parity, get_opposite_parity

CONFIG = cfg.load()
timedelta = 0


def get_subject_time(subj_day_number, subj_number):
    start_time = 0
    end_time = 0

    global timedelta
    date = datetime.datetime.now().date()
    day = str(date + datetime.timedelta(subj_day_number + timedelta - date.weekday())) + "T"

    if subj_number == 1:
        start_time = day + "08:20"
        end_time = day + "09:50"
    elif subj_number == 2:
        start_time = day + "10:00"
        end_time = day + "11:35"
    elif subj_number == 3:
        start_time = day + "12:05"
        end_time = day + "13:40"
    elif subj_number == 4:
        start_time = day + "13:50"
        end_time = day + "15:25"
    elif subj_number == 5:
        start_time = day + "15:35"
        end_time = day + "17:10"
    elif subj_number == 6:
        start_time = day + "17:20"
        end_time = day + "18:40"
    elif subj_number == 7:
        start_time = day + "18:45"
        end_time = day + "20:05"
    elif subj_number == 7:
        start_time = day + "20:10"
        end_time = day + "21:30"
    else:
        print(u'[ERROR] index is out of range')

    appendix = ":00.000000"

    return start_time + appendix, end_time + appendix


def put_subj_to_cal(subj, day_number, subj_number, parity):
    if 'couple' in subj:
        if parity == "числ.":
            subj = (subj['couple'])[0]
        else:
            subj = (subj['couple'])[1]

    print(parity)

    summary = subj['name'] + " (" + subj['type'] + ")"
    location = subj['place']
    desc = subj['teacher']
    start_time, end_time = get_subject_time(day_number, subj_number)

    if subj['type'] == "лек.":
        color = CONFIG['color.lesson']
    elif subj['type'] == "пр.":
        color = CONFIG['color.practice']
    elif subj['type'] == "лаб.":
        color = CONFIG['color.laboratory_work']
    else:
        color = CONFIG['color.default']

    if subj['other'] == "":
        print(summary)
        #ca.insert(summary, location, color, desc, start_time, end_time, CONFIG['calendarId'])
    elif subj['other'] in CONFIG['include.specializations']:
        pass
        #ca.insert(summary, location, color, desc, start_time, end_time, CONFIG['calendarId'])


def put_day_to_cal(day, day_number, parity):
    for index in range(0, 9):
        if type(day[index]) is dict:
            put_subj_to_cal(day[index], day_number, index, parity)


def put_week_to_cal(j_week):
    print("[INFO] Start loading schedule...")
    global timedelta, CONFIG
    week = json.loads(j_week, encoding="utf-8")
    parity = get_parity()
    if (int)(CONFIG['recurrence.count']) > 1:

        cfg.upd_par("system.calendar.interval", "2")
        CONFIG = cfg.reload()

        for index in range(0, 6):
            put_day_to_cal((((week['response'])['days'])[index])['subjects'], index, parity)

        timedelta = 7
        for index in range(0, 6):
            put_day_to_cal((((week['response'])['days'])[index])['subjects'], index, get_opposite_parity())

        # return default timedelta and system.calendar.interval
        timedelta = 0
        cfg.upd_par("system.calendar.interval", "1")
    else:
        for index in range(0, 6):
            put_day_to_cal((((week['response'])['days'])[index])['subjects'], index, parity)
    print("[INFO] Loading is finished.")


def clear_cal():
    print("[WARNING] Do you really want clean your calendar?(Y/N)")
    ans = input()
    if ans == "Y" or ans == "YES" or ans == "y" or ans == "yes":
        print("[INFO] Clean started...")
        ca.clean_primary_calendar(CONFIG['calendarId'])
        print("[INFO] Clean finished")
    else:
        print("[INFO] Clean cancelled")
