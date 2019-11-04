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
            minrtt = tcpinfo["MinRTT"] / 1e03
            rtt = tcpinfo["RTT"] / 1e03
            x.append(elapsed_time)
            y1.append(minrtt)
            y2.append(rtt)
    pylab.plot(x, y1, "o-", label="MinRTT")
    pylab.plot(x, y2, "s-", label="RTT")
    pylab.legend()
    pylab.grid()
    pylab.show()

if __name__ == "__main__":
    main()
