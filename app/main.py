from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello Shawon! Python Flask App is Running from AWS EC2 ECR Docker. More tutorial: https://shawonruet.com"
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
