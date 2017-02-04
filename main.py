#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import sys
import api as api
import generate_schedule_matrix as gen_matrix

import wrapper_for_calc as wrap


def main(argv):
    schedule_matrix = gen_matrix.generate_schedule_matrix("http://www.sgu.ru/schedule/mm/do/313")
    json_week = api.get_week(schedule_matrix)
    wrap.put_to_calc_week(json_week)


if __name__ == "__main__":
    main(sys.argv)
