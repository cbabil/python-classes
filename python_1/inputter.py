#!/usr/local/bin/python3
#
#   inputter.py
#
"""
1. Write a program that uses a while loop to accept input from the user (if the user presses Enter, exit the program).
2. Save the input to a file, then print it.
3. Upon starting, the program will display any previous content of the file.
"""
# Open the file for reading, writing and appending
# If the file does not exist, it will be created
# automatically.
fh = open('file.txt', 'a+')

while True:

    # Check the current position
    # of the pointer in the file
    pos = fh.tell()

    if pos > 0:
        # Reposition the pointer at
        # the begining of the file
        fh.seek(0,0)

        # Output the content of the file
        print(fh.read(pos))

    uin = input("Enter text: ")
   
    # Break out of the loop if user presses Enter
    # without any text
    if not uin:
        break
    
    # Write to the file
    fh.write(uin) 

# Close the file handler
fh.close()


