Steps to run the project:

1. Install all the required libraries:
pip install -r requirements.txt

2. Create the key for authentication with DB:
run cookingJar.py file and provide filename as coverified.key and your CECID and password.
This will provide you a key, that you have to keep handy to run the project.

3. Now need to run the cookie generator that will run every 6 hours:
run oreoGenerator and provide the private key that we have generated above, this will create a new file oreo to keep your cookies.

4. Now we need to install Hookbuster to listen on a localhost for BOT request:
git clone https://github.com/WebexSamples/hookbuster.git
now install all the libraries inside hookbuster folder >>> npm install.

5. Now we need to enable Hookbuster 2 times, so open 2 cmd window and run node app.js.
Provide the BOT access token and port number, in project we kept Port number for Attachment Server as 8080 and Messaging Server as 8081.

Attachment Server>
Access Token > ###########################################################################
PORT > 8080
Resources > aa
Event > c

Message Server>
Access Token > ###########################################################################
PORT > 8081
Resources > m
Event > c

6. Now finally we need to run our flask services, AttachmentServer.py and MessageServer.py
both needs AccessToken and it may ask two times, while running the file (don't know why)