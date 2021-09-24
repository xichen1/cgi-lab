#!/usr/bin/env python3
import cgi, cgitb
# Python 3.7 versus Python 3.8
try:
    from cgi import escape #v3.7
except:
    from html import escape #v3.8
import secret, os
from http.cookies import SimpleCookie
from templates import secret_page, after_login_incorrect

def after_login_correct():
    print("Set-Cookie: username=" + secret.username + ";")
    print("Set-Cookie: password=" + secret.password)
    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    print("<head>")
    print("<title>Hello - Second CGI Program</title>")
    print("</head>")
    print("<p><b>Username</b> %s <b>password</b> %s</p>" % (username, password))
    print("</body>")
    print("</html>")


form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')

cookie = SimpleCookie(os.environ.get("HTTP_COOKIE"))
if(cookie.get("username") and cookie.get("password") and 
cookie.get("username").value == secret.username and cookie.get("password").value == secret.password):
        print("Content-type:text/html\r\n\r\n")
        print(secret_page(cookie.get("username").value, cookie.get("password").value))

elif(username == secret.username and password == secret.password):
    after_login_correct()
            
else:
    print("Content-type:text/html\r\n\r\n")
    print(after_login_incorrect())

