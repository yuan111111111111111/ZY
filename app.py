from flask import Flask,render_template

app = Flask(__name__)

@app.route('/index.html')
def index(): # put application's code here
    return render_template('index.html')

@app.route('/about.html')
def about(): # put application's code here
    return render_template('about.html')

@app.route('/index2.html')
def index2(): # put application's code here
    return render_template('index2.html')

@app.route('/blog.html')
def blog(): # put application's code here
    return render_template('blog.html')

@app.route('/services.html')
def services(): # put application's code here
    return render_template('services.html')

@app.route('/shortcodes.html')
def shortcodes(): # put application's code here
    return render_template('shortcodes.html')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
