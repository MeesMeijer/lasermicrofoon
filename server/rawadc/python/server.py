path = 'C:\\Users\\meesr\\Documents\\GitHub\\lasermicrofoon\\server\\rawadc\\javascript\\adc.raw'
leng = 16384 * 2 # 2 want 16 bits 

Fs = 44000
bits = 16
Ts = 1/44000
CHUCK = 1024 ## bytes = 512 samples


print((Ts*leng )/ 2, "sec music")

import wave 

with open(path, "rb") as file:

    data = file.read()

    print(len(data)/leng)

    firstSamples = data[0:leng]

    with wave.open("test.wav", "wb") as out_f:
        out_f.setnchannels(1)
        out_f.setsampwidth(2) # number of bytes
        out_f.setframerate(44000)
        out_f.writeframesraw(firstSamples)

        print(out_f.getnframes() / out_f.getframerate())



