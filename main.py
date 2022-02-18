from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/helpline')
def help():
    return render_template('helpline.html')
    
@app.route('/track', methods=['post'])
def track():
    if request.method == 'POST':
        url = request.form['user_url']
        resp = requests.get(url)
        redirect_url = resp.history
        return render_template('track.html', endurl = resp, redirect = redirect_url)

if __name__ == '__main__':
    app.run(debug=True)