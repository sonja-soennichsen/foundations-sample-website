from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', page_title="Studying at Code")


@app.route('/first-page')
def first_page():
    return render_template('first-page.html', page_title="Admissions")


@app.route('/second-page')
def second_page():
    return render_template('second-page.html', page_title="Study Programs")

# add additonal pages here using a similar format as above


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
