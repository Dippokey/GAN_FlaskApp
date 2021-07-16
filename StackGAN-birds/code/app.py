from flask import Flask, render_template, url_for, request, redirect
from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired 
import os




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
         caption = name
         caption_filename = "example_captions.txt"
         
         #put the file path here inside the comments
         caption_file = open("/content/drive/MyDrive/StackGAN-birds/data/birds/" + caption_filename, "w")

         caption_file.write(caption)
         caption_file.close()
         
         #Run StackGAN code
         os.system('clear')
         os.system('python3 main.py --cfg cfg/config_birds.yml --gpu 0')
         

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


if __name__ == "__main__":
    run_with_ngrok(app)
    app.run() 

