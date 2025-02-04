from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "Member" and password == "2016":
            resp = make_response(redirect(url_for('dashboard')))
            resp.set_cookie('member', 'false') 
            return resp
        else:
            return render_template('login.html', message="Invalid credentials!")
    return render_template('login.html', message="Hint : User is 'Member' and pwd is AlphaBit's Birth Year")

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', hint="He's our president, This is basic knowledge !")

@app.route('/El-Barae')
def page_hint1():
    return render_template('page_hint1.html', hint="Now, It's the BIG event !")

@app.route('/Alpha-CTF')
def page_hint2():
    return render_template('page_hint2.html', hint="Nice, go to the 'protected' area, if you're worthy.")

@app.route('/protected')
def page_protected():
    return render_template('page_protected.html', hint="Almost there! Rest and eat something !")

@app.route('/final-member')
def page_final():
    member = request.cookies.get('member', 'false')
    if member == 'true':
        return render_template('member_area.html') 

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
