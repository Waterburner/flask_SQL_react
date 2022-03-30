# tutorial
# https://www.youtube.com/watch?v=7LNl2JlZKHA

# python3 -m venv <nameOfTheVirtualEnviroment>
# activate: source <nameOfTheVirtualEnviroment>/bin/activate
# pip3 install flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, I'm flask!"

# Members API Route

@app.route("/members")
def members():
    return {"members": ["member1", "Member2", "Member3"]}



if __name__ == "__main__":
    app.run(debug=True)