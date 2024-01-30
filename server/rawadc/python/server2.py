from flask_socketio import SocketIO, emit, send
from flask import Flask, request, make_response
import numpy as np 
import wave
app = Flask(__name__)
# app.secret_key ="123123123"
socketio = SocketIO(app)

buffer: [np.uint16];



@app.route("/adc_samples", methods=["GET", "POST"])
def adcsamples():
    # print(len(request.data))

    f= wave.open("test.wav", "w")
    f.setnchannels(1)
    f.setframerate(44000)
    f.setsampwidth(2)
    f.writeframesraw(request.data)
    f.close()
    return make_response("test", 200)





@socketio.on("connect")
def handleConnect():
    print("Ws connected")



if __name__ == "__main__":
    app.run(
        "192.168.2.3",
        5003, 
        debug=True
    )