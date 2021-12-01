#!/usr/bin/python3
def parse(filename, lst) :
	with open(filename, "r") as file:
		lines=file.readlines()
		for line in lines:
			lst.append(line.strip().split())
