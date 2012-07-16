from flask import Flask
import boto

sns = boto.connect_sns()
app = Flask(__name__)


@app.route('/')
def main():
    return 'hello world'


@app.route('/batsignal')
def batsignal():
    topic = "arn:aws:sns:us-east-1:209247679858:Test"
    sns.publish(topic, "Something important!")
    return 'okay'
