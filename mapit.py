import sys, webbrowser
# run this script in terminal, with arguments as the Address of the location you want to get to, in Google Maps 

if len(sys.argv)>1:
    addr = ''.join(sys.argv[1:])

webbrowser.open('https://www.google.com/maps/place/' + addr)
