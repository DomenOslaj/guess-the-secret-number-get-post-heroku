from flask import Flask, render_template, make_response, request
import random

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    secret_num = request.cookies.get("secret_num")    # check if secret num already exists in a cookie

    response = make_response(render_template("index.html"))

    if not secret_num:
        new_secret = str(random.randint(0, 29))
        response.set_cookie("secret_num", new_secret)

    return response


@app.route("/result", methods=["POST"])
def result():
    guess = int(request.form.get("guess"))
    secret_num = int(request.cookies.get("secret_num"))

    if guess > 30 or guess < 1:
        message = "Just numbers between 1 and 30!"
        return render_template("result.html", message=message)

    elif guess == secret_num:
        message = "Correct! Secret number is {0}!" .format(str(secret_num))
        response = make_response(render_template("result.html", message=message))
        response.set_cookie("secret_num", str(random.randint(0, 29)))
        return response

    elif guess > secret_num:
        message = "Not correct, try something smaller!"
        return render_template("result.html", message=message)

    elif guess < secret_num:
        message = "Not correct, try something bigger!"
        return render_template("result.html", message=message)


if __name__ == '__main__':
    app.run(debug=True)