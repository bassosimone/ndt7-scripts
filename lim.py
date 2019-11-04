#!/usr/bin/env python3

import gzip
import json
import sys

import pylab

def main():
    x, y1, y2, y3 = [0], [0], [0], [0]
    with gzip.open(sys.argv[1]) as filep:
        measurements = json.load(filep)['Download']['ServerMeasurements']
        for m in measurements:
            tcpinfo, bbrinfo = m["TCPInfo"], m["BBRInfo"]
            elapsed_time = float(tcpinfo["ElapsedTime"]) / 1e06
            app_limited = tcpinfo["AppLimited"]
            sndbuf_limited = float(tcpinfo["SndBufLimited"]) / tcpinfo["ElapsedTime"]
            rwnd_limited = float(tcpinfo["RWndLimited"]) / tcpinfo["ElapsedTime"]
            x.append(elapsed_time)
            y1.append(app_limited)
            y2.append(sndbuf_limited)
            y3.append(rwnd_limited)
    pylab.plot(x, y1, "o-", label="AppLimited")
    pylab.plot(x, y2, "s-", label="SndBufLimited")
    pylab.plot(x, y3, "^-", label="RWndLimited")
    pylab.legend()
    pylab.grid()
    pylab.show()

if __name__ == "__main__":
    main()
