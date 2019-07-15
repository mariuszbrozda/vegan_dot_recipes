import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
from wtforms import Form, BooleanField, StringField, PasswordField, validators

app = Flask(__name__)
app.secret_key = os.urandom(22)
app.config["MONGO_DBNAME"] = 'Vegan_Dot_DB'
app.config['MONGO_URI'] = "mongodb+srv://root:Latino1@myfirstcluster-wdhib.mongodb.net/Vegan_Dot_DB?retryWrites=true"



mongo = PyMongo(app)


## -------------------------------------------------LOIN PAGE ROUTE ----- 




@app.route("/", methods=["GET", "POST"])
@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('main_page'))
    return render_template("log_in.html")


 
## -------------------------------------------------MAIN PAGE ROUTE -----   
    
@app.route("/main_page/", methods=["GET", "POST"])
def main_page():
    username = session.get('username')
    recipes = mongo.db.recipes.find()
    return render_template("main_page.html", user=username, recipes=recipes)


## ------------------NAV TABS ROUTES -----

@app.route("/starters", methods=["GET", "POST"])
def starters():
    username = session.get('username')
    starters_recipes = mongo.db.recipes.find({"recipe_category_name": "Starters"})
    return render_template("starters.html", user=username, starters_recipes=starters_recipes )
    
    
@app.route("/main_courses", methods=["GET", "POST"])
def main_courses():
    username = session.get('username')
    main_courses_recipes = mongo.db.recipes.find({"recipe_category_name": "Main courses"})
    return render_template("main_courses.html", user=username,
                            main_courses_recipes = main_courses_recipes )
    
    
@app.route("/desers", methods=["GET", "POST"])
def desers():
    username = session.get('username')
    desers_recipes = mongo.db.recipes.find({"recipe_category_name": "Desers"})
    return render_template("desers.html", user=username,
                           desers_recipes = desers_recipes )
    
    
@app.route("/smoothies", methods=["GET", "POST"])
def smoothies():
    username = session.get('username')
    smoothies_recipes = mongo.db.recipes.find({"recipe_category_name": "Smoothies"})
    return render_template("smoothies.html", user=username,
                            smoothies_recipes = smoothies_recipes)
    
    
@app.route("/juices", methods=["GET", "POST"])
def juices():
    username = session.get('username')
    juices_recipes = mongo.db.recipes.find({"recipe_category_name": "Juices"})
    return render_template("juices.html", user=username,
                            juices_recipes = juices_recipes )
    
## ----------------------------------------------MY RECIPES ROUTE -----     


@app.route("/my_recipes", methods=["GET", "POST"])
def my_recipes():
    username = session.get('username')
    recipes_uploaded_by_me = mongo.db.recipes.find({})
    return render_template("my_recipes.html", user=username, recipes_uploaded_by_me=recipes_uploaded_by_me)


## ----------------------------------------------RECIPE ROUTE ----- 


@app.route("/recipe/<recipe_id>",methods=["GET", "POST"])
def recipe(recipe_id):
    recipes =  mongo.db.recipes
    recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    username = session.get('username')
    return render_template("recipe.html", user=username, recipe = recipe)
    
    
    
## ------------------CRUD OPERATIONS -----


## ----------------------------------------------ADD RECIPE ROUTE ----- 

@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    recipes =  mongo.db.recipes
    username = session.get('username')
    return render_template("add_recipe.html", user=username,
                        recipes_categories=mongo.db.recipes_categories.find())
                        



    
## ----------------------------------------------INSERT RECIPE ROUTE -----  
    
@app.route('/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():
    
    recipes =  mongo.db.recipes
    
    form_data = request.form.copy()
    index = 0
    ingredients= []
    nutrition_info= []
    alergens= []
    
   
    for input_field in request.form:
        if input_field[:-1] == "ingredient":
            ingredients.append(form_data[input_field])
            del form_data[input_field]
        if input_field[:-1] == "nutrition":
                nutrition_info.append(form_data[input_field])
                del form_data[input_field]
        if input_field[:-1] == "alergen":
                alergens.append(input_field)
                del form_data[input_field]
        
        
        if len(ingredients) > 0:
            form_data["ingredients"] = ingredients
        if len(nutrition_info) > 0:
            form_data["nutrition_info"] = nutrition_info
        if len(alergens) > 0:
            form_data["alergens"] = alergens
        
    recipe_dict = recipes.insert_one(
        {
        'recipe_name':request.form.get('recipe_name'),
        'recipe_category_name':request.form.get('recipe_category_name'),
        'recipe_description': request.form.get('recipe_description'),
        'cousine': request.form.get('cousine'),
        'uploaded_by': request.form.get('uploaded_by') ,
        'recipe_picture_url': request.form.get('recipe_picture_url'),
        'preparation_time': request.form.get('preparation_time'),
        'recipe_how_to_serve': request.form.get('recipe_how_to_serve'),
        'preparation':request.form.get('preparation'),
        'ingredients': ingredients,
        'nutrition_info':nutrition_info,
        'alergens': alergens
        }
    )
    return redirect(url_for('main_page' ))



## ----------------------------------------------EDIT ROUTE -----

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.recipes_categories.find()
    return render_template('edit_recipe.html', recipe = recipe,
                           recipes_categories=all_categories)    
                           





@app.route('/update_recipe/<recipe_id>', methods=["GET", "POST"])
def update_recipe(recipe_id):
    
    recipes =  mongo.db.recipes
        
    form_data = request.form.copy()
    index = 0
    ingredients= []
    nutrition_info= []
    alergens= []
    
   
    for input_field in request.form:
        if input_field[:-1] == "ingredient":
            ingredients.append(form_data[input_field])
            del form_data[input_field]
        if input_field[:-1] == "nutrition":
                nutrition_info.append(form_data[input_field])
                del form_data[input_field]
        if input_field[:-1] == "alergen":
                alergens.append(input_field)
                del form_data[input_field]
        
        
        if len(ingredients) > 0:
            form_data["ingredients"] = ingredients
        if len(nutrition_info) > 0:
            form_data["nutrition_info"] = nutrition_info
        if len(alergens) > 0:
            form_data["alergens"] = alergens
    
    
   
    
      
    recipe_dict = recipes.update(
        {"_id": ObjectId(recipe_id)},
        {
        
        'recipe_name':request.form.get('recipe_name'),
        'recipe_category_name':request.form.get('recipe_category_name'),
        'recipe_description': request.form.get('recipe_description'),
        'cousine': request.form.get('cousine'),
        'uploaded_by': request.form.get('uploaded_by') ,
        'recipe_picture_url': request.form.get('recipe_picture_url'),
        'preparation_time': request.form.get('preparation_time'),
        'recipe_how_to_serve': request.form.get('recipe_how_to_serve'),
        'preparation':request.form.get('preparation'),
        'ingredients': ingredients,
        'nutrition_info': nutrition_info,
        'alergens': alergens
        }
        
    )
    
    
    
    return redirect(url_for('my_recipes'))

@app.route('/delete_recipe/<recipe_id>', methods=["POST"])
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('my_recipes'))
    




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)