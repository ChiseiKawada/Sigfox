from flask import *
from datetime import datetime


app = Flask(__name__)

urls = []
times = []

@app.route("/", methods=["GET", "POST"])
def route():
    if request.method == "GET":
        return """
        <h1>GETだよ</h1>
        """
    elif request.method == "POST":
        return """
        <h1>POSTだよ</h1>
        """
        print("POSTだょ")
        return request.host_url

@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        urls.append(request.host_url)
        times.append(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
        print("postだよ")

    return render_template('test.html', content=urls, times=times) #変更



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)