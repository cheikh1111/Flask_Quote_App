from flask import Flask , render_template , url_for , redirect
from requests import get
from random import choice


app = Flask(__name__)
def load_quote():
    category = choice([ "life"       ,"success"       ,"amazing"     ,
                        "cool"       ,"attitude"      ,"computers"   ,
                        "courage"    ,"car"           ,"change"      ,
                        "business"   ,"morning"       , "dreams"     ,
                        "education"  ,"failure"       ,"family"      ,
                        "funny"      ,"future"        ,"graduation"  ,
                        "food"       ,"forgiveness"   ,"great"       ,
                        "health"     ,"intelligence"  ,"men"         ,
                        "government" ,"experience"    ,"learning"    ,
                        "leadership" ,"knowledge"     ,"learning"
                        
                        ])
    
    quotes_api = f'https://api.api-ninjas.com/v1/quotes?category={category}'
    response=get(quotes_api,headers={'X-Api-Key': 'q79+Z1ci+UI+QpBOFvQ8ow==yW7ecdmkRKeR5CBq'})
    quote_elements = response.json()[0]
    quote = quote_elements.get("quote")
    author = quote_elements.get("author")
    category = quote_elements.get("category")
    return quote, author,category


skills=[('python',85),
        ('Html',95),
        ('Css',89),
        ('Git',75)
        ]

@app.route("/")
@app.route("/home")

def home():
    quote,author,category= load_quote()
    return render_template("home.html",
                           title="Minute Quote",
                           quote=quote,
                           author=author,
                           category=category,
                           skills=skills)

@app.route("/Contact")
@app.route("/contact")
def contact():
    return render_template("contact.html",
                            title="Contact")

@app.route("/source")
@app.route("/source_code")
def source():
    return redirect("https:github.com/cheikh1111/Flask_Quote_App")


@app.errorhandler(404)
def e404(e):
    return render_template('404.html',
                            title="404 Page Not Found")
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

