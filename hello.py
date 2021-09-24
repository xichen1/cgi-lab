#!/usr/bin/env python3
import os, json

print("Content-type:text/html\r\n\r\n")
print("<title>Test CGI</title>")
print("<p>Hello World cmput404 class!</p>")

print(os.environ)
json_object = json.dumps(dict(os.environ), indent = 4)
print(json_object)