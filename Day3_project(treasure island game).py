#this code displays a simple treasure island game based on some conditional statements

print("Welcome to Treasure Island!!! \nYour mission is to find the hidden treasure. \nBeware of the beast that lurks within!!!")

way = input("You have reach a crossroad. Which way is it going to be? 'left' or 'right'?  ").lower()

if way == 'left':
    print("The path is clear. Advance to the next level.")
    
    river = input("Oh no!!! How do we get pass this river? \nWill you 'swim' or 'wait'?  ").lower()
    
    if river == 'wait':
        print("Here comes a boat. You're very lucky. \nAdvance to the next level.")
        
    else:
        print("SHARKS!!! No where to go!!! GAME OVER!!!")
        
        door = input("Three doors!!! What door is it going to be? \n 'yellow' 'red' or 'green'?  ").lower()
        
        if door == 'yellow':
            print("YOU WIN!!! You have discovered the treasure!")
            
        else:
            print("GAME OVER!!! You were so close but the beast got you. \nBe careful in your next life.")

else:
    print("GAME OVER!!! You've been attacked by a pack of wolves.")