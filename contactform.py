#!C:\Python27\python.exe
# Import modules for CGI handling
import cgi, cgitb
cgi.test()
cgitb.enable()
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
email = form['email']
art_piece  = form.['art piece']
comments = form['Comments']

#contacts = open('contacts.txt', "w")
#contacts.write(email + '\t\t' + art_piece + '\t\t\t' + comments)

