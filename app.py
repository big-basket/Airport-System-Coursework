from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/mappage')
def mappage():
    return render_template('mappage.html')

@app.route('/alertpage')
def alertpage():
    return render_template('alertpage.html')

@app.route('/settings')
def settingspage():
    return render_template('settingspage.html')

if __name__ == '__main__':
    app.run(debug=True)