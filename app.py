import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 


app = Flask(__name__)
app.secret_key = os.urandom(22)
app.config["MONGO_DBNAME"] = os.getenv('MONGO_DBNAME')
app.config['MONGO_URI'] = os.getenv("MONGO_URI")

mongo = PyMongo(app)


## -------------------------------------------------LOIN PAGE ROUTE ----- 


@app.route("/", methods=["GET", "POST"])
@app.route("/log_in", methods=["GET", "POST"])

# Function for login that after post request,
# creates username var in session and redirect to 'main page'
def log_in():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('main_page'))
    return render_template("log_in.html")


 
## -------------------------------------------------MAIN PAGE ROUTE -----   
    
@app.route("/main_page/", methods=["GET", "POST"])

# Function for 'main page' that gets username var from session
# and finds all recipes in MongoDB recipes collection
def main_page():
    username = session.get('username')
    recipes = mongo.db.recipes.find()
    return render_template("main_page.html", user=username, recipes=recipes)


## ------------------STARTER ROUTES -----

@app.route("/starters", methods=["GET", "POST"])

# Function for 'STARTERS' that gets username var from session
# and finds all STARTERS recipes in MongoDB recipes collection
def starters():
    username = session.get('username')
    starters_recipes = mongo.db.recipes.find({"recipe_category_name": "Starters"})
    return render_template("starters.html", user=username, starters_recipes=starters_recipes )
    
    
## ------------------MAIN COURSE ROUTES -----    
@app.route("/main_courses", methods=["GET", "POST"])

# Function for 'Main courses' that gets username var from session
# and finds all Main courses recipes in MongoDB recipes collection
def main_courses():
    username = session.get('username')
    main_courses_recipes = mongo.db.recipes.find({"recipe_category_name": "Main courses"})
    return render_template("main_courses.html", user=username,
                            main_courses_recipes = main_courses_recipes )
    

## ------------------DESERS ROUTES -----    
@app.route("/desers", methods=["GET", "POST"])

# Function for 'Desers' that gets username var from session
# and finds all Desers recipes in MongoDB recipes collection
def desers():
    username = session.get('username')
    desers_recipes = mongo.db.recipes.find({"recipe_category_name": "Desers"})
    return render_template("desers.html", user=username,
                           desers_recipes = desers_recipes )
    
    
## ------------------SMOOTHIES ROUTES -----
@app.route("/smoothies", methods=["GET", "POST"])

# Function for 'Smoothies' that gets username var from session
# and finds all Smoothies recipes in MongoDB recipes collection
def smoothies():
    username = session.get('username')
    smoothies_recipes = mongo.db.recipes.find({"recipe_category_name": "Smoothies"})
    return render_template("smoothies.html", user=username,
                            smoothies_recipes = smoothies_recipes)
    

## ------------------JUICES ROUTES -----   
@app.route("/juices", methods=["GET", "POST"])

# Function for 'Juices' that gets username var from session
# and finds all Juices recipes in MongoDB recipes collection
def juices():
    username = session.get('username')
    juices_recipes = mongo.db.recipes.find({"recipe_category_name": "Juices"})
    return render_template("juices.html", user=username,
                            juices_recipes = juices_recipes )
  
  
    
## ----------------------------------------------MY RECIPES ROUTE -----     
@app.route("/my_recipes", methods=["GET", "POST"])

# Function for 'my recipes' that gets username var from session
# and finds all recipes uploaded by user in MongoDB recipes collection
def my_recipes():
    username = session.get('username')
    recipes_uploaded_by_me = mongo.db.recipes.find({})
    return render_template("my_recipes.html", user=username, recipes_uploaded_by_me=recipes_uploaded_by_me)


## ----------------------------------------------RECIPE ROUTE ----- 
@app.route("/recipe/<recipe_id>",methods=["GET", "POST"])

# Function for recipe that gets username var from session
# and finds particular recipe by ID 
def recipe(recipe_id):
    recipes =  mongo.db.recipes
    recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    username = session.get('username')
    return render_template("recipe.html", user=username, recipe = recipe)
    
    
    
## ------------------CRUD OPERATIONS -----


## ----------------------------------------------ADD RECIPE ROUTE ----- 
@app.route("/add_recipe", methods=["GET", "POST"])

# Function for adding recipe that gets username var from session
# and finds all recipe's categories and return add_recipe page
def add_recipe():
    recipes =  mongo.db.recipes
    username = session.get('username')
    return render_template("add_recipe.html", user=username,
                        recipes_categories=mongo.db.recipes_categories.find())
                        



    
