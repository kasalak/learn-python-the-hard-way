""" import argv from sys to be able to get the filename """
from sys import argv
""" packs script and one variable (filename) into argv """
script, filename = argv
''' lets us open non-hardcoded filename'''
txt = open(filename)
''' prints filename and then what is in the file '''
print "Here's your file %r:" % filename
print txt.read()
txt.close()
'''repeats line 8-9 again, but in a different manner'''
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
