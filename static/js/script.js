

var j = 0;

function addIngrediens() {
    
    var j = 0;
    j++
    
    var ingredients = $("#ingredients").find(".form-control").length + 1;
    $("#ingredients").append("<input id='ingredient" + ingredients
    + "' name='ingredient" + ingredients
    + "' type='text' class='addedInput form-control'>");
 }

function removeIngrediens() {
    var ingredient_name = document.getElementById('ingredients');
    ingredient_name.removeChild(ingredient_name.lastChild);
    
}



function addNutritionInfo() {
    var j = 0;
    j++
    var nutrition_info = $("#nutrition_info").find(".form-control").length + 1;
    $("#nutrition_info").append("<div class='addedInputGroup'><label class='stepLabel' for='nutrition" + nutrition_info + "'>nutrition" 
    + nutrition_info + "</label><input id='nutrition" + nutrition_info
    + "' name='nutrition" + nutrition_info
    + "' type='text' class='addedInput form-control'>");
    
}

function removeNutritionInfo() {
    var nutrition_name = document.getElementById('nutrition_info');
    nutrition_name.removeChild(nutrition_name.lastChild);
}


function addAlergens() {
    var j = 0;
    j++
    var alergens = $("#alergens").find(".form-control").length + 1;
    $("#alergens").append("<div class='addedInputGroup'><label class='stepLabel' for='alergen" + alergens + "'>alergen" 
    + alergens + "</label><input id='alergen" + alergens
    + "' name='alergen" + alergens
    + "' type='text' class='addedInput form-control'>");
}

function removeAlergens() {
    var remove = document.getElementById('alergens');
    remove.removeChild(remove.lastChild);
    
}







