# GrandPyBot

This conversational bot will give you description of a location, the address and a map to go there from an question or
from coordinates share by the user. 
This is a test driven project. 

## How to run 
Create an environment then install the same requirements then in requirements.txt. 
Go at the same directory level then run.py. 
In your bash launch the command "python run.py". 
Open the localhost in your favorite navigator. 

## Back End functionalities

### Parse, mother class for other parer
#### => Class Parser
This class parse message from front input from user and return it to API.
This class do it in tree step: 
* Step 1, format the message: lower the message, remove comma and dot and quotes, and put all word in a list. 
* Step 2, removed the verb from the list: two imbricate loop create verb prefix and verb termination from lists and
removed created verb from the list from step 1. 
* Step 3, with list from step 2, a stop word list is use for removed stop word. 
The results is a list of key word. 

### Parser for Google Map and com with API 
#### => Class TheGoogleMapParseCom
Parser for Google Map with Python back end. 
Speak with Google Map API with Python back end and Json message.
Inherit from Parse class: Parse message from front with the aim to do a list of key words use to interrogate the Google Map API. 
Obtain coordinates from Wiki Media. 
Transform this coordinates in string. 
Interrogate Google map API with this strong coordinates to obtain a static png map. 

### Parser for Media Wiki and com with API 
#### => Class TheWikiMediaParseCom 
Parser for Media Wiki with Python back end.
Speak with Media Wiki API with Python back end and Json message.
Inherit from Parse class: Parse message from front with the aim to do a list of key words use to interrogate the Media Wiki API. 
With a list of key word interrogate Wiki Media API to obtain a title corresponding to this key words. 


### Randomly sentence send
#### => Class TheRandomMessage
Engine to randomly send sentence from back end.

### Give Coordinates from titles  
#### => Class Coordinates
Obtain coordinates and formatted address from a given title.

###  Give titles from coordinates
#### => ParsedRequestedQuestionFromCoordinates
Give a key word for obtain wikipedia resources and other from share coordinates.

## Front End functionalities

### home.html
Simple home page with form field and two button: one submit button to send data from field to the back end. 
One button to trig JavaScript function for obtain users position.
The home page contain code for responsive application.  

### form.js
This JavaSript file contain tree main part: 
* At the beginning of the file functions for obtain user position and display it in the field. 
* jQuery selector and AJAX function to exchange json data with back end. 
* Some function to store conversation data in memory, in session storage. 

### GrandPyBot_style.css
Classic css. 