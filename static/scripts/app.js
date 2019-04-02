console.log("Javascript is working!")
$(document).ready(function(e){
    $.ajax({
        method: 'GET',
        url: `https://www.googleapis.com/content/v2/133499847/products`,
        success: function (response) {
            console.log(response)
        },
        error: function(error) {
        console.log(error);
        }
    });

    $.ajax({
        method: 'GET',
        url: `https://skincare-api.herokuapp.com/products/74`,
        success: function (response) {
            console.log(typeof response)
        },
        error: function(error) {
        console.log(error);
        }
    });
//returns first 25 skincare products with rose ingredient
    $.ajax({
        method: 'GET',
        url: `https://skincare-api.herokuapp.com/ingredient?q=rose&limit=25&page=1`,
        success: function (response) {
            console.log(typeof JSON.parse(response))
            console.log(response)
        },
        error: function(error) {
        console.log(error);
        }
    });

    
});
