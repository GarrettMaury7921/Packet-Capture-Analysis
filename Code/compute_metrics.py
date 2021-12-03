#!/usr/bin/python3
from packet_analyzer import *


def compute(lst1, lst2, lst3, lst4):
    for x in [lst1, lst2, lst3, lst4]:
        if x == lst1:
            ip = '192.168.100.1'
        elif x == lst2:
            ip = '192.168.100.2'
        elif x == lst3:
            ip = '192.168.200.1'
        else:
            ip = '192.168.200.2'
        req_sent = 0
        req_rec = 0
        reply_rec = 0
        reply_sent = 0
        #request bytes sent/rec
        req_by_sent = 0
        req_by_rec = 0
        #request data sent/rec
        req_da_sent = 0
        req_da_rec = 0
        #iterate thought list
    
        for i in x:
            #if source = node then data is sent
            if i[2] == '192.168.100.1': 
                if i[8] == 'request':
                    req_sent = req_sent + 1
                    req_by_sent = req_by_sent + int(i[5])
                if i[8] == 'reply':
                    reply_sent = reply_sent + 1
                    #only actual payload should be not frame length
                    #req_da_sent = req_da_sent + int(i[5])
            #if not node data is recieved
            if i[2] != '192.168.100.1': 
                if i[8] == 'request':
                    req_rec = req_rec + 1
                    req_by_rec = req_by_rec + int(i[5])
                if i[8] == 'reply':
                    reply_rec = reply_rec + 1
                    #only actual payload should be not frame length
                    #req_da_rec = req_da_rec + int(i[5])
        print("req sent", req_sent, "\nreq rec", req_rec)        
        print("Reply sent", reply_sent , "\nReply rec ", reply_rec)
        print(req_by_sent, req_by_rec, req_da_sent, req_da_rec, "\n\n")
    
