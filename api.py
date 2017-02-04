#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def get_day(subjects, with_response=True):
    inside = dict()
    #inside[u'date'] = date
    inside[u'subjects'] = list()

    for subject in subjects:
        inside['subjects'].append(subject)

    if with_response:
        response = dict()
        response[u'response'] = inside
        return json.dumps(response, ensure_ascii=True, sort_keys=True).decode('unicode-escape').encode('utf8')
    else:
        return json.dumps(inside, ensure_ascii=True, sort_keys=True).decode('unicode-escape').encode('utf8')


def get_week(raw_week_data):
    response = dict()
    days = dict()
    #days[u'week'] = week_number
    days[u'days'] = list()
    response[u'response'] = days

    #dates = ["1.10", "2.10"]  # replace to get_dates(week)

    for date in range(1, 7):
        days[u'days'].append(json.loads(get_day(raw_week_data[date], False)))

    return json.dumps(response, ensure_ascii=True, sort_keys=True).decode('unicode-escape').encode('utf8')


def get_dates(week):
    # calculate
    return []


def error_response(code):
    error = dict()
    error['error_code'] = code
    generated_msg = ""
    error['error_msg'] = generated_msg

    response = dict()
    response[u'error'] = error
    return json.dumps(response, ensure_ascii=True, sort_keys=True)
