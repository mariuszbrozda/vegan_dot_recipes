import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Vegan_Dot_DB'
app.config['MONGO_URI'] = "mongodb+srv://root:Machiaveli6@myfirstcluster-wdhib.mongodb.net/Vegan_Dot_DB?retryWrites=true"


mongo = PyMongo(app)


@app.route("/")
@app.route("/log_in")
def log_in():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)