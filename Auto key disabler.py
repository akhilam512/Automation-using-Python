import os
#os.system( "command" ) # this sends command to the terminal directly 

#xmodmap -e 'keycode <keycodevalue>=' # this disables the keycoded value key

#to find out keycodevalue of a key, run : xev -event keyboard
#now enter the key you want to disable and try to find out the keycode value from the output 

os.system("xmodmap -e 'keycode 117='")  #disables pg down key

""" other examples:
os.system("xmodmap -e 'keycode 112='")  #disables pg up key
os.system("xmodmap -e 'keycode 115='")  #disables end key
os.system("xmodmap -e 'keycode 110='")  #disables home key
""" 

#place this file in "Startup Applications" (for Ubuntu users), so that the script is executed automatically at startup  
