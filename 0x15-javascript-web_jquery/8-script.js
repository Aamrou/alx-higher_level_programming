// Jquery
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.getJSON(url, function (response) {
  $.each(response.results, function (i, item) {
    $('UL#list_movies').append('<li>' + item.title + '</li>');
  });
});
