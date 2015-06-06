#!/usr/local/bin/python3
#
#   three_param.py
#
"""
1. Write a class named Dog. Dog's __init__() method should take two parameters, name and breed, in addition to the implicit self.
2. Bind an empty list to a dogs global variable (dogs should not be an attribute of the Dog class).
3. Using a while loop, get user input for name and breed. The loop should terminate when the user enters a blank name.
4. For each name and breed entered, create an instance of the Dog class with name and breed as arguments. Append the object to the dogs list.
5. Each time around the loop, print the current dogs list (the name and breed of each dog).
"""
class Dog:
    """ A Dog Class """
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

if __name__ == "__main__":
    dogs = []

    while True:
    
        uinname = input("Name: ")

        # Break out of the loop if user
        # enter a blank name
        if not uinname:
            break

        uinbreed = input("Breed: ")
        dogs.append(Dog(uinname, uinbreed))
        print("DOGS")
        ctr = 0
        for dog in dogs:
             print(str(ctr) + ". " + dog.name + ":" + dog.breed)
             ctr += 1

        print("****************************************")
