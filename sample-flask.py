from flask import Flask
import socket

sampleFlask = Flask(__name__)

@sampleFlask.route("/")
def home():
    return '{}{}'.format("App Version 1.0 and HostName: ", socket.gethostname())


@sampleFlask.route("/status")
def status():
    return "ok", 200

if __name__ == "__main__":
    sampleFlask.run()
