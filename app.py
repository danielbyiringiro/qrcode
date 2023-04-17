from flask import Flask, request, render_template
import pyqrcode
import os
import uuid

app = Flask(__name__)

qr_code_counter = 0

@app.route('/', methods=['GET', 'POST'])
def qr_code_generator():
    global qr_code_counter

    if request.method == 'POST':
        url = request.form['urlInput']
        qr = pyqrcode.create(url)
        filename = str(uuid.uuid4()) + '.png'
        qr.png(os.path.join('static', filename), scale=6)
        qr_code_counter += 1  # Increment the counter
        return render_template('index.html', qr_code=True, filename=filename, qr_code_counter=qr_code_counter)
    return render_template('index.html', qr_code_counter=qr_code_counter)

if __name__ == '__main__':
    app.run(debug=True)
