from flask import Flask, request, render_template

app = Flask(__name__,template_folder="templates",static_folder="templates/static")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        req_data=request.get_json()
        
        return render_template("login.html")
    else:
        return render_template("login.html")


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        req_data=request.get_json()
        
        return render_template("signup.html")
    else:
        return render_template("signup.html")

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)