from flask import Flask, request, render_template, url_for
from flask_scss import Scss
app = Flask(__name__)
Scss(app, static_dir='website ethicate/static/css',asset_dir='website ethicate/static/sass')

Gooddeedlist = []
Baddeedlist = []
GoodWords = ["help", "taught", "gave"]
BadWords = ["hit", "yell", "stole"]

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/listPage", methods=["GET", "POST"])
def listPage():
    if request.method == 'POST':
        deed = request.form['deed']
        nwidth = 5*len(Gooddeedlist) - 5*len(Baddeedlist)
        for word in GoodWords:
            if word in deed:
                Gooddeedlist.append([len(Gooddeedlist) + 1, deed, 5])
                return render_template('listPage.html', Gooddeeds = Gooddeedlist, Baddeeds = Baddeedlist, width = width, Good = 1, Bad = 0)
        for word in BadWords:
            if word in deed:
                Baddeedlist.append([len(Baddeedlist) + 1, deed, -5])
                return render_template('listPage.html', Gooddeeds = Gooddeedlist, Baddeeds = Baddeedlist, width = 5*len(Gooddeedlist) - 5*len(Baddeedlist), Good = 0, Bad = 1)
        return render_template('listPage.html', Gooddeeds = Gooddeedlist, Baddeeds = Baddeedlist, width = 5*len(Gooddeedlist) - 5*len(Baddeedlist), Good = 0, Bad = 0)
    else:
        return render_template('listPage.html')
    
   
if __name__ == "__main__":
    app.run() 
