#!/usr/bin/python3
#-*- coding: utf-8 -*-
import re,readline
y=input("")
r=re.compile("([\S]*)\s*\(([^\) ]*)\s*[123]\)")
g1=raw_input("GOLD")
g2=raw_input("")
g3=raw_input("")
g4=raw_input("")

m=r.finditer(g1)
for i in m:
    print "%s,%s,%s,금" % (y,i.group(1), i.group(2))
    
m=r.finditer(g2)
for i in m:
    print "%s,%s,%s,은" % (y,i.group(1), i.group(2))


m=r.finditer(g3)
for i in m:
    print "%s,%s,%s,동" % (y,i.group(1), i.group(2))



m=r.finditer(g4)
for i in m:
    print "%s,%s,%s,장려" % (y,i.group(1), i.group(2))

