from flask import Flask, send_file
from service.dowload_file_from_n_link import download_file_from_n_link
app = Flask(__name__)

@app.route('/get_file')
def get_file():
    file = download_file_from_n_link()
    return send_file(file, as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)