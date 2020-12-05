from flask import Flask, url_for, request, render_template, session, redirect, make_response

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    if 'user' in session:
        return "Hello %s!" % session['user']
    else:
        title = request.args.get('title', '游客')
        # return render_template('login.html', title=title)
        # # 构建响应
        response = make_response(render_template('login.html', title=title), 200)
        response.headers['key'] = 'value'
        return response


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('login'))


app.secret_key = '123456'
if __name__ == "__main__":
    app.run(debug=True)