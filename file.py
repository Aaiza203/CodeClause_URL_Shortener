# Aaiza Naeem
# Python Development Intern
# CodeClause

import pyshorteners
url = input("Enter the URL: ")
shortener = pyshorteners.Shortener()
converted = shortener.tinyurl.short(url)
print(converted)