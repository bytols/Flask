from flask import Flask , render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'asdas8d9asdjasjda0sd9131basldxxas'

posts = [
    {
        'title': 'Post 1',
        'content': 'This is the content of post 1',
        'author': 'John Doe',
        'date_posted': 'April 20, 2024'
    },
    {
        'title': 'Post 2',
        'content': 'This is the content of post 2',
        'author': 'Erick Rocha',
        'date_posted': 'April 21, 2024'
    },
    {
        'title': 'Post 3',
        'content': 'This is the content of post 3',
        'author': 'Helena Sanchez',
        'date_posted': 'April 22, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html' , posts = posts , title = 'pagina')


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html" , title = "login" , form = form )

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html" , title = "register" , form = form )

if __name__ == '__main__':
    app.run(debug=True)