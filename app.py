from bottle import route, run, auth_basic, static_file, request

users = ['dave']
passwords = {'dave': 'password1'}

def authenticated(user, passwd):
    return user in users and passwords[user] == passwd

@route('/upload')
@auth_basic(authenticated)
def index():
    return static_file('upload.htm', root='/')

@route('/newfile', method='POST')
@auth_basic(authenticated)
def do_upload():
    upload = request.files.get('file')
    upload.save(f"/var/tmp/{upload.filename}")
    return f"File uploaded as {upload.filename}"

run(host='0.0.0.0', port=8000)
