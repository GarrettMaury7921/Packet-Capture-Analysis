# Packet-Capture-Analysis
Utilizing .pcap files to see what type of packets are in the file.

- Takes in a .pcap file.
- Creates a text file version of the .pcap file.
- Creates a filtered text file of the newly created text file to see desired packets of a certain protocol.

Finds metrics based on the .pcap file
- Node
- How many echo requests sent
- How many echo replies received
- How many echo request bytes sent
- how many echo request bytes received
- Average RTT (ms)
- Echo Request Throughput (kB/sec)
- Echo Request Goodput (kB/sec)
- Average Reply Delay
- Average Echo Request Hop Count
