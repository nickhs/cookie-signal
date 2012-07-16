from flask import Flask, render_template
import boto

app = Flask(__name__)
sns = boto.connect_sns()

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/batsignal')
def batsignal():
    topic = "arn:aws:sns:us-east-1:209247679858:Test"
    sns.publish(topic, "There are cookies in the vincinity")
    return 'okay'

if __name__ == '__main__':
    app.run(debug=True)
