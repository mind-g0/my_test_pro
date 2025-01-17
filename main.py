from flask import Flask, request, jsonify, render_template

#create flask instance >>
app = Flask(__name__)

# this if statement is used to render the page of the main.py file
if __name__ == "__main__":
    app.run(debug=True)


#create a route for any page >>

@app.route('/')
#before i use this def i shuold add atemplets folder and i put the index.html or any other pages in the folder of templates
def home():
    return render_template("index.php")
# if i put  /about in the route of the url ( ex:> http://127.0.0.1:5000/about ) it will show the page of about
@app.route('/about')
def about():
    return "<h1> something else <h1>" 

#this will allow the user to enter his name in the url and it will show it in the page >>

@app.route('/hello/<user>')
def hello(user):
    names=["ahmed","mohamed","ali","omar","khaled"]
    #this line will show the name of the user in the page
    return render_template("user.php", name=user,names=names)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> the name-the replas


