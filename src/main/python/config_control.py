#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

from __future__ import print_function

import json

FILE = "resources/config.json"


def load():
    with open(FILE, 'r') as cfg_file:
        return json.load(cfg_file)


def reload():
    return load()


def upd_par(par, value):
    current_config = load()
    current_config[par] = value
    with open(FILE, 'w') as cfg_file:
        json.dump(current_config, cfg_file)
