#To Get Flask Installed
- Download at least [Python 2.7.11](https://www.python.org/downloads/)  
- Then run `pip install Flask` from your terminal
- Next install virtualenv (make sure you do all this in one folder, ideally one for set aside for flask apps)

		sudo easy_install virtualenv  
		virtualenv venv  
		. venv/bin/activate  


	- To stop running virtualenv just type `deactivate` in your terminal
- Make a file called hello.py and put this code in it:

		from flask import Flask
		app = Flask(__name__)

		@app.route('/')
		def hello_world():
    		return 'Hello World!'

		if __name__ == '__main__':
    		app.run()
    		
	- **NOTE:** those are two underscores on each side of `name` and `main`, not one!
	- **ANOTHER NOTE:** the spacing is VERY IMPORTANT, Python uses spacing accomplish the same thing as curly braces in JavaScript
- Then in run the app from your terminal using `python hello.py`
	- You should see the following:
			
			* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

- Got to <localhost:5000> and check it out!