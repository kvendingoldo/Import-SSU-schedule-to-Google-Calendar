#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import re
from bs4 import BeautifulSoup
import numpy as np


def get_time(response):
    soup = BeautifulSoup(response, "lxml")
    tmp = str(soup.findAll('th'))

    soup = BeautifulSoup(tmp, "lxml")
    invalid_tags = ['html', 'body', 'p', 'th']

    for tag in invalid_tags:
        for match in soup.findAll(tag):
            match.replaceWithChildren()

    print re.sub(r'<br/>', '-', str(soup))


def delete_html_tag(raw_html):
    return re.sub(r'<.*?>', '', raw_html)


def get_elem_by_class(soup, class_name):
    return delete_html_tag(str((soup.findAll("div", {"class": class_name})[0])))


def generate_schedule_matrix(url):
    request = urllib2.Request(url)
    request.add_header('Accept-Encoding', 'utf-8')
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "lxml")
    raw_data = soup.find_all('td', {'id': re.compile(r'\d_\d')})
    matrix = np.empty((10, 7), dtype=object)
    matrix[:] = ""

    for element in raw_data:
        pattern = re.compile(r"<td\sclass=\"\"\sid=\"\d_\d\">(.+)</td>")
        if pattern.match(str(element)):
            soup = BeautifulSoup(str(element), "lxml")

            subject = dict()

            subject['parity'] = get_elem_by_class(soup, "l-pr-r")
            subject['type'] = get_elem_by_class(soup, "l-pr-t")
            subject['other'] = get_elem_by_class(soup, "l-pr-g")
            subject['name'] = get_elem_by_class(soup, "l-dn")
            subject['teacher'] = get_elem_by_class(soup, "l-tn")
            subject['place'] = get_elem_by_class(soup, "l-p")

            pattrn = re.compile(r'\d_\d')
            subject_number = "".join(pattrn.findall(str(element)))
            i = int(subject_number[0])
            j = int(subject_number[2])
            matrix[i][j] = subject
        else:
            pass
            # print "skip" # write to log
    return matrix.transpose()


SCHEDULE_MATRIX = generate_schedule_matrix("http://www.sgu.ru/schedule/mm/do/313")

for row in SCHEDULE_MATRIX:
    for elem in row:
        for item in elem:
            print item, ":", elem[item]
        print '\n'
    print()
