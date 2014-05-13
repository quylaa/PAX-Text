#Requires BeautifulSoup4 and Requests
#Find your mobile carrier's SMS Gateway from here:
#      http://www.ukrainecalling.com/email-to-text.aspx
#I have it set up to use Gmail's SMTP server, feel free to configure it otherwise

import requests
from bs4 import BeautifulSoup

import smtplib
import sched
import time

s = sched.scheduler(time.time, time.sleep)

def main(sc):
    page = requests.get('http://prime.paxsite.com/').content

    soup = BeautifulSoup(page)

    badges = '<ul id="badges">\n <li class="soon">\n  <h3>\n   Soon\n  </h3>\n </li>\n</ul>\n'

    test = soup.find(id='badges').prettify()

    if test == badges:
        print(time.strftime("[%I:%M:%S %p %d/%m]") + ' Nothing different...')
        sc.enter(30*1, 1, main, (sc, ))
    else:
        print('Go now!')
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login('username','password')
        server.sendmail('your@email.com','your-cell-phone-number@SMS-gateway.com','BUY THOSE PAX BADGES')
        server.quit()

s.enter(1, 1, main, (s, ))
s.run()