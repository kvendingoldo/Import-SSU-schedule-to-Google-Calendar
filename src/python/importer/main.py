#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

from entity import config as cfg
from entity import calendar as cal
from generator import schedule as sch

def main():
    config = cfg.Config()
    calendar = cal.Calendar(configuration=config)

    schedule = sch.generate('http://www.sgu.ru/schedule/%s/%s/%s' % (
        config.data['department'], config.data['study_mode'], config.data['group']))

    #calendar.clear_cal()
    calendar.put_week(schedule)


if __name__ == '__main__':
    main()
