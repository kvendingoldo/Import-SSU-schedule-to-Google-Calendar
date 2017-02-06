#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

import datetime
from math import floor


def get_parity(current_day=datetime.datetime.now().day):
    """This function is my modification of SSU Parity logic (https://github.com/vadim8kiselev/ssu-parity)
    written by @vadim8kiselev"""

    parity = "знам."
    now = datetime.datetime.now()
    current_month = now.month
    current_year = now.year

    day_first_of_september = datetime.datetime(current_year, 9, 1).weekday()
    day_first_of_january = datetime.datetime(current_year, 1, 1).weekday()

    if day_first_of_september == 2:
        date_first_monday_in_september = 7
    else:
        date_first_monday_in_september = (9 - day_first_of_september) % 7

    if day_first_of_january == 2:
        date_first_monday_in_january = 7
    else:
        date_first_monday_in_january = (9 - day_first_of_january) % 7

    count_full_week_before_ny = floor((datetime.date.today() - datetime.date(current_year, 9, 1)).days / 7)
    count_full_week_after_ny = floor((datetime.date.today() - datetime.date(current_year, 1, 1)).days / 7)

    if current_month > 9 and count_full_week_before_ny % 2 != 0:
        parity = "числ."
    elif current_month == 9:
        if current_day >= date_first_monday_in_september and count_full_week_before_ny % 2 != 0:
            parity = "числ."
        elif current_day < date_first_monday_in_september:
            parity = "числ."
    elif current_month < 9:
        if current_month <= 5 and current_month >= 1:
            if (current_month == 1) and (current_day < date_first_monday_in_january):
                if date_first_monday_in_september == 1 or day_first_of_september > 5:
                    parity = "числ."
            elif count_full_week_after_ny % 2 == 0:
                parity = "числ."
        elif current_month > 5:
            parity = "summer"

    return parity


def get_opposite_parity():
    parity = get_parity()
    if parity == "знам.":
        return "числ."
    else:
        return "знам."
