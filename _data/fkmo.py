#!/usr/bin/python3
#-*- coding: utf-8 -*-
import re,readline,sys
y=input("")
r=re.compile("([^\) \s]*)\s*\(([^\) \s]*)\s*[123456]\)")
r2=re.compile("([^\) \s]*)\s*([^\) \s]*(학교|고|중))\s*[123456][^\)]")

output=""
lastline=""
award=""
for g1 in sys.stdin:
    if g1.find("최우수상")>=0:
        award="최우수상"
    elif g1.find("우수상")>=0:
        award="우수상"
    if g1.find("대    상")>=0:
        award="대상"
    if g1.find("대   상")>=0:
        award="대상"
    if g1.find("대  상")>=0:
        award="대상"
    if g1.find("대 상")>=0:
        award="대상"
    if g1.find("대상")>=0:
        award="대상"
    if g1.find("금    상")>=0:
        award="금상"
    if g1.find("금   상")>=0:
        award="금상"
    if g1.find("금  상")>=0:
        award="금상"
    if g1.find("금상")>=0:
        award="금상"

    if g1.find("은    상")>=0:
        award="은상"
    if g1.find("은   상")>=0:
        award="은상"
    if g1.find("은  상")>=0:
        award="은상"
    if g1.find("금 상")>=0:
        award="금상"
    if g1.find("은 상")>=0:
        award="은상"
    if g1.find("동    상")>=0:
        award="동상"
    if g1.find("동   상")>=0:
        award="동상"
    if g1.find("동  상")>=0:
        award="동상"
    if g1.find("동 상")>=0:
        award="동상"
    if g1.find("은상")>=0:
        award="은상"
    if g1.find("동상")>=0:
        award="동상"
    if g1.find("장려상")>=0:
        award="장려상"
    if g1.find("5%")>=0:
        award="상위 5% 이내"
    if g1.find("10%")>=0:
        award="상위 10% 이내"
    if g1.find("15%")>=0:
        award="상위 15% 이내"
    if g1.find("20%")>=0:
        award="상위 20% 이내"
    if g1.find("25%")>=0:
        award="상위 25% 이내"
    if g1.find("30%")>=0:
        award="상위 30% 이내"
    if lastline=="" and g1.count("(")>g1.count(")"):
        print ("---")
        lastline=g1
        continue
    str=lastline.replace("\n","")+g1
    lastline=""
    m=r.finditer(str)
    for i in m:
        sc=i.group(2).replace("고등학교","고").replace("중학교","중").replace("초등학교","초").replace("과고","과학고")
        output=output + ( "%s,%s,%s,%s\n" % (y, i.group(1).replace("*",""), sc,award))
    m=r2.finditer(str)
    for i in m:
        sc=i.group(2).replace("고등학교","고").replace("중학교","중").replace("초등학교","초").replace("과고","과학고")
        output=output + ( "%s,%s,%s,%s\n" % (y, i.group(1).replace("*",""), sc,award))

print ("======")
print (output)
