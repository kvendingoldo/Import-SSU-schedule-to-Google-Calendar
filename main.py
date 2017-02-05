#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import json
import sys

import api as api
import gen_schedule_matrix as gen_matrix
import wrapper_over_cal_api as wrap


def main(argv):
    with open('config.json', 'r') as conf_file:
        config = json.load(conf_file)

    schedule_matrix = gen_matrix.generate_schedule_matrix("http://www.sgu.ru/schedule/"
                                                          + config['department'] + "/"
                                                          + config['study_mode'] + "/"
                                                          + config['group'])
    json_week = api.get_week(schedule_matrix)

    wrap.clear_cal()

    print("[INFO] Start loading schedule...")
    #wrap.put_week_to_cal(json_week)
    print("[INFO] Loading is finished.")


if __name__ == "__main__":
    main(sys.argv)
