import time
import random

def print_output(message): 
    choice = input("{} [y/n]".format(message)) 
    if choice in ['y', 'Y', 'Yes', 'YES', 'yes']:
        return True 
    return False

def game():
    # Play game 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
    print("Welcome to the Cavern Adventure!") 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    print ("You enter a dark cavern out of curiosity. It is dark and you can only make out a small stick on the floor.")
    
    # Stick taken
    if print_output("Do you take it?"):
        print("You have taken the stick!") 
    # Stick not taken
    else:
        print("You did not take the stick")
    
    print ("Game continues.")
    
def main():
# game loop
    game()
    
if __name__ == "__main__": main()



