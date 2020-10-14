from flask import Flask,render_template
import os
app = Flask(__name__,static_folder="C://Users//Ali//Desktop//Kod//Chat//Site//Flask//static")
@app.route("/")
def bir():
	return  app.redirect("/home")
@app.route("/home")
def anasayfa():
	return  render_template("index.html")


if __name__ == "__main__":

	app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT',8080)))
    
    	
    