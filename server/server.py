from flask import Flask, redirect, jsonify, current_app, make_response, url_for, request, session
import jwt, datetime




users = {
    "test": {
        "username": "test",
        "password": "test" 
    }
}

app = Flask(__name__)
app.secret_key = "121212oawisudhv092f98-`2hf98h23f98h2hfu92-`bf-82hfb8"

def createJwt(user):
    jwtToken = jwt.encode({'username': user, "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=10)}, key=app.secret_key)
    users[user]['jwt'] = jwtToken
    return jwtToken

@app.route("/login", methods=['POST'])
def login():

    formJson : dict = request.json
    # print(formJson)
    user = users.get(formJson.get("username"), False)
    if not user: return jsonify({"error": True})
    if user['password'] != formJson.get("password"): return jsonify({"error": True})
    if not user: return jsonify({"error": True})
    
    
    token = createJwt(user['username'])

    session['user'] = user
    session['jwt-token'] = token

    return jsonify({"error": False, "user": user})


@app.route("/logout", methods=['POST'])
def logout():
    print(rawtoken := request.headers.get("Authorization"))
    
    try:
        token = jwt.decode(rawtoken, key=app.secret_key, algorithms=['HS256'])
    except Exception as ex:
        print(ex)
        return jsonify({"error": True})

    print(token)
    print()

    if users[token['username']].get('jwt') != rawtoken: return jsonify({"error": True})
    del users[token['username']]["jwt"]
    return jsonify({"error": False, "secret": 'Mees Heeft Altijd Gelijk!'})


@app.route("/protected")
def prot():
    # if (request.headers.get(""))
    print(rawtoken := request.headers.get("Authorization"))
    
    try:
        token = jwt.decode(rawtoken, key=app.secret_key, algorithms=['HS256'])
    except Exception as ex:
        print(ex)
        return jsonify({"error": True})

    print(token)
    print()

    if users[token['username']].get('jwt') != rawtoken: return jsonify({"error": True})
        
    return jsonify({"error": False, "secret": 'Mees Heeft Altijd Gelijk!'})




if __name__ == "__main__":
    app.run("192.168.2.7", 5000, debug=True)
