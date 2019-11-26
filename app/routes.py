from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app import app
from app.forms import LoginForm
from app.models import User

# user = {
#     "username":"trevor", 
#     "splash": "/static/images/becca-romine-Lll4QeybDEg-unsplash.jpg",
#     "audio": {"hover":"/static/audio/select.wav"},
#     }
# links = [
#     {'url': "https://www.python.org/", 'text':"[Python]"},
#     {'url': "static/learn/Learn Python The Hard Way, 3rd Edition .pdf", 'text': ". Learn Python The Hard Way"},
#     {'url': "https://realpython.com/list-comprehension-python/", 'text': ". Python - (list comprehension)"},
#     {'url': "https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world", 'text': ". Python - (flask mega tutorial)"}, 
#     {'url': "https://kivy.org/", 'text': ". Python - (kivy GUI for RAD)"},
#     {'url': "static/learn/PythonNotesForProfessionals.pdf", 'text': ". Python - (notes)"},
#     {'url': "", 'text': "<br />"},
#     {'url': "https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript", 'text': "[Javascript]"},
#     {'url': "https://developer.mozilla.org/en-US/docs/Web/JavaScript", 'text': ". Javascript - (MDN)"},
#     {'url': "static/learn/JavaScriptNotesForProfessionals.pdf", 'text': ". Javascript - (notes)"},
#     {'url': "static/learn/NodeJSNotesForProfessionals.pdf", 'text': ". NodeJS - (notes)"},
#     {'url': "", 'text': "<br />"},
#     {'url': "https://whatwg.org/", 'text': "[HTML]"},
#     {'url': "https://developer.mozilla.org/en-US/docs/Web/HTML",'text': ". HTML - (MDN)"},
#     {'url': "static/learn/HTML5NotesForProfessionals.pdf", 'text': ". HTML5 - (notes)"},
#     {'url': "", 'text': "<br />"},
#     {'url': "https://www.w3.org/Style/CSS/", 'text': "[CSS]"},
#     {'url': "https://developer.mozilla.org/en-US/docs/Web/CSS", 'text': ". CSS - (MDN)"},
#     {'url': "https://css-tricks.com/guides/",'text': ". CSS guides - (css-tricks)"},
#     {'url': "", 'text': "<br />"},
#     {'url': "http://www-formal.stanford.edu/jmc/recursive.pdf", 'text': "(LISP)"},
#     {'url': "http://www.lisperati.com/casting.html", 'text': ". Casting SPELs in LISP"},
#     {'url': "https://clojure.org/guides/getting_started", 'text': ". Clojure"},
#     {'url': "https://www.haskell.org/", 'text': ". Haskell"},
#     {'url': "https://www.erlang.org/", 'text': ". Erlang"}]

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="home", user=current_user, links=[])

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))    
    return render_template("login.html", title="Sign In", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
