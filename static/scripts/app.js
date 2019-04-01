console.log("Javascript is working!")

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