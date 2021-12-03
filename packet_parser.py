#!/usr/bin/python3
import re


def parse(filename, lst):
    temp = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            temp.append(line.strip().split())

    for k in temp:
        if len(k) > 2:
            if re.search(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", k[2]):
                lst.append(k)