## ----------------------------------------------INSERT RECIPE ROUTE -----  
@app.route('/insert_recipe', methods=['GET', 'POST'])

# Function for inserting recipe(document) to recipe collection.
def insert_recipe():
    
    recipes =  mongo.db.recipes
    
    form_data = request.form.copy()
    index = 0
    ingredients= []
    nutrition_info= []
    alergens= []
    
  # FOR loop that appends ingredient, nutrition, alergen from inputs to particular arrays
    for input_field in request.form:
        
# if statements that check if input value is ingredient, nutrition or alergen
        if input_field[:-1] == "ingredient":
            ingredients.append(form_data[input_field])
            del form_data[input_field]
        if input_field[:-1] == "nutrition":
                nutrition_info.append(form_data[input_field])
                del form_data[input_field]
        if input_field[:-1] == "alergen":
                alergens.append(input_field)
                del form_data[input_field]
        
# if statements that check if there are more elements than 0 in  arrays : ingredient, nutrition or alergen    
        if len(ingredients) > 0:
            form_data["ingredients"] = ingredients
        if len(nutrition_info) > 0:
            form_data["nutrition_info"] = nutrition_info
        if len(alergens) > 0:
            form_data["alergens"] = alergens
            

# Taking values of recipe elements from form and inserting them to recipe collection as a document

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
        'ingredients': {
            'ingredient1': request.form.get('ingredient1'),
            'ingredient1_ammount': request.form.get('ingredient1_ammount'),
            'ingredient2': request.form.get('ingredient2'),
            'ingredient2_ammount': request.form.get('ingredient2_ammount'),
            'ingredient3': request.form.get('ingredient3'),
            'ingredient3_ammount': request.form.get('ingredient3_ammount'),
            'ingredient4': request.form.get('ingredient4'),
            'ingredient4_ammount': request.form.get('ingredient4_ammount'),
            'ingredient5': request.form.get('ingredient5'),
            'ingredient5_ammount': request.form.get('ingredient5_ammount'),
            'ingredient6': request.form.get('ingredient6'),
            'ingredient6_ammount': request.form.get('ingredient6_ammount'),
            'ingredient7': request.form.get('ingredient7'),
            'ingredient7_ammount': request.form.get('ingredient7_ammount'),
            'ingredient8': request.form.get('ingredient8'),
            'ingredient8_ammount': request.form.get('ingredient8_ammount'),
            'ingredient9': request.form.get('ingredient9'),
            'ingredient9_ammount': request.form.get('ingredient9_ammount'),
            'ingredient10': request.form.get('ingredient10'),
            'ingredient10_ammount': request.form.get('ingredient10_ammount'),
            },
            
        'nutrition_info': {
            'nutrition1': request.form.get('nutrition1'),
            'nutrition1_ammount': request.form.get('nutrition1_ammount'),
            'nutrition2': request.form.get('nutrition2'),
            'nutrition2_ammount': request.form.get('nutrition2_ammount'),
            'nutrition3': request.form.get('nutrition3'),
            'nutrition3_ammount': request.form.get('nutrition3_ammount'),
            'nutrition4': request.form.get('nutrition4'),
            'nutrition4_ammount': request.form.get('nutrition4_ammount'),
            'nutrition5': request.form.get('nutrition5'),
            'nutrition5_ammount': request.form.get('nutrition5_ammount'),
            'nutrition6': request.form.get('nutrition6'),
            'nutrition6_ammount': request.form.get('nutrition6_ammount'),
            'nutrition7': request.form.get('nutrition7'),
            'nutrition7_ammount': request.form.get('nutrition7_ammount'),
            'nutrition8': request.form.get('nutrition8'),
            'nutrition8_ammount': request.form.get('nutrition8_ammount'),
            'nutrition9': request.form.get('nutrition9'),
            'nutrition9_ammount': request.form.get('nutrition9_ammount'),
            'nutrition10': request.form.get('nutrition10'),
            'nutrition10_ammount': request.form.get('nutrition10_ammount'),
            
            },
            
        'alergens': {
            'alergen1': request.form.get('alergen1'),
            'alergen2': request.form.get('alergen2'),
            'alergen3': request.form.get('alergen3'),
            'alergen4': request.form.get('alergen4'),
            'alergen5': request.form.get('alergen5'),
            'alergen6': request.form.get('alergen6'),
            'alergen7': request.form.get('alergen7'),
            'alergen8': request.form.get('alergen7'),
            'alergen9': request.form.get('alergen9'),
            'alergen10': request.form.get('alergen10'),
            },
        
        }
    )
    return redirect(url_for('main_page' ))



