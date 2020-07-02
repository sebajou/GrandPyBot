# GrandPyBot

This conversational bot will give you description of a location and a map to go there from an address. 
This is a test driven project. 

## Fonctionnalities

### Static page for display
Static HTML CSS page to display main information.

### Dynamic page for display
JavaScript / JQuery for modify body text with data query on back end.

### Parse, mother class for other parer
#### => Class Parse
This class parse message from front input from user and return it to API.
This class do it in tree step: 
* Step 1, format the message: lower the message, remove comma and dot and quotes, and put all word in a list. 
* Step 2, removed the verb from the list: two imbricate loop create verb prefix and verb termination from lists and
removed created verb from the list from step 1. 
* Step 3, with list from step 2, a stop word list is use for removed stop word. 
The results is a list of key word. 

### Parser for Google Map and com with API 
#### => Class GoogleMapParseCom
Parser for Google Map with Python back end. 
Speak with Google Map API with Python back end and Json message.
Inherit from Parse class: Parse message from front with the aim to do a list of key words use to interrogate the Google Map API. 
Obtain coordinates from Wiki Media. 
Transform this coordinates in string. 
Interrogate Google map API with this strong coordinates to obtain a static png map. 

### Parser for Media Wiki and com with API 
#### => Class MediaWikiParseCom 
Parser for Media Wiki with Python back end.
Speak with Media Wiki API with Python back end and Json message.
Inherit from Parse class: Parse message from front with the aim to do a list of key words use to interrogate the Media Wiki API. 
With a list of key word interrogate Wiki Media API to obtain a title corresponding to this key words. 


### Randomly sentence send
#### => Class RandomMessage
Engine to randomly send sentence from GranPapy with Python back end.

### Parser of json message from Media Wiki API 
#### => Class

### Json from API parser
#### => Class JsonParser
On back end Parse Json from API Google Map and Media wiki.

### Back end and Front end component for Ajax message
#### => Class AjaxMessage
Ajax for data exchange from server to front, POST.