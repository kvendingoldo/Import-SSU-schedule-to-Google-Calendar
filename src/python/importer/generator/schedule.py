#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

from __future__ import print_function

import re
import urllib.request as ulib
import numpy as np

from bs4 import BeautifulSoup

from utils import json_view as jw


def get_time(response):
    soup = BeautifulSoup(response, 'lxml')
    tmp = str(soup.findAll('th'))

    soup = BeautifulSoup(tmp, 'lxml')
    invalid_tags = ['html', 'body', 'p', 'th']

    for tag in invalid_tags:
        for match in soup.findAll(tag):
            match.replaceWithChildren()

    print(re.sub(r'<br/>', '-', str(soup)))


def delete_html_tag(raw_html):
    return re.sub(r'<.*?>', '', raw_html)


def get_elem_by_class(soup, class_name, index=0):
    return delete_html_tag(str((soup.findAll("div", {"class": class_name})[index])))


def check_unique_subj(data):
    return data.count('l-pr-r', 0, len(data))


def prepare_subject(element):
    soup = BeautifulSoup(str(element), "lxml")
    subject = dict()

    if check_unique_subj(str(element)) == 2:
        subject['couple'] = list()
        for index in range(2):
            subj = dict()
            subj['parity'] = get_elem_by_class(soup, "l-pr-r", index)
            subj['type'] = get_elem_by_class(soup, "l-pr-t", index)
            subj['other'] = get_elem_by_class(soup, "l-pr-g", index)
            subj['name'] = get_elem_by_class(soup, "l-dn", index)
            subj['teacher'] = get_elem_by_class(soup, "l-tn", index)
            subj['place'] = get_elem_by_class(soup, "l-p", index)
            subject['couple'].append(subj)
    else:
        subject['parity'] = get_elem_by_class(soup, "l-pr-r")
        subject['type'] = get_elem_by_class(soup, "l-pr-t")
        subject['other'] = get_elem_by_class(soup, "l-pr-g")
        subject['name'] = get_elem_by_class(soup, "l-dn")
        subject['teacher'] = get_elem_by_class(soup, "l-tn")
        subject['place'] = get_elem_by_class(soup, "l-p")

    return subject


def generate(url):
    request = ulib.Request(url)
    request.add_header('Accept-Encoding', 'utf-8')
    response = ulib.urlopen(request)
    soup = BeautifulSoup(response, "lxml")
    raw_data = soup.find_all('td', {'id': re.compile(r'\d_\d')})
    if not raw_data:
        raise Exception('[ERROR] response is empty')
    matrix = np.empty((10, 10), dtype=object)
    matrix[:] = ""

    for element in raw_data:
        pattern = re.compile(r"<td\sclass=\"\"\sid=\"\d_\d\">(.+)</td>")
        if pattern.match(str(element)):
            subject = prepare_subject(element)
            pattrn = re.compile(r'\d_\d')
            subject_number = "".join(pattrn.findall(str(element)))
            i = int(subject_number[0])
            j = int(subject_number[2])
            matrix[i][j] = subject

    return jw.get_week(matrix.transpose())
