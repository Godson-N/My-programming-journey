import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")   #clears screen for windows, mac & linux OS

auction = {}
more_bidders = True

while more_bidders:
    print("Welcome to the auction")
    name = input("Enter your name: \n")
    bid = int(input("Enter your bid: \n$"))

    auction[name] = bid
    next_bidder = input("Is there another bidder? 'yes' or 'no' \n")

    if next_bidder == 'yes':
        clear_screen()
    elif next_bidder == 'no':
        more_bidders = False

highest_bid = 0
for name in auction:
    if auction[name] > highest_bid:
        highest_bid = auction[name]
        highest_bidder = name

print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}.")