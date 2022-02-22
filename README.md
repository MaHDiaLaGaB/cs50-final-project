# Go Live Pro

### Video Demo [ Project in action](https://youtu.be/z0QfeRAUaAU)
## WHY THIS PROJECT

### My motivation

This is the final project for CS50 Harvard online program 
after nine weeks of studying hard between learning the 
essentials of programming with C to the advanced 
topics in C programming to more modern language 
.
 It is python and from here we learned more 
about frameworks and here i loved Flask.

### Problem to solve

I have a GoPro hero 9 camera I was wondering 
how I can download my media or stream without 
a USB cable, and after searching around the 
internet I found nothing, and here the idea 
comes up to me about how I can make a web app
 to automate and stream by GoPro 9 without cable.

### What I learned
- Manage and build a web app from the ground 
with MVC (Model-View-Controller) structure.

- How to use blueprints, how to use more than one language
to build one app.
- Flask was really nice practice for me
to use SQLalchemy, blueprints, hash passwords, dealing with sessions.
- I learned the logic of HTTP requests and manipulating DOM, sending requests between 
**Frontend** and **Backend** without refreshing the page using 
JQuery and Javascript and finally how to use
OpenCV library.

## Project Description

It is a Flask web app that gives you the power to control your 
Go Pro Hero camera without a wire, just connect your camera
via wifi and you can change camera settings, take photos,
shoot the video even stream live and record the your stream by just hitting a button
from the website.

I used python as the main Backend language with Flask
as a framework, for the Frontend Javascript and JQuery library
of course, CSS and Bootstrap make the website looks joyful.


## How to Use Go-Live Pro

- Connect your GoPro Hero camera via wifi and you can do 
   that in these steps:
   1. Connect your camera to **GoPro Quik** application on
   your smartphone and pair it.
   2. In **GoPro Quik** hit **Control Your GoPro** button,
   which will trigger the camera wifi to be open and be able
   to find it by your Laptop or Pc.
   3. On your machine search for new networks available,
   you should find your **GoPro Camera** and you are good
   to go.
- Lunch Flask by running run.py on local server.
- Make an account by registering, if you have
   one already just log in.
- go to GoLive! and you will find buttons where you can
  control your camera and change settings, take photos and shoot videos.
- You can go live stream by clicking on **You wanna Stream live? Click Here**,
  the stream will start automaticlly and recording automaticlly too, you can change the recording time window from the this file [live.py](project/main/live.py) on line 79.
- you can download the recorded video by clicking on 
  **Download Your Record** this will happen just if the
  app is hosted, if it's running locally on your machine
  you will find the recorded video here in [videos](project/videos) folder.
  

## Challenges I faced

- the lack of references to use GoPro for Livestream was my first
issue and I kept taking the API examples as reference.

- as new to python language I had to learn during working on the project,
  using Object Oriented programming was a real challenge for me,
  the issues and errors I faced made me more knowledgeable
  how to fix this type of error in the future.


## Stack and libraries
- **Frontend** HTML, CSS, Bootstrap, Javascript, JQeury
- **Backend** Python, Flask, SQLite
- **Libraries** Flask, Flask login,Flask-SQLAlchemy, 
  bcrypt, openCV, 
  goprocam, socket, os, time, numpy, python-dotenv.


## future features
- the abillty to Start and Stop the stream by clicking on start or stop buttons.
- start recoding whenever you like by one click.
- share the stream on Youtube and twich.
- face ditiction.
  
