#!/usr/bin/env python
import os
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
print "Content-type: text/html"
print
print """
<html>
<head><title>Robotic Arm Control</title></head>
<body>
<h3>Robotic Arm Control</h3>
"""
form = cgi.FieldStorage()
x = form.getvalue("x", "0")
y = form.getvalue("y", "0")
print """
<FORM ACTION="../cgi-bin/xy.py">
<INPUT TYPE=IMAGE SRC="/10x10.gif" BORDER=0>
</FORM>
<p>X=%s Y=%s</p>
</body>
</html>
""" % (cgi.escape(x),cgi.escape(y))
nx=int(cgi.escape(x))
ny=int(cgi.escape(y))
nx=nx-150
path = "/home/pi/arm.fifo"
fifo = open(path, "w")
fifo.write("%d,%d\n" % (nx,ny))
fifo.close()
