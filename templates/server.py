from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pageB')
def page_b():
    return render_template('register.html')

@app.route('/redirect')
def redirect_to_page_b():
    return redirect(url_for('page_b'))

if __name__ == '__main__':
    app.run(debug=True)
