#!/usr/bin/env python
# -*- coding utf-8 -*-

import smtplib
import requests
requests.packages.urllib3.disable_warnings()
import re

def main():
	urls = [
		('https://shop.pimoroni.com/products/raspberry-pi-zero', 4, 'Out of stock'),
		('https://www.adafruit.com/products/2885', 4, 'OUT OF STOCK'),
		('https://www.adafruit.com/products/2817', 4, 'OUT OF STOCK'),
		('https://thepihut.com/collections/new-products/products/raspberry-pi-zero?variant=14062734980', 1, 'OutofStock'),
		('http://www.element14.com/community/docs/DOC-79263?ICID=hp-pizero-ban', 2, 'SOLD OUT')
		]
	
	for url, count, search_term in urls:
		check(url, count, search_term)

#	print "sending fake message"
#	mailMe('http://fake.com')

def check(url, count, search_term):
	r = requests.get(url, verify=False)
	if r.status_code == 200:
		numberOfOccurrences = len(re.findall(search_term, r.text))
		if count != numberOfOccurrences:
			mailMe(url)

def mailMe(url):
	# edit in your credentials
	username = 'modubot'
	password = 'BeepBoop!'
	fromaddr = 'modubot@gmail.com'
	toaddr = 'petermjso@gmail.com'

	msg = 'Subject: Raspberry Pi Zero is back in stock'
	msg += '\nFrom: '.format(fromaddr)
	msg += '\nTo: '.format(toaddr)
	msg += '\n\n {}'.format(url)

	server = smtplib.SMTP_SSL('smtp.gmail.com:465')
	server.login(username, password)
	server.sendmail(fromaddr, toaddr, msg)
	server.quit

if __name__ == '__main__':
	main()
