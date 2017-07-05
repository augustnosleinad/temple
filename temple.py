from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/game', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        command = request.form['command']

        return render_template(
            'temple.html',
            command=command,
        )

    return render_template('temple.html')
