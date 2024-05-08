#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
operands = form.getlist('operand')
username = form.getvalue('username', None)

try:
    total = sum(map(int, operands))
    body = "Your total is: {}".format(total)
except (ValueError, TypeError):
    body = "Unable to calculate sum: Please provide integer operands."

print("Content-type: text/plain")
print()
print(f"{username}, this is the result of your sum:")
print(body)
