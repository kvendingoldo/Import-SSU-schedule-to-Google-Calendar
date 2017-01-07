import json


def get_day(date, with_response=True):
    inside = dict()
    inside[u'date'] = date
    inside[u'subjects'] = list()

    for subject in subjects:
        inside['subjects'].append(subject)

    if with_response:
        response = dict()
        response[u'response'] = inside
        return json.dumps(response, ensure_ascii=True, sort_keys=True)
    else:
        return json.dumps(inside, ensure_ascii=True, sort_keys=True)


def get_week(week_number):
    response = dict()
    days = dict()
    days[u'week'] = week_number
    days[u'days'] = list()
    response[u'response'] = days

    dates = ["1.10", "2.10"]  # replace to get_dates(week)

    for date in dates:
        days[u'days'].append(json.loads(get_day(date, False)))

    return json.dumps(response, ensure_ascii=True, sort_keys=True)


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
