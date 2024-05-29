// Jquery
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$('document').ready(function (){ 
  $.getJSON(url, function (response) {
  $('DIV#hello').text(response.hello);
  });
});
