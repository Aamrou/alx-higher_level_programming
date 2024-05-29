vascript - Web JQuery

## General
* Why jQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
* How to select HTML elements in Javascript
* How to select HTML elements with jQuery
* What are differences between ID, class and tag name selectors
* How to modify an HTML element style
* How to get and update an HTML element content
* How to modify the DOM
* How to make a GET request with jQuery Ajax
* How to make a POST request with jQuery Ajax
* How to listen/bind to DOM events
* How to listen/bind to user events

## 0. No jQuery
Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000):

* You must use document.querySelector to select the HTML tag
* You can’t use the jQuery API

Please test with this HTML file in your browser:

    guillaume@ubuntu:~/0x15$ cat 0-main.html 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Holberton School</title>
    </head>
    <body>
        <header> 
        First HTML page
        </header>
        <footer>
        Holberton School - 2017
        </footer>
        <script type="text/javascript" src="0-script.js"></script>
    </body>
    </html>
    guillaume@ubuntu:~/0x15$

## 1. With jQuery
Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000):

* You can’t use document.querySelector to select the HTML tag
* You must use the jQuery API

## 2. Click and turn red
Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header:

## 3. Add `.red` class
Javascript script that adds the class red to the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header:

## 4. Toggle classes
Javascript script that toggles the class of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#toggle_header:

* If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.

## 5. List of elements
Javascript script that adds a LI element to a list when the user clicks on the tag DIV#add_item

* The new element must be: <li>Item</li>
* The new element must be added to UL.my_list

## 6. Change the text
Javascript script that updates the text of the HTML tag HEADER to “New Header!!!” when the user clicks on DIV#update_header

## 7. Star wars character
Javascript script that fetches and replaces the name of this URL: `https://swapi-api.hbtn.io/api/people/5/?format=json`

## 8. Star Wars movies
Javascript script that fetches and lists all movies title by using this URL: `https://swapi-api.hbtn.io/api/films/?format=json`

* All movie titles must be list in the HTML tag UL#list_movies

## 9. Say Hello!
Javascript script that fetches from `https://fourtonfish.com/hellosalut/?lang=fr` and displays the value of hello from that fetch in the HTML’s tag DIV#hello.
