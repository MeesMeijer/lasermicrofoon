import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

path = 'C:\\Users\\meesr\\Documents\\GitHub\\lasermicrofoon\\server\\rawadc\\javascript\\adc.raw'
leng = 16384 * 2 # 2 want 16 bits 

Fs = 44000
bits = 16
Ts = 1/44000
CHUCK = 1024 ## bytes = 512 samples


print((Ts*leng )/ 2, "sec music per .raw file ")

with open(path, "rb") as file:

    data = file.read()
    
    signal = np.frombuffer(data, np.uint16)

    fs = 44000
    secs = len(signal) / fs
    Time = np.linspace(0, secs, num=len(signal))
    print(f"plotting {secs} sec of raw audio")

    

    # plt.figure(1)
    # plt.title("Signal Wave...")
    # plt.plot(Time, signal)
    # plt.show()




# spf = wave.open("test.wav", "r")

# # Extract Raw Audio from Wav File
# signal = spf.readframes(-1)
# intType = np.uint8 if spf.getsampwidth() == 1 else np.uint8  # width 1 or 2 times 8 bits (16 bits support)
