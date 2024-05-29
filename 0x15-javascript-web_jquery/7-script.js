// Jquery
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.getJSON(url, function (response) {
  $('DIV#character').text(response.name);
});
