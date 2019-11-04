#!/usr/bin/env python3

import gzip
import json
import sys

import pylab

def main():
    x, y1, y2, y3, y4 = [0], [0], [0], [0], [0]
    with gzip.open(sys.argv[1]) as filep:
        measurements = json.load(filep)['Download']['ServerMeasurements']
        for m in measurements:
            tcpinfo, bbrinfo = m["TCPInfo"], m["BBRInfo"]
            maxbandwidth = bbrinfo["MaxBandwidth"] * 8 / 1e06
            elapsed_time = float(tcpinfo["ElapsedTime"]) / 1e06
            if elapsed_time < 0.01:
                continue
            bytes_acked = tcpinfo["BytesAcked"] * 8 / 1e06
            speed = bytes_acked / elapsed_time
            delivery_rate = tcpinfo["DeliveryRate"] * 8 / 1e06
            pacing_rate = tcpinfo["PacingRate"] * 8 / 1e06
            x.append(elapsed_time)
            y1.append(maxbandwidth)
            y2.append(speed)
            y3.append(delivery_rate)
            y4.append(pacing_rate)
    pylab.plot(x, y1, "o-", label="MaxBandwidth")
    pylab.plot(x, y2, "s-", label="Speed")
    pylab.plot(x, y3, "^-", label="DeliveryRate")
    pylab.plot(x, y3, "x-", label="PacingRate")
    pylab.legend()
    pylab.grid()
    pylab.show()

if __name__ == "__main__":
    main()
