#!/usr/bin/env python
# -*- coding: utf-8 -*-

import api as api
import sys
import generate_schedule_matrix as gen_matrix


def main(argv):
    SCHEDULE_MATRIX = gen_matrix.generate_schedule_matrix("http://www.sgu.ru/schedule/mm/do/313")

    a = api.get_week(SCHEDULE_MATRIX)

    print a

if __name__ == "__main__":
    main(sys.argv)