from requests import get
from bs4 import BeautifulSoup as bs
lang=input('사용하는 언어의 정식 영문 명칭을 입력해주세요 : ')
if lang=='C#': lang='C Sharp'
name=input('이름을 입력해주세요 : ')
desc=input('설명을 입력해주세요 : ')
try:
    color=bs(get('https://simpleicons.org/').text,'lxml').find(title=lang+' color')
    darklist=[]; brightlist=[]; color1, color2 = '', ''; colorlist = list(color.text[1:])
except: print('없는 언어입니다'); exit()
for i in range(0,6,2):
    temp=int(colorlist[i]+colorlist[i+1],16)
    if temp<20: darklist.append(00); brightlist.append(20)
    elif temp>234: darklist.append(235); brightlist.append(255)
    else: darklist.append(temp-20); brightlist.append(temp+20)
for j in range(0,3):
    if len(str(hex(brightlist[j]))[2:])==1: color1=color1+'0'
    if len(str(hex(darklist[j]))[2:])==1: color2=color2+'0'
    color1=color1+str(hex(brightlist[j]))[2:]; color2=color2+str(hex(darklist[j]))[2:]
if str(color).split('copy-color contrast-')[1][:4]=='dark': textcolor='black'
else: textcolor='white'
final='<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="z-index:1;position:relative" width="854" height="300" viewBox="0 0 854 300"><g transform="translate(427, 150) scale(1, 1) translate(-427, -150)"><defs><linearGradient id="linear" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#'+color1+'"/><stop offset="100%" stop-color="#'+color2+'"/></linearGradient></defs><path d="" fill="url(#linear)" opacity="0.4"><animate attributeName="d" dur="20s" repeatCount="indefinite" keyTimes="0;0.333;0.667;1" calcmod="spline" keySplines="0.2 0 0.2 1;0.2 0 0.2 1;0.2 0 0.2 1" begin="0s" values="M0 0L 0 220Q 213.5 260 427 230T 854 255L 854 0 Z;M0 0L 0 245Q 213.5 260 427 240T 854 230L 854 0 Z;M0 0L 0 265Q 213.5 235 427 265T 854 230L 854 0 Z;M0 0L 0 220Q 213.5 260 427 230T 854 255L 854 0 Z"/></path><path d="" fill="url(#linear)" opacity="0.4"><animate attributeName="d" dur="20s" repeatCount="indefinite" keyTimes="0;0.333;0.667;1" calcmod="spline" keySplines="0.2 0 0.2 1;0.2 0 0.2 1;0.2 0 0.2 1" begin="-5s" values="M0 0L 0 220Q 213.5 260 427 230T 854 255L 854 0 Z;M0 0L 0 245Q 213.5 260 427 240T 854 230L 854 0 Z;M0 0L 0 265Q 213.5 235 427 265T 854 230L 854 0 Z;M0 0L 0 220Q 213.5 260 427 230T 854 255L 854 0 Z"/></path><path d="" fill="url(#linear)" opacity="0.4"><animate attributeName="d" dur="20s" repeatCount="indefinite" keyTimes="0;0.333;0.667;1" calcmod="spline" keySplines="0.2 0 0.2 1;0.2 0 0.2 1;0.2 0 0.2 1" begin="-10s" values="M0 0L 0 235Q 213.5 280 427 250T 854 260L 854 0 Z;M0 0L 0 250Q 213.5 220 427 220T 854 240L 854 0 Z;M0 0L 0 245Q 213.5 225 427 250T 854 265L 854 0 Z;M0 0L 0 235Q 213.5 280 427 250T 854 260L 854 0 Z"/></path></g><svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="'+textcolor+'" height="40" x="-40%" y="35.5%">'+get('https://simpleicons.org/icons/'+lang.lower().replace(' ','').replace('+','plus')+'.svg').text.split('</title>')[1]+'<text xmlns="http://www.w3.org/2000/svg" text-anchor="start" alignment-baseline="middle" x="15%" y="44%" style="fill: '+textcolor+'; @import url(//fonts.googleapis.com/css?family=Lato:300); font-size: 50px; font-family: \'Lato\', sans-serif; font-weight: 300;">'+name+'</text><text xmlns="http://www.w3.org/2000/svg" text-anchor="end" alignment-baseline="middle" x="92%" y="44%" style="fill: '+textcolor+'; @import url(//fonts.googleapis.com/css?family=Lato:300); font-size: 23px; font-family: \'Lato\', sans-serif; font-weight: 300;">'+desc+'</text></svg>'
file=open('Nametag.svg','w')
file.write(final); file.close()
