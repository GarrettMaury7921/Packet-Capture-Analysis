#!/usr/bin/python3
from filter_packets import *
from packet_parser import *
from compute_metrics import *
import sys

def main():
    filter()
    lst1,lst2,lst3,lst4=[],[],[],[]
    parse(sys.path[0]+"/../Captures/Node1_filtered.txt",lst1)
    parse(sys.path[0]+"/../Captures/Node2_filtered.txt",lst2)
    parse(sys.path[0]+"/../Captures/Node3_filtered.txt",lst3)
    parse(sys.path[0]+"/../Captures/Node4_filtered.txt",lst4)    
    compute()
if __name__ == '__main__':
    main()
