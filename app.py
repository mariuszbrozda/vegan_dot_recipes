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
        
        return redirect(url_for('main_page'))
    return render_template("index.html")
    
    
@app.route("/main_page", methods=["GET", "POST"])
def main_page():
    
    return render_template("main_page.html" )


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)