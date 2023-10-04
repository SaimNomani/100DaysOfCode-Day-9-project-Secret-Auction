# from replit import clear: This line of code only works if
#                           you are running your program in Replit and is used to clear the screen.
from art import logo

participants = {}
want_to_continue = 'yes'
print(logo)
while want_to_continue == 'yes':
    name = input("What is your name?: ")
    bid = int(input("What is your bid: $"))
    participants[name] = bid
    want_to_continue = (input("Are there any other bidders? Type 'yes' or 'no': ")).lower()
    if want_to_continue == 'no':
        break
    # elif want_to_continue=='yes':
        # clear(): to clear the screen
highest_bid = 0
highest_bidder = ''
for key in participants:
    if participants[key] > highest_bid:
        highest_bid = participants[key]
        highest_bidder = key
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
