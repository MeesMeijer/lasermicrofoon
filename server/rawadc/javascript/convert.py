import wave

with open("adc.raw", "rb") as inp_f:
    data = inp_f.read()
    with wave.open("adc2.wav", "wb") as out_f:
        out_f.setnchannels(1)
        out_f.setsampwidth(2) # number of bytes
        out_f.setframerate(44100)
        out_f.writeframesraw(data)