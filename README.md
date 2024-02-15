# Scoreboard
Displays runtime percentage of manufacturing factory's machines in the last hour and flash red if they stop.
<hr>

- ### HTML: Template filea
[Main source code](https://github.com/serjikssg/scoreboard/blob/main/scoreboard/templates/scoreboard/scoreboard.html)

[Tag_change source code](https://github.com/serjikssg/scoreboard/blob/main/scoreboard/templates/scoreboard/tag_change.html)
<hr>

- ### Python: Function in views.py to get and clean the data from the Guidewheel API, and populate the HTML file with machine cards. 
[source code](https://github.com/serjikssg/scoreboard/blob/main/scoreboard/views.py)
<hr>

- ### Database: models.py tables for machines and tags. 
[source code](https://github.com/serjikssg/Scoreboard/blob/main/scoreboard/models.py)
<hr>

- ### JavaScript: Function to make machine cards flash
[source code](https://github.com/serjikssg/scoreboard/blob/main/scoreboard/static/scoreboard/js/scoreboard.js)
<hr>

- ### CSS: Style for the machine cards flashing
[source code](https://github.com/serjikssg/scoreboard/blob/main/scoreboard/static/scoreboard/css/style.css)
<hr>

- ### urls.py: To link the scoreboard app to a Django project
[source code](https://github.com/serjikssg/scoreboard/blob/main/scoreboard/urls.py)
<hr>

- ### admin.py: Addning the data model on admin backend page
[source code](https://github.com/serjikssg/scoreboard/blob/main/scoreboard/admin.py)
<hr>

#### Next plan: To create a mobile app to do same. (react native) 
