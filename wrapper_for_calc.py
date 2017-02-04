#!/usr/bin/python3.5
#  -*- coding: utf-8 -*-

import json
import datetime
import google_api as ga


with open('config.json', 'r') as f:
    config = json.load(f)

def get_subject_time(day_number, subj_number):

    start_time = 0
    end_time = 0

    date = datetime.datetime.now().date()
    day = str(date + datetime.timedelta(day_number+7-date.weekday()))+"T"

    if subj_number == 1:
        start_time = day + "08:20:00.000000"
        end_time = day + "09:50:00.000000"
    elif subj_number == 2:
        start_time = day + "10:00:00.000000"
        end_time = day + "11:35:00.000000"
    elif subj_number == 3:
        start_time = day + "12:05:00.000000"
        end_time = day + "13:40:00.000000"
    elif subj_number == 4:
        start_time = day + "13:50:00.000000"
        end_time = day + "15:25:00.000000"
    elif subj_number == 5:
        start_time = day + "15:35:00.000000"
        end_time = day + "17:10:00.000000"
    elif subj_number == 6:
        start_time = day + "17:20:00.000000"
        end_time = day + "18:40:00.000000"
    elif subj_number == 7:
        start_time = day + "18:45:00.000000"
        end_time = day + "20:05:00.000000"
    elif subj_number == 7:
        start_time = day + "20:10:00.000000"
        end_time = day + "21:30:00.000000"
    else:
        print(u'[ERROR] index is out of range')

    return start_time, end_time


def put_to_calc_subj(subj, day_number, subj_number, put_extra_subject=False):
    summary = subj['name'] + " (" + subj['type'] + ")"
    location = subj['place']
    desc = subj['teacher']
    start_time, end_time = get_subject_time(day_number, subj_number)

    if subj['type'] == "лек.":
        color = config['lesson_color_id']
    elif subj['type'] == "пр.":
        color = config['practice_color_id']
    elif subj['type'] == "лаб.":
        color = config['laboratory_work_color_id']
    else:
        color = config['default_color']

    if subj['other'] == "":
        ga.insert(summary, location, color, desc, start_time, end_time, timezone='Europe/Samara')

    if put_extra_subject:
        ga.insert(summary, location, color, desc, start_time, end_time, timezone='Europe/Samara')


def put_to_calc_day(day, day_number):
    for index in range(0, 9):
        if type(day[index]) is dict:
            put_to_calc_subj(day[index], day_number, index)


def put_to_calc_week(j_week):
    week = json.loads(j_week, encoding="utf-8")
    for index in range(0, 6):
        put_to_calc_day((((week['response'])['days'])[index])['subjects'], index)
