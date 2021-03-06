from auth import auth
from change_password import insert_new_passwd, change_password_form
from forgot_password import forgot_password, insert_new_password
from pysql import questions
from signup import signup_db
from snippet import put_snippet, get_all_snipets
from upload import upload_file
from vial import render_template, Vial


def index(headers, body, data):
    snippets = get_all_snipets()
    return render_template('index.html', headers=headers, body=body, snippets=snippets), 200, {}


def recovery(headers, body, data):
    question_tuple = questions()
    return render_template('recovery.html', headers=headers, body=body, data=data, questions=question_tuple), 200, {}


def signup(headers, body, data):
    question_tuple = questions()
    return render_template('signup.html', headers=headers, body=body, data=data, questions=question_tuple), 200, {}


def new_snippet(headers, body, data):
    return render_template('new_snippet.html', headers=headers, body=body, data=data), 200, {}


def upload(headers, body, data):
    return render_template('upload.html', body=body, data=data), 200, {}

routes = {
    '/': index,
    '/auth': auth,
    '/recovery': recovery,
    '/passwordRecovery': forgot_password,
    '/insert_new_password': insert_new_password,
    '/signup': signup,
    '/signup_db': signup_db,
    '/new_snippet': new_snippet,
    '/put_snippet': put_snippet,
    '/upload': upload,
    '/upload_file': upload_file,
    '/password_change_form': change_password_form,
    '/password_change': insert_new_passwd
}

app = Vial(routes, prefix='', static='/static').wsgi_app()
