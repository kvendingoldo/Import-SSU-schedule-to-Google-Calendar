import json

subjects = []
subj = dict()

subj['parity'] = '21'
subj['type'] = '2'
subj['other'] = '3'
subj['name'] = '4'
subj['teacher'] = '5'
subj['place'] = '6'

subjects.append(subj)
subj = dict()

subj['parity'] = 'a'
subj['type'] = 'b'
subj['other'] = 'c'
subj['name'] = 'd'
subj['teacher'] = 'e'
subj['place'] = 'f'

subjects.append(subj)


def get_day(date):
    response = dict()
    # response[u'status'] = "success" # add error
    response[u'date'] = date
    response[u'subjects'] = list()
    subjects_number = 10
    response['subjects'].append(subjects_number)

    for subject in subjects:
        response['subjects'].append(subject)
    return json.dumps(response, ensure_ascii=True, sort_keys=True)


def get_week(week_number):
    response = dict()
    response[u'week_number'] = week_number
    response[u'days'] = list()

    # function for get dates

    dates = ["1.10", "2.10"]

    for date in dates:
        response['days'].append(json.loads(get_day(date)))

    return response


def get_dates(week):
    return "null"


def error_response(status):
    error = dict()
    error['status'] = status
    # error['detail']

    response = dict()
    response[u'errors'] = list()

    response[u'errors'].append(error)

    return response


# print get_day('01.10.2017')
print get_week(1)

print error_response("404")
