#!/usr/bin/python3
from filter_packets import *
from packet_parser import *
from compute_metrics import *

def main():
    filter()
    parse()
    compute()
if __name__ == '__main__':
    main()