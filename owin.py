#!/usr/bin/env python3

import gzip
import json
import sys

import pylab

def main():
    x, y1, y2 = [0], [0], [0]
    with gzip.open(sys.argv[1]) as filep:
        measurements = json.load(filep)['Download']['ServerMeasurements']
        for m in measurements:
            tcpinfo, bbrinfo = m["TCPInfo"], m["BBRInfo"]
            elapsed_time = float(tcpinfo["ElapsedTime"]) / 1e06
            bytes_sent = tcpinfo["BytesSent"]
            bytes_acked = tcpinfo["BytesAcked"]
            x.append(elapsed_time)
            y1.append((bytes_sent - bytes_acked) / 1024.0 / 1024.0)
    pylab.plot(x, y1, "o-", label="OWIN")
    pylab.legend()
    pylab.grid()
    pylab.show()

if __name__ == "__main__":
    main()
