from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired 

#flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my super key is my power!"

#form class
class NamerForm(FlaskForm):
    name = StringField("Enter the description of the bird", validators=[DataRequired()])
    submit = SubmitField("submit")


#route url
@app.route('/', methods=['GET','POST'])
def index():
     name = None
     form = NamerForm()

     #validate form
     if form.validate_on_submit():
         name = form.name.data
         form.name.data = ''

     return render_template("index.html", name = name, form = form)
    


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

#error pages
@app.errorhandler(404)
def error1(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def error1(e):
    return render_template("500.html"), 500


