#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import api as api
import sys
import generate_schedule_matrix as gen_matrix
import datetime
import google_api as ga
import  wrapper_for_calc as wrap


def main(argv):
    SCHEDULE_MATRIX = gen_matrix.generate_schedule_matrix("http://www.sgu.ru/schedule/mm/do/313")
    json_week = api.get_week(SCHEDULE_MATRIX)
    #print(json_week)

    #ga.insert("Базы Данных (лек.)", "9 корп. ауд. им. Д.И. Лучинина (401)", "Ромайкина О.М.",
    #          "2017-02-04T18:30:00.000000", "2017-02-04T20:30:00.000000")

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    wrap.put_to_calc_week(json_week)



if __name__ == "__main__":
    main(sys.argv)