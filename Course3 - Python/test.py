import time
import random

def print_output(decision): 
    choice = "i"
    while (choice == "i"):
        choice = input("{} [y/n] \n(Enter i to see you inventory. )".format(decision)) 
        if (choice == "i"):
            # print_inventory()
            pass
        if choice in ['y', 'Y', 'Yes', 'YES', 'yes']:
            return True 
    return False

def game():
    # Get global variables global inventory
    inventory = {"torch": 2}
    # Play game 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
    print("Welcome to the Cavern Adventure!") 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Start : %s" % time.ctime())
    # time.sleep(3)
    print("End : %s" % time.ctime())
    
    print ("You enter a dark cavern out of curiosity. It is dark and you can only make out a small stick on the floor.")
    
    # Stick taken
    if print_output("Do you take it?"):
        num = random.random() 
        print(num)
        if num < 0.8:
            print("You have taken the stick!") 
            # time.sleep(2)
            inventory["stick"] = 1
        else:
            print("Oh no! The stick was actually a snake.") 
            # time.sleep(1)
            complete = 0
            return complete
    # Stick not taken
    else:
        print("You did not take the stick")
    
    print ("Game continues. \nAs you proceed further into the cave, you see a large glowing object")
    
def main():
# game loop
    game()
    
if __name__ == "__main__": main()



