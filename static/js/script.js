var tweetLink = "https://twitter.com/intent/tweet?text=";
var facebookPost = 'http://www.facebook.com/share.php?u='
var recipeUrl = "";

function getQuote() {
  $.getJSON(quoteUrl, createTweet);
};
  
function createMessage(input) {
  var tweetText = ('Quote for today is : ' + input.quoteText +'Author : ' + input.quoteAuthor);
  var tweet = tweetLink + encodeURIComponent(tweetText);
  var 
  var fbPost = facebookPost + encodeURIComponent(tweetText);
  if (!input.quoteAuthor.length) {
    input.quoteAuthor = "Unknown author";
  }
  if (tweetText.length > 140) {
    getQuote();
  }
  else {
    $('.quote').text(input.quoteText);
    $('.author').text("Author: " +  input.quoteAuthor);
    $('.tweet').attr('href', tweet);
  }
  $('.tweet').attr('href', tweet);
};

$(document).ready(function() {
  getQuote();
  $('.trigger').click(function() {
    getQuote();
  })
  
});

