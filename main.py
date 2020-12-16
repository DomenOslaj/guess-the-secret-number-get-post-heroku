from flask import Flask, render_template, make_response, request
import random

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    secret_num = request.cookies.get("secret_num")    # check if secret num already exists in a cookie

    response = make_response(render_template("index.html"))  # response holds the cookie, server sends it to the users
                                                             # browser

    if not secret_num:
        new_secret = str(random.randint(0, 29))
        response.set_cookie("secret_num", new_secret)

    return response


if __name__ == '__main__':
    app.run(debug=True)