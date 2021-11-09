from flask.helpers import flash
from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.email import Register




@app.route('/')
def survey():
    return render_template("index.html")


@app.route('/resultspage')
def resultsPage():
    return render_template("emailpage.html",result = Register.get_email())


@app.route("/results", methods=["POST"])
def results():
    if Register.validate_email(request.form):
        data = {
            "email":request.form["email"]
        }
        Register.saveemail(data)
        return redirect('/resultspage')
    return redirect("/")