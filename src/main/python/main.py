#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

import api as api
import config_control as cfg
import gen_schedule_matrix as gen_matrix
import wrapper_over_cal_api as wrap


def main():
    config = cfg.load()

    schedule_matrix = gen_matrix.generate_schedule_matrix("http://www.sgu.ru/schedule/"
                                                          + config['department'] + "/"
                                                          + config['study_mode'] + "/"
                                                          + config['group'])
    json_week = api.get_week(schedule_matrix)

    wrap.clear_cal()
    wrap.put_week_to_cal(json_week)


if __name__ == "__main__":
    main()
