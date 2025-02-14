from flask import Flask, redirect, render_template, request

app = Flask(__name__, static_url_path="/static")

def setTheme(theme):
    if theme == "light":
        return "light"
    else:
        return "dark"

@app.route("/blog/hello")
def hr():
  return redirect("/hello")

@app.route("/blog/bye")
def br():
  return redirect("/bye")

@app.route('/hello')
def hello():
    title = "Hello World"
    date = "October 25th"
    text = "Here is my first blog entry."
    theme = setTheme(request.args.get('theme'))
   
    return render_template("blog.html", title=title, date=date, text=text, theme=theme)



@app.route('/bye')
def bye():
    title = "Bye World"
    date = "October 25th"
    text = "Here is my last blog entry."
    theme = setTheme(request.args.get('theme'))
    return render_template("blog.html", title=title, date=date, text=text, theme=theme)
    

app.run(host='0.0.0.0', port=81)