import math
from audiolazy.lazy_filters import ZFilter, z


# bandpass Filter
WH, WL = 300,200
W0 =  math.sqrt(WH*WL)
BW = WH-WL

Fs = 44_000
Ts = 1/Fs

num = (1 - (z**-1)) * (BW) * Ts 
denum = 1-2*(z**-1) + (z**-2) * Ts * BW + ((W0)**2)
filt = num/denum
data = [1, 5, -4, -7, 9]
stream_result = filt(data)

print(list(stream_result))