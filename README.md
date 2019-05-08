# DigiGirlzCodingChallenge
## Intro
This repo was designed as a Digi Girlz coding challenge! It should take ~an hour and is useful for not super deep technical ability. It covers Python, HTML, and flask.

## Overview of the technology used:
The code in the .py file is written in Python. 

The code in the /templates folder that end in .html is written in HTML.

We are using a combination of both of these and a microframework called Flask (http://flask.pocoo.org/) to build a small locally hosted website!

We are also using Jinja, a templating language for python (http://jinja.pocoo.org/docs/2.10/).





## Setup:
If you're new to github check out: https://guides.github.com/

If you're new to navigating the Command Prompt check out: http://ifoundthemeaningoflife.com/learntocode/cmd101win

Open a Command Prompt/terminal and navigate to where the code files are being held or where you want them to land.

_I do recommend using virtual environments to manage the dependencies for your python projects. However, I will not be covering that in this project as it's aimed at beginners! If you want to find out more about how to use them with flask check out the documentation here: http://flask.pocoo.org/docs/1.0/installation/#virtual-environments_

Then run: 
```sh
git clone https://github.com/CRehfuss/DigiGirlzCodingChallenge.git
```

Navigate to the DigiGirlzCodingChallenge folder:
```sh
cd DigiGirlzCodingChallenge
```

Download flask via the command prompt:
```sh
pip install Flask
```
or 
```sh
python -m pip install Flask
```

_Hopefully_ that ran without any issues!!


To run the application, make sure you're in the DigiGirlzCodingChallenge folder and run:
```sh
python -m flask run
```
It should output a few lines and then say something similar to:
```sh
Running on http://127.0.0.1:5000/
```
If your url is different that's ok!

You can now navigate to that link in any browser and should see a blank page that says "Welcome to DigiGirlz"

**To stop the program, hit control C in the command prompt.**

When you make changes in either the python or html code make sure that you save your changes. Stop the program (control C) and re-run the application.
Refresh the webpage and you should see the effects of your changes. 

*Try changing line 13 to return something else!*

Check out what's on http://127.0.0.1:5000/hello 

It should be something different! To see what's going on check out the app.py file!

_app.route_ is how we specify what should be at different URL endings. Notice if you go to a url like http://127.0.0.1:5000/potato you will get a Not Found page. That's becasue we haven't specified that route. 

# So what's in our files?

**In app.py we have definitions for:**

* @app.route('/')
* @app.route('/hello')
* @app.route('/hello/<name>')

   Note that these two route are listed about the same indented code!  
   See what happens when you go to http://127.0.0.1:5000/hello/Claire

* @app.route('/facePhoto')

   This has most of the logic behind call the Microsoft Face API

* @app.route('/itemPhoto')

   This method is empty **For Now**! This is what you'll be filling out as a challenge!

These are all of the routes that we can navigate to!


**In the templates folder we have:**

* hello.html 

   A basic html file that is generated when /hello is on the url. It checks if there is a name on the end or not and returns different pages depending!

* photo.html

   This is the html that's returned from facePhoto

* itemphoto.html

   This is mostly empty and you'll fill it out as a challenge. It should be rendered from itemPhoto


# Helpful tipcs
You can use the terminal to view variables and other statements that you print in app.py

You can view the html that is generated by pressing Fn F12 and pulling up the Developer Tools. Or by left clicking and selecting _View Source_,_View Page Source_, etc. 

If you see Internal Server Error check the terminal output. The last line will give you a hint as to what the error was. 

If you see Page Not Found Error make sure that you have actually defined the route! 


# Challenges
Ok now to get to what you should try to do!

## Beginner
1. Go to all the routes that are in the app.py file! There should be 5 different URL's you go to!

1. Change what is printed when you go to http://127.0.0.1:5000/

2. Change the image that is being detected!

3. Try to make the /photo page to say "I don't see a photo with faces"

4. Print out the age of the people in the images

5. Print out some other description of the people!

6. Change Photo.html so that IF there is only one person you print out "There is only 1 face! Make some friends."

## Reach challenge!
7. Implement @app.route('/itemPhoto') and itemphoto.html


# Meta

Made by: Claire Rehfuss – [Twitter: @ClaireRehfuss](https://twitter.com/ClaireRehfuss) – Email: ClaireRehfuss@gmail.com


Github: [https://github.com/crehfuss](https://github.com/crehfuss/)