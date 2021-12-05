#!/usr/bin/python3


def compute(lst1, lst2, lst3, lst4):

    node_num = 0

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
        # request bytes sent/rec
        req_by_sent = 0
        req_by_rec = 0
        # request data sent/rec
        req_da_sent = 0
        req_da_rec = 0
        # iterate thought list

        for i in x:
            # if source = node then data is sent
            if i[2] == '192.168.100.1':
                if i[8] == 'request':
                    req_sent = req_sent + 1
                    req_by_sent = req_by_sent + int(i[5])
                    # only actual payload should be not frame length
                    # DATA = Length - mac header, ip header, icmp header (42)
                    req_da_sent = req_da_sent + int(i[5])
                    req_da_sent = req_da_sent - 42
                if i[8] == 'reply':
                    reply_sent = reply_sent + 1
            # if not node data is received
            if i[2] != '192.168.100.1':
                if i[8] == 'request':
                    req_rec = req_rec + 1
                    req_by_rec = req_by_rec + int(i[5])
                    # only actual payload should be not frame length
                    # DATA = Length - mac header, ip header, icmp header (42)
                    req_da_rec = req_da_rec + int(i[5])
                    req_da_rec = req_da_rec - 42
                if i[8] == 'reply':
                    reply_rec = reply_rec + 1

        # Print out what node is being printed
        print("NODE: " + str(node_num+1))
        print("Echo Requests Sent", req_sent, "\nEcho Requests Received", req_rec)
        print("Echo Replies Sent", reply_sent, "\nEcho Replies Received ", reply_rec)

        print("Echo Request Bytes Sent ", req_by_sent)
        print("Echo Request Bytes Received ", req_by_rec)

        print("Echo Request Data Sent ", req_da_sent)
        print("Echo Request Data Received ", req_da_rec, "\n\n")
        node_num = node_num + 1
        
# Function for Request Data Sent
def request_data_sent(node,ip):
    sum=0
    for k in node:
        if k[2]==ip and k[8]=="request":
            sum+=int(k[5])-2
    return sum

# Function for Request Bytes Sent
def request_bytes_sent(node,ip):
    sum=0
    for k in node:
        if k[2] == ip and k[8] == "request":
            sum+=int(k[5])
    return sum

# Function for average RTT(ms)
def average_RTT(node, ip):
    sum=0
    count=0
    for i in range(0, len(node), 2):
        if node[i][2]==ip and node[i][8]=="request":
            sum+=float(node[i+1][1])-float(node[i][1])
            count+=1
    return (sum/count)*1000

# Function for Echo Request Throughput(kB/sec)
def echo_request_throughput(node, ip):
    sum=0
    for i in range(0, len(node), 2):
        if node[i][2]==ip and node[i][8]=="request":
            sum+=(float(node[i+1][1])-float(node[i][1]))
    return ((request_bytes_sent(node, ip)/sum)/1000)

# Function for Echo Request Goodput(kB/sec)
def echo_request_goodput(node, ip):
    sum=0
    for i in range(0, len(node), 2):
        if node[i][2] == ip and node[i][8] == "request":
            sum+=(float(node[i+1][1])-float(node[i][1]))
    return (request_data_sent(node, ip)/sum)/1000

# Function for Average Reply Delay(us)
def average_reply_delay(node, ip):
    sum=0
    temp=0
    for i in range(0, len(node), 2):
        if node[i][3]==ip and node[i][8]=="request":
            sum+=(float(node[i+1][1])-float(node[i][1]))
            temp+=1
    return (sum/temp)*1000000

# Function for Average Echo Request Hop Count
def average_hop_count(node, ip):
    temp=129
    sum=0
    count=0
    for i in range(0, len(node)):
        if node[i][8]=="reply" and node[i][3]==ip:
            sum+=(temp-(int("".join(filter(str.isdigit, node[i][11])))))
        if node[i][8]=="request" and node[i][2]==ip:
            count+=1
    return float(sum)/float(count)

