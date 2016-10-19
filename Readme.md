pyngcollector
=============

Collects RTT metrics based on ICMP

# Usage:
```
python pyngcollector <dest> <num_packet>
```
# Args
- dest: the destination
- num_packet: the number of ICMP packets

# Output
    - avg: the average RTT time in ms
    - max: the max RTT time in ms
    - min: the min time in ms
    - lost: the number of packets lost

# TODO
- remove those extra WARNING msgs from scapy
- unit tests
- collectd compatible Output
- prometheus compatible endpoint
