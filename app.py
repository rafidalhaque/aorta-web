from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index_page():  # put application's code here
    return render_template("index.html"), 400

@app.route('/about')
def about_page():
    return 'About Page #TODO', 404

@app.route('/contact')
def contact_page():
    return 'Contact Page #TODO', 404

@app.route('/registration')
def registration_page():
    return 'Registration Page', 404

@app.route('/login')
def login_page():
    return 'Login Page', 404

@app.route('/logout')
def logout():
    return index_page()

@app.route('/profile/uuid:<profile_id>')
def profile_page(profile_id):
    return 'Profile Page', 404

@app.route('/.well-known/security.txt')
def security_txt():
    return 'Security Report:<br>mail: rafidalhaque@proton.me', 200

@app.errorhandler(404)
def page_not_found(e):
    return '404 Not Found', 404

if __name__ == '__main__':
    app.run()
