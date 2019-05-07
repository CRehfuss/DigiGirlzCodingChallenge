# DigiGirlzCodingChallenge
## Intro
This repo was designed as a Digi Girlz coding challenge! It should take ~an hour and is useful for not super deep technical ability. It covers Python, HTML, and flask.

## For beginners:
The code in the .py file is written in Python. 
The code in the /templates folder that end in .html is written in HTML.
We are using a combination of both of these and a microframework called Flask (http://flask.pocoo.org/) to build a small locally hosted website!





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



# Meta

Your Name – [@ClaireRehfuss](https://twitter.com/ClaireRehfuss) – ClaireRehfuss@gmail.com


[https://github.com/crehfuss](https://github.com/crehfuss/)