from flask import Flask , render_template , url_for , request
from requests import get
from random import choice
from time import sleep

app = Flask(__name__)
category = choice(["life", "success", "morning" , "learning" , "leadership" , "knowledge"])
quotes_api = f'https://api.api-ninjas.com/v1/quotes?category={category}'
response=get(quotes_api,headers={'X-Api-Key': 'q79+Z1ci+UI+QpBOFvQ8ow==yW7ecdmkRKeR5CBq'},timeout=4)
quote_elements = response.json()[0]
quote = quote_elements.get("quote")
author = quote_elements.get("author")
category = quote_elements.get("category")




# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template("home.html",title="Home Page",quote=quote,author=author,category=category)

@app.route("/Contact")
@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

@app.errorhandler(404)
def e404(e):
    return render_template('404.html', title="404 Page Not Found")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

