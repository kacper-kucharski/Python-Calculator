
#!/usr/bin/python

import sys
import functions
import types

'''
The entry-point of our application.
'''
def main():
    # Indicates whether or not our application should quit
    quit = False

    # Implement basic functionality
    while(not quit):
        command = input("")
        if command == "quit":
            quit = True
        elif command == "help":
            functions.print_functions()
        elif command == "version":
            print("calculator version 0.1")
        else: 
            functions.process_line(command)    
  
if __name__== "__main__":
    main()