#!/usr/bin/python3.5
#  -*- coding: utf-8 -*-

import json


def get_day(subjects, with_response=True):
    inside = dict()
    inside[u'subjects'] = list()

    for subject in subjects:
        inside['subjects'].append(subject)

    if with_response:
        response = dict()
        response[u'response'] = inside
        return json.dumps(response, ensure_ascii=True, sort_keys=True) \
            .encode('utf8').decode('unicode-escape')
    else:
        return json.dumps(inside, ensure_ascii=True, sort_keys=True) \
            .encode('utf8').decode('unicode-escape')


def get_week(raw_week_data):
    response = dict()
    days = dict()
    # days[u'week'] = week_number
    days[u'days'] = list()
    response[u'response'] = days

    for date in range(1, 7):
        days[u'days'].append(json.loads(get_day(raw_week_data[date], False)))

    return json.dumps(response, ensure_ascii=True, sort_keys=True) \
        .encode('utf8').decode('unicode-escape')


def error_response(code):
    error = dict()
    error['error_code'] = code
    generated_msg = ""
    error['error_msg'] = generated_msg

    response = dict()
    response[u'error'] = error
    return json.dumps(response, ensure_ascii=True, sort_keys=True)
