from flask import render_template
from app import app

with open("/js/index.js") as f:
    javascript = f.read()

f.close()

with open("/css/index.css") as f:
    style = f.read()

f.close()

@app.route("/css")
def css():
    return style

@app.route("/script")
def javascript():
    return javascript
    
@app.route("/")
@app.route("/index")
def index():
    user = {"username":"trevor"}
    links = [
        {'url': "https://www.python.org/", 'text':"[Python]"},
        {'url': "learn/Learn Python The Hard Way, 3rd Edition .pdf", 'text': ". Learn Python The Hard Way"},
        {'url': "https://realpython.com/list-comprehension-python/", 'text': ". Python - (list comprehension)"},
        {'url': "https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world", 'text': ". Python - (flask mega tutorial)"}, 
        {'url': "https://kivy.org/", 'text': ". Python - (kivy GUI for RAD)"},
        {'url': "learn/PythonNotesForProfessionals.pdf", 'text': ". Python - (notes)"},
        {'url': "", 'text': "<br />"},
        {'url': "https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript", 'text': "[Javascript]"},
        {'url': "https://developer.mozilla.org/en-US/docs/Web/JavaScript", 'text': ". Javascript - (MDN)"},
        {'url': "learn/JavaScriptNotesForProfessionals.pdf", 'text': ". Javascript - (notes)"},
        {'url': "learn/NodeJSNotesForProfessionals.pdf", 'text': ". NodeJS - (notes)"},
        {'url': "", 'text': "<br />"},
        {'url': "https://whatwg.org/", 'text': "[HTML]"},
        {'url': "https://developer.mozilla.org/en-US/docs/Web/HTML",'text': ". HTML - (MDN)"},
        {'url': "learn/HTML5NotesForProfessionals.pdf", 'text': ". HTML5 - (notes)"},
        {'url': "", 'text': "<br />"},
        {'url': "https://www.w3.org/Style/CSS/", 'text': "[CSS]"},
        {'url': "https://developer.mozilla.org/en-US/docs/Web/CSS", 'url': ". CSS - (MDN)"},
        {'url': "https://css-tricks.com/guides/",'text': ". CSS guides - (css-tricks)"},
        {'url': "", 'text': "<br />"},
        {'url': "http://www-formal.stanford.edu/jmc/recursive.pdf", 'text': "[LISP]"},
        {'url': "http://www.lisperati.com/casting.html", 'text': ". Casting SPELs in LISP"},
        {'url': "https://clojure.org/guides/getting_started", 'text': ". Clojure"},
        {'url': "https://www.haskell.org/", 'text': ". Haskell"},
        {'url': "https://www.erlang.org/", 'text': ". Erlang"}]
    return render_template("index.html", title="home", user=user, links=links)
