from flask import Flask, render_template, request, flash
from models import newRecipe
from . import db

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        recipeList = "winter_x64"
        return render_template("homepage.html", recipeList = recipeList)

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        header = request.form.get('header')
        Recipe = request.form.get('recipe')

        if len(Recipe) < 1:
            flash('Recipe is too short!', category='error')
        elif len(header) < 1:
            flash('title is too short!', category='error')
        else:
            new_Recipe = newRecipe(header= header, data=Recipe)
            db.session.add(new_Recipe)
            db.session.commit()
            flash('Recipe added!', category='success')

    return render_template("upload.html")


app.run(debug=True)