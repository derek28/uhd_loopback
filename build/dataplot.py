#! /usr/bin/env python3

import matplotlib.pyplot as plt
import struct
import cmath
import math
import scipy.fftpack as pyfft
import numpy as np

fd = open("usrp_samples.dat", "rb")
dat = fd.read()
fd.close()

B = 8
b = 4
NFFT = 4096
Fs = 5000     # kHz

l = int(len(dat) / B)
print("l = ", l)

r = [complex(0,0) for i in range(NFFT)]
for i in range(l - NFFT, l, 1):             # only takes the last 4096 samples
    Q = struct.unpack('<f', dat[i * B : i * B + b]) # little endian
    I = struct.unpack('<f', dat[i * B + b: i * B + B]) # little endian
    #Q = struct.unpack('>h', dat[i * 4 : i * 4 + 2]) # big endian
    #I = struct.unpack('>h', dat[i * 4 + 2: i * 4 + 4]) # big endian
    #print("Q =", Q[0], "I=", I[0]);
    r[i - l + NFFT] = complex(I[0], Q[0])

y = pyfft.fft(r)
y_shift = [complex(0, 0) for i in range(NFFT)]
y_shift[:2048] = y[2048:]
y_shift[2048:] = y[:2048]

print(len(y_shift))

y_mag = [0.0 for i in range(NFFT)]
for i in range(NFFT):
    y_mag[i] = 10 * (math.log(abs(y_shift[i]) ** 2, 10));

f = np.arange(-Fs/2, Fs/2, Fs/NFFT)

plt.grid()
plt.xlabel("Frequency / kHz")
plt.ylabel("Power Spectral Density / dB")
plt.plot(f, y_mag)
plt.show()
