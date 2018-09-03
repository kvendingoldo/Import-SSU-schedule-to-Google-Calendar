#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

from __future__ import print_function

import json


class Config(object):
    data = json.dumps({})

    def __init__(self, *args, **kwargs):
        s = len(args)
        if s is 1:
            if len(kwargs) > 0:
                self.load(kwargs.get('config_file', 0))
        else:
            self.load()

    def load(self, config_file='../../resources/config.json'):
        with open(config_file, 'r') as cfg_file:
            self.data = json.load(cfg_file)

    def update(self, parameter, value):
        self.data[parameter] = value
