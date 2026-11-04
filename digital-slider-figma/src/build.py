# Builds ../index.html from shell.html + app.js (+ the reference renders as data URLs).
import os
d=os.path.dirname(os.path.abspath(__file__))
s=open(os.path.join(d,'shell.html')).read(); a=open(os.path.join(d,'app.js')).read()
a=a.replace('/*RENDERS*/',open(os.path.join(d,'renders.js')).read())
open(os.path.join(d,'..','index.html'),'w').write(s.replace('/*APP*/',a))