## ----------------------------------------------EDIT/ ROUTE -----

@app.route('/edit_recipe/<recipe_id>')

# Function for edit recipe.
#Finds recipe by it's ID and return edit_recipe page
def edit_recipe(recipe_id):
    recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.recipes_categories.find()
    return render_template('edit_recipe.html', recipe = recipe,
                           recipes_categories=all_categories)    
                           


## ------------------UPDATE ROUTES -----


@app.route('/update_recipe/<recipe_id>', methods=["GET", "POST"])

# Function for update recipe.
def update_recipe(recipe_id):
    
    recipes =  mongo.db.recipes
    form_data = request.form.copy()
    ingredients= []
    nutrition_info= []
    alergens= []
 
# Taking values of recipe elements from edit form and updating them in existing recipe document

    recipe_dict = recipes.update(
        {"_id": ObjectId(recipe_id)},
        {"$set":
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
            'ingredients': {
                'ingredient1': request.form.get('ingredient1'),
                'ingredient1_ammount': request.form.get('ingredient1_ammount'),
                'ingredient2': request.form.get('ingredient2'),
                'ingredient2_ammount': request.form.get('ingredient2_ammount'),
                'ingredient3': request.form.get('ingredient3'),
                'ingredient3_ammount': request.form.get('ingredient3_ammount'),
                'ingredient4': request.form.get('ingredient4'),
                'ingredient4_ammount': request.form.get('ingredient4_ammount'),
                'ingredient5': request.form.get('ingredient5'),
                'ingredient5_ammount': request.form.get('ingredient5_ammount'),
                'ingredient6': request.form.get('ingredient6'),
                'ingredient6_ammount': request.form.get('ingredient6_ammount'),
                'ingredient7': request.form.get('ingredient7'),
                'ingredient7_ammount': request.form.get('ingredient7_ammount'),
                'ingredient8': request.form.get('ingredient8'),
                'ingredient8_ammount': request.form.get('ingredient8_ammount'),
                'ingredient9': request.form.get('ingredient9'),
                'ingredient9_ammount': request.form.get('ingredient9_ammount'),
                'ingredient10': request.form.get('ingredient10'),
                'ingredient10_ammount': request.form.get('ingredient10_ammount'),
                
                },
            'nutrition_info': {
            'nutrition1': request.form.get('nutrition1'),
            'nutrition1_ammount': request.form.get('nutrition1_ammount'),
            'nutrition2': request.form.get('nutrition2'),
            'nutrition2_ammount': request.form.get('nutrition2_ammount'),
            'nutrition3': request.form.get('nutrition3'),
            'nutrition3_ammount': request.form.get('nutrition3_ammount'),
            'nutrition4': request.form.get('nutrition4'),
            'nutrition4_ammount': request.form.get('nutrition4_ammount'),
            'nutrition5': request.form.get('nutrition5'),
            'nutrition5_ammount': request.form.get('nutrition5_ammount'),
            'nutrition6': request.form.get('nutrition6'),
            'nutrition6_ammount': request.form.get('nutrition6_ammount'),
            'nutrition7': request.form.get('nutrition7'),
            'nutrition7_ammount': request.form.get('nutrition7_ammount'),
            'nutrition8': request.form.get('nutrition8'),
            'nutrition8_ammount': request.form.get('nutrition8_ammount'),
            'nutrition9': request.form.get('nutrition9'),
            'nutrition9_ammount': request.form.get('nutrition9_ammount'),
            'nutrition10': request.form.get('nutrition10'),
            'nutrition10_ammount': request.form.get('nutrition10_ammount'),
            
            },
        'alergens': {
            'alergen1': request.form.get('alergen1'),
            'alergen2': request.form.get('alergen2'),
            'alergen3': request.form.get('alergen3'),
            'alergen4': request.form.get('alergen4'),
            'alergen5': request.form.get('alergen5'),
            'alergen6': request.form.get('alergen6'),
            'alergen7': request.form.get('alergen7'),
            'alergen8': request.form.get('alergen7'),
            'alergen9': request.form.get('alergen9'),
            'alergen10': request.form.get('alergen10'),
            },
            
            }
        }
    )
    return redirect(url_for('my_recipes'))


## ------------------DELETE ROUTES -----
@app.route('/delete_recipe/<recipe_id>', methods=["POST"])

# Function for delete recipe with particular ID.
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('my_recipes'))
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)