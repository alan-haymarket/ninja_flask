from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

app = Flask(__name__)
app.secret_key = 'alan-haymarket'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninja():
	return render_template('ninja.html')

@app.route('/ninja/<color>', methods = ['GET'])
def show_ninja(color):
	if color == 'red':
		flash("It's Raphael")
		return render_template("ninja.html")
	elif color == 'blue':
		flash("It's Leonardo")
		return render_template("ninja.html")
	elif color == 'purple':
		flash("It's Donatello")
		return render_template("ninja.html")
	elif color == 'orange':
		flash("It's Michelangelo")
		return render_template("ninja.html")
	else:
		print "haha"
		flash("It's Megan Foxx")
    	return render_template('ninja.html')

app.run(debug=True)
