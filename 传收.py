from flask import Flask, render_template, jsonify

app = Flask(__name__)


# @app.route('/')
#
#
# def index():
#
#
#     return render_template('2.html')


@app.route('/data')


def data():


    return jsonify({'key': 'value'})

@app.route('/')

def index():
    return render_template('1.html', title=a, message=b)


if __name__ == '__main__':
	a='Hello, Flask!'
	b='This is a message from Flask.'
	app.run(debug=True)