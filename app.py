import json
import sys
from pathlib import Path

from bottle import auth_basic, request, route, run, static_file
from werkzeug.security import check_password_hash

files = "/files"
passwd = "/passwd"


def authenticated(user, password):
    with open(passwd, "r") as p:
        auth = json.load(p)
    return user in auth and check_password_hash(auth[user], password)


@route("/upload")
@auth_basic(authenticated)
def index():
    return static_file("upload.htm", root="/")


@route("/newfile", method="POST")
@auth_basic(authenticated)
def do_upload():
    upload = request.files.get("file")
    upload.save(f"{files}/{upload.filename}")
    return f"File uploaded as {upload.filename}"


run(host="0.0.0.0", port=8000)
