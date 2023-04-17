from flask import Flask, request, render_template
import pyqrcode

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def qr_code_generator():
    if request.method == 'POST':
        url = request.form['urlInput']
        qr = pyqrcode.create(url)
        qr.png('qrcode/static/qr_code.png', scale=6)
        return render_template('index.html', qr_code=True)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
