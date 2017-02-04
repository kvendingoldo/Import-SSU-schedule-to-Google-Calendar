#!/usr/bin/python3
# -*- coding: utf-8 -*-

import google_api as ga
import json


def put_to_calc_subj(subj, put_extra_subject=False):
    summary = subj['name'] + " (" + subj['type'] + ")"
    location = subj['place']
    desc = subj['teacher']
    start_time = ""
    end_time = ""

    if subj['other'] == "":
        print(summary, location, desc, start_time, end_time)
        #ga.insert(summary, location, desc, start_time, end_time, timezone='Europe/Samara')

    if put_extra_subject:
        ga.insert(summary, location, desc, start_time, end_time, timezone='Europe/Samara')


def put_to_calc_day(day):
    for index in range(0, 9):
        if type(day[index]) is dict:
            print(day[index])

        #put_to_calc_subj(day[index])


def put_to_calc_week(j_week):
    week = json.loads(j_week, encoding="utf-8")
    #for index in range(0,6):
    #    put_to ((((week['response'])['days'])[index])['subjects'])
    put_to_calc_day((((week['response'])['days'])[0])['subjects'])






