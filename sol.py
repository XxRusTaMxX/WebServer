from flask import Flask
from flask import render_template, url_for, request
import sqlite3
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def __unicode__(self):
    return u"{}".format(self.name)

class LoginForm(FlaskForm):
    username = StringField('�����', validators=[DataRequired()])
    password = PasswordField('������', validators=[DataRequired()])
    remember_me = BooleanField('��������� ����')
    submit = SubmitField('�����')

@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return '''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport"
                            content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                            crossorigin="anonymous">
                            <title>������ �����</title>
                          </head>
                          <body>
                            <h1>����� ��� ����������� � �������������� �������</h1>
                            <form method="post">
                                <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="������� ����� �����" name="email">
                                <input type="password" class="form-control" id="password" placeholder="������� ������" name="password">
                                <div class="form-group">
                                    <label for="classSelect">� ����� �� ������</label>
                                    <select class="form-control" id="classSelect" name="class">
                                      <option>7</option>
                                      <option>8</option>
                                      <option>9</option>
                                      <option>10</option>
                                      <option>11</option>
                                    </select>
                                 </div>
                                <div class="form-group">
                                    <label for="about">������� � ����</label>
                                    <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                </div>
                                <div class="form-group">
                                    <label for="photo">��������� ����������</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <div class="form-group">
                                    <label for="form-check">������� ���</label>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                      <label class="form-check-label" for="male">
                                        �������
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                      <label class="form-check-label" for="female">
                                        �������
                                      </label>
                                    </div>
                                </div>
                                <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" for="acceptRules">����� ���� ������������</label>
                                </div>
                                <button type="submit" class="btn btn-primary">����������</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "����� ����������"
    
    
    
@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return '''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport"
                            content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                            crossorigin="anonymous">
                            <title>������ �������� �����</title>
                          </head>
                          <body>
                            <h1>�������� ����</h1>
                            <form method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">�������� ����</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">���������</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        print(f.read())
        return "����� ����������"
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return '''<!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <title>{}</title>
    </head>
      <body>
        <header>
          <nav class="navbar navbar-light bg-light">
            <a class="navbar-brand" href="#">���� ����������</a>
          </nav>
        </header>
        <!-- Begin page content -->
        <main role="main" class="container">
        <h1>�����������</h1>
    <form action="" method="post" novalidate>
        {{ form.hidden_tag() }}
        <p>
            {{ form.username.label }}<br>
            {{ form.username }}<br>
            {% for error in form.username.errors %}
                <div class="alert alert-danger" role="alert">
                    {{ error }}
                </div>
            {% endfor %}
        </p>
        <p>
            {{ form.password.label }}<br>
            {{ form.password }}<br>
            {% for error in form.password.errors %}
                <div class="alert alert-danger" role="alert">
                    {{ error }}
                </div>
            {% endfor %}
        </p>
        <p>{{ form.remember_me() }} {{ form.remember_me.label }}</p>
        <p>{{ form.submit() }}</p>
    </form>
        </main>
      </body>
    </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1') 