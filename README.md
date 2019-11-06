
Vegan Dot Recipes:

This project is a data-driven online cook book with vegan recipes. 
Website logic is mainly written in Python(Flask framework),HTML,CSS.
MongoDB was used to store data. In the project were used CRUD operations to Create,Read,Update and delete recipes.
Website purpose is to share information about vegan recipes in one place.


UX DESIGN


MOCKUP LINK https://app.moqups.com/Vau7X8SpAb/view/page/aa9df7b72

The project was created for consumers who are looking for the ideas for vegan recipes.
My plan was to create website, in which users could easily find vegan recipes, share their own vegan recipes and also keep in one place all their favorite ones.
I believe that it will make users want to come back to my website again and again.

Project design was inspared by 'Blueapron' recipes website (https://www.blueapron.com/pages/sample-recipes).
On it's main page, recipes are presented as a cards with clear description and meal image. 
It will help to create positive user experience and encourage users to interact with the website.

On main page we can also find clear navigation with particular tabs. It will help users easily navigate the page, for example: search, upload and edit recipes and also log out.
There are tabs leading to particular meals such us starters, main courses, desers, smoothies or juices. It helps users to find recipe fast and easy from one category to another.

There is a 'home page' tab which quickly redirect users to main page where are all recipes.

Tab named 'Upload recipe' leads users to the page where they can add their own recipes to the website.

There is also 'log out' tab and users can use it to log out from website anytime and from any page.

'My recipes' tab leads users to recipes they uploaded before. They can remove or edit recipe from there.

The navigation is usefull and simple for user. It makes a user-friendy page and easy to searching through website content.


USER'S STORIES :

As a vegan person I want to find information about vegan recipes so that I can cook my vegan food at home
 -After log in user can search recipes and also share his/her own meals ideas with others.

As person with intolerance and allergy for some products, I want to make sure that meals I find don't contain harmful for me allergens.
 -Each recipe has list of allergens so users can check what type of allergens are in the meal.

As a person on diet I want to find information about nutrition facts so I can keep ballance in my diet.
 -All recipes have nutrition info table in which users can check all nutrition facts. For example ammount of proteins in meal.
 

FEATURES 

Meals category tabs feature - 
Website has a seperate tabs for each meal category which is very helpfull for searching recipes. 
By clicking tab name, user can find recipes from particular category.
For example tab 'Desers' will return only desers meals.
After user clicks name of category tab, find() function is executed and all recipes from that category are returned (based on query filter).


Add recipe feature(Create) - 
By filling out a form in upload recipe template, user can add a recipe to the database and the website using MongoDB insert-one() function(by clicking 'upload recipe' button). 


Find Recipe feature(Read) - 
When user clicks 'view' button to see recipe, find() function is executed to find requested recipe. To locate particular recipe MongoDB uses object ID. 
User is redirected to the recipe's page where information from the database is presented in a readable format to the user.


Edit recipe feature(Update) - 
In 'my recipes' tab, user can find each uploaded recipes. By clicking edit button in particular recipe card, user can edit recipes uploaded on the website before.
It will redirect him/her to edit form on which updates can be done. After making changes and click 'update recipe' button, update() function is executed and changes are updated in Mongo database collection. 
To find particular recipe and its entry MongoDB uses objectid.


Delete Recipe(Delete) feature - 
Each recipe can be deleted in 'My recipes' tab, by clickinghas a 'Delete Recipe' button found at the bottom of the page. Once clicked it uses the remove() mongoDB method.


My recipes feature - 
Each recipe uploaded by user can be managed in 'My recipes' tab. User can view, edit or delete recipe from website and MongoDB collection. 


Log in/Log out feature - 
User is able to login and log out to the website and full authentication is added.


FEATURES LEFT TO IMPLEMENT

Social media sharing feature
Let user post and share recipes on social media

Add to favorites feature
User will be able to add recipes to favorites and then manage them in 'My recipes' tab. By clicking 'add to favorites' button.

User profile account feature
User will be able to log in to his/her account to use full content of website, keep and manage recipes.
After clicking on user name tab User will be redirected to his/her profile.


TECHNOLOGIES USED

Python - To create backend and add functionalities to project. LINK https://www.python.org/

HTML - To create basic structure of the project LINK ( https://www.w3schools.com/html/ )

CSS - To add styles to the project. Also some part of responsiveness was done by css styles by adding media queries.

Bootstrap framework - To create responsive layout and add some design and components by add helpfull classes. LINK: https://getbootstrap.com/

Flask framework - To create backend and add functionalities to the project. Flask helps backend and front en work together as a whole LINK: http://flask.pocoo.org/

Google Fonts - To add some fonts.

Materialize framework  - To create responsive layout and add some design and components LINK ( https://materializecss.com/ )


TESTING


Application was tested manually by pretending to be a user.

Testing log in / log out functionality - Expected that user is redirected from log in page to home page, after fill out and submit a log in form.
Expecting that user name typed in login form is presented on main page after log in.


Testing add recipe functionality - Making sure that when click on 'upload recipe' tab, user is redirected to add_recipe page.
Expected that after fill out and submit add recipe form, all data is presented on recipe's page as planned. Also cancel button on add_recpe page was tested, by clicking and checking if user is redirected to previous page.


Testing Meals category tabs functionality - Expected that after clicking tab with particular category name, user will be redirected to that page.
Check if only recipes from that category are found and presented.


Testing 'view' button functionality - Check if after click 'view' button, user is redirected to recipe's page 


Testing edit recipe functionality - Go to 'My recipes' and click edit button on recipe to update. Check if user is redirected to 'edit_recipe' page(edit form) and if correct data from database is presented in the form.
Check if data is correctly updated to database after refill edit form and if it is presented on recipe's page with no issues.


Testing delete recipe functionality - Check if recipe is deleted from database and also website after clicing 'delete' (red button wit 'X' sign) button.
Make sure if deleting correct recipe.


Testing my recipes tab(recipes managing) functionality - Testing if user is redirected to 'My recipes' page after clicing 'My recipes' tab. 
Expected to see all uploaded by user recipes with view, deleteand edit buttons(possibility).


Testing home page tab functionality - Testing if user is redirected to 'home page' after clicking 'home' tab. By clicking 'home' from any website locations.

Project was based on Graceful degradation approach which means that desktop version was created as first then responsiveness was added for mobile and tablets. 
Media query and bootstrap responsive classes were used to achieve that. Projects responsiveness was tested by google developer tools where it was resising to particular device size(for example iphones,samsung ) 
It was tested also by changing size of browser window. Application was tested after each functionality was added to it.


DATABASE SCHEMA

The database is structured with two collections, recipes and recipes_categories. 
The two collections are related as recipes contains a 'recipe_category_name' key that corresponds the recipes_categories documents.
The recipes document contains unstuctured data. With key/value pairs that relating to each description of the recipe. 
Nutrition table, alergens table and ingredients table are stored as an seperate arrays in recipes document.
An example of a recipe document can be found in /static/img/recipes_schema_example.png
A recipes categories schema document can be found in /static/img/recipes_categories_schema.png

DEPLOYMENT

The project was deployed on Heroku platform under link : https://vegan-dot-recipes.herokuapp.com/

COMMANDS USED TO DEPLOY PROJECT TO HEROKU:

git init (create empty repository)
git add ( to add files)
git commit -m'' (to commit changes and add message)
heroku login (To log in to heroku platform)
heroku ps:scale web=1 (to run app on heroku)
git push heroku master ( to push local repository to heroku)

The project was deployed to Heroku with config vars:

IP = 0.0.0.0
PORT = 5000

The development and deployed versions are the same.

CREDITS

Code for appends ingredient, nutrition, alergen from inputs to particular arrays and
check if there are more elements than 0 in  arrays : ingredient, nutrition or alergen was taken from : https://github.com/Code-Institute-Submissions/cookbook-7/blob/master/app.py
and changed and adopted to my project.

Logo was taken from instagram profile https://www.instagram.com/vegan_dot/?hl=en My project will be linked to it in future.




