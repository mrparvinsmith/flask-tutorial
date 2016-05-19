#The Docs
The [docs](http://flask.pocoo.org/docs/0.10/) for Flask.

#To Get Flask Installed
- Download at least [Python 2.7.11](https://www.python.org/downloads/)  
- Then run `pip install Flask` from your terminal
- Next install virtualenv (make sure you do all this in one folder, ideally one for set aside for flask apps)

		sudo easy_install virtualenv  
		virtualenv venv  
		. venv/bin/activate  


	- To stop running virtualenv just type `deactivate` in your terminal
- To test, let's make a file called hello.py and put this code in it:

		from flask import Flask
		app = Flask(__name__)

		@app.route('/')
		def hello_world():
    		return 'Hello World!'

		if __name__ == '__main__':
    		app.run()
    		
	- **NOTE:** those are two underscores on each side of `name` and `main`, not one!
	- **ANOTHER NOTE:** the spacing is VERY IMPORTANT, Python uses spacing to accomplish the same thing as curly braces in JavaScript
- Then run the app from your terminal using `python hello.py` (this is how we run python apps)
	- You should see the following:
			
			* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

- Got to [localhost:5000](http://localhost:5000) and check it out!

#Making an html page with Flask
- It has a library called Jinja that uses embedded Python, similar to how embedded javascript or ruby was done
	- Use `{%  %}` for the equivalent of flounders (do stuff, but don't show stuff)
	- Use `{{  }}` for the equivalent of squids (show stuff)