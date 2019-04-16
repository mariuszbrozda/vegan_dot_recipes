import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.secret_key = os.urandom(22)
app.config["MONGO_DBNAME"] = 'Vegan_Dot_DB'
app.config['MONGO_URI'] = "mongodb+srv://root:Machiaveli6@myfirstcluster-wdhib.mongodb.net/Vegan_Dot_DB?retryWrites=true"


mongo = PyMongo(app)


@app.route("/", methods=["GET", "POST"])
@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        session['username'] = request.form['username']
        return redirect(url_for('main_page'))
    return render_template("log_in.html")
    
    
@app.route("/main_page", methods=["GET", "POST"])
def main_page():
    username = session.get('username')
    return render_template("main_page.html", user=username )
    

@app.route("/my_recipes", methods=["GET", "POST"])
def my_recipes():
    username = session.get('username')
    return render_template("my_recipes.html", user=username )


## ------------------NAV TABS ROUTES -----

@app.route("/starters", methods=["GET", "POST"])
def starters():
    username = session.get('username')
    return render_template("starters.html", user=username )
    
    
@app.route("/main_courses", methods=["GET", "POST"])
def main_courses():
    username = session.get('username')
    return render_template("main_courses.html", user=username )
    
    
@app.route("/desers", methods=["GET", "POST"])
def desers():
    username = session.get('username')
    return render_template("desers.html", user=username )
    
    
@app.route("/smoothies", methods=["GET", "POST"])
def smoothies():
    username = session.get('username')
    return render_template("smoothies.html", user=username )
    
    
@app.route("/juices", methods=["GET", "POST"])
def juices():
    username = session.get('username')
    return render_template("juices.html", user=username )
    
    

## ------------------CRUD OPERATIONS -----

@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    username = session.get('username')
    return render_template("add_recipe.html", user=username )


@app.route('/edit_recipe/')
def edit_recipe():
    
    return render_template('edit_recipe.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)