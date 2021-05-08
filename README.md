__Steps to run the project:__

1. Install all the required libraries:<br>
__pip install -r requirements.txt__

2. Create the key for authentication with DB:<br>
run __cookingJar.py__ file and provide filename as __coverified.key__ and your CECID and password.<br>
This will provide you a key, that you have to keep handy to run the project.

3. Now need to run the cookie generator that will run every 6 hours:<br>
run __oreoGenerator.py__ and provide the private key that we have generated above, this will create a new file oreo to keep your cookies.

4. Now we need to install Hookbuster to listen on a localhost for BOT request:<br>
__git clone https://github.com/WebexSamples/hookbuster.git__<br>
now install all the libraries inside hookbuster folder >>> __npm install__.

5. Now we need to enable Hookbuster 2 times, so open 2 cmd window and __run node app.js__.<br>
Provide the BOT access token and port number, in project we kept Port number for Attachment Server as 8080 and Messaging Server as 8081.

__Attachment Server>__<br>
Access Token > ###########################################################################<br>
PORT > 8080<br>
Resources > aa<br>
Event > c<br>

__Message Server>__<br>
Access Token > ###########################################################################<br>
PORT > 8081<br>
Resources > m<br>
Event > c<br>

6. Now finally we need to run our flask services, __AttachmentServer.py__ and __MessageServer.py__<br>
both needs AccessToken and it may ask two times, while running the file (don't know why)