## HW 1
## SI 364 F18
## 1000 points

#################################

## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".



## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications. Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

import requests
import json
from flask import Flask, render_template, flash, request

app = Flask(__name__)
app.debug = True

@app.route('/class')
def hello_to_you():
    return 'Welcome to SI 364!'

@app.route('/movie/<movie>')
def getstuff(movie): 
	baseurl = "https://itunes.apple.com/search" 
	params_diction = {}
	params_diction["term"] = movie
	resp = requests.get(baseurl, params=params_diction)
	text = resp.text
	return text

@app.route('/question')
def q_form():
	formstring = """
	<form action="http://localhost:5000/result" method="GET">
	<input type="text" name="number"> Enter a number: 
	<input type="submit" value="Submit">
	"""
	return formstring

@app.route('/result',methods=["GET"])
def result_qform():
    if request.method == "GET":
        print("ARGUMENTS", "     ", request.args) # Check out your Terminal window where you're running this...
        orig_num = request.args.get('number','')
        double = 2 * int(orig_num)
        result_str = "Double your favorite number is {}<br><br>".format(double)
        return result_str
    return "Nothing was selected this time!"

@app.route('/problem4form')
def problem4form():
    return """ 
  <p>What is your favorite movie genre? I will recommend you some phenomenal movies!</p>
  <form action="http://localhost:5000/result1" method='GET'>
  <input type="checkbox" name="movie1" value="Romantic Comedy"> I like romantic comedies<br>
  <input type="checkbox" name="movie2" value="Action"> I like action movies<br>
  <input type="checkbox" name="movie3" value="Drama"> I like drama Movies<br>
  <input type="submit" value="Submit">

  </form>
  <form action="http://localhost:5000/result2" method='GET'>
  I like a different genre of movie:<br><input type="text" name="movie4" value=0> <br>
  <input type="submit" value="Submit">
  </form>
	"""

# 

@app.route('/result1',methods=["GET"])
def result_form1():
    if request.method == "GET":
        print(request.args) # Check out your Terminal window where you're running this...
        result_str = ""
        for k in request.args: #request.args is how you access the results from a previous post
            #result_str += "{} - {}<br><br>".format(k, request.args.get(k,""))
            baseurl = "https://itunes.apple.com/search"
            params_diction = {}
            params_diction["term"] = request.args.get(k,"")
            resp = requests.get(baseurl, params=params_diction)
            text = resp.text
            python_obj = json.loads(text)
            movies = []
            for item in python_obj["results"]:
            	if item.get("kind") == "feature-movie":
	            	movies.append("<em>" + item["trackName"] + "<em>" + k)
            all_titles = "<br>".join(movies)
            return all_titles
    return "Nothing was selected this time!"

@app.route('/result2',methods=["GET"])
def result_form2():
    if request.method == "GET":
        print(request.args) # Check out your Terminal window where you're running this...
        result_str = ""
        for k in request.args: #request.args is how you access the results from a previous post
            #result_str += "{} - {}<br><br>".format(k, request.args.get(k,""))
            baseurl = "https://itunes.apple.com/search"
            params_diction = {}
            params_diction["term"] = request.args.get(k,"")
            resp = requests.get(baseurl, params=params_diction)
            text = resp.text
            python_obj = json.loads(text)
            movies = []
            for item in python_obj["results"]:
            	if item.get("kind") == "feature-movie":
	            	movies.append("<em>" + item["trackName"] + "<em>" + k)
            all_titles = "<br>".join(movies)
            return all_titles
    return "Nothing was selected this time!"

'''send form asking if they like popular movies, Oscar winning movies, or bad movies
go to imdb database, get results for top selling movies of all time (if popular), 
get the 
'''
if __name__ == '__main__':
    app.run()


## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should see something like the data shown in the included file sample_ratatouille_data.txt, which contains data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:

# {
#  "resultCount":0,
#  "results": []
# }


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.


## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application, following a few requirements.

## You should create a form that appears at the route: http://localhost:5000/problem4form

## Submitting the form should result in your seeing the results of the form on the same page.

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form and is readable by humans (more readable than e.g. the data you got in Problem 2 of this HW). The new data should be gathered via API request or BeautifulSoup.

# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)

# Points will be assigned for each specification in the problem.
