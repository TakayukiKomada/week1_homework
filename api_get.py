from flask import Flask
from flask import render_template
from flask import request
import json
import requests
import secrets

# flaskを使うのに必要なコード
app = Flask(__name__)
# APIを呼び出す
# response = requests.get("https://api.thecatapi.com/v1/images/search")
# 返ってきたデータ(文字)をそのまま表示
# jsonデータとしてロードして特定のデータのみ
# https://dog.ceo/api/breeds/image/random
# https://randomfox.ca/floof/
# ローカルホストで開いたときにindex.htmlを呼び出す

# セッション情報を暗号化するためのキー設定
app.secret_key = secrets.token_urlsafe(32)


@app.route("/")
def show_form():
    return render_template("index.html")


# catはページで開いたときに角括弧で囲われているので0が必要、他はそのまま呼び出せる。
@app.route("/post", methods=["POST"])
def post():
    if request.form["animal"] == "cat":
        res = requests.get("https://api.thecatapi.com/v1/images/search")
        outfile = json.loads(res.text)[0]["url"]
    elif request.form["animal"] == "dog":
        res = requests.get("https://dog.ceo/api/breeds/image/random")
        outfile = json.loads(res.text)["message"]
    else:
        res = requests.get("https://randomfox.ca/floof")
        outfile = json.loads(res.text)["image"]
    return render_template("upload.html", outfile=outfile)


# flaskを使うのに必要なコード、デバックトゥルーにするといちいち開き直さなくてよくなる。
if __name__ == "__main__":
    app.run(debug=True)
