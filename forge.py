import os 
import time 




print "Welcome to Mateo's"
print "What's the name on the reservation?"

player_one = raw_input()
os.system("clear")

if player_one == "Mateo":
    print "Oh! Sorry Mr. Mateo, I didn't recognize you. "
    print "Check out today's High Scores"
    time.sleep(3)
    clock = 3
    while clock >-1:
        time.sleep(1)
        os.system("clear")
        print(clock)
        clock -=1
    os.system("clear")
    print "\t\t HIGH SCORES(9/26/2018) \nBitcoin - $4,521 \nEthereum - $133 \nDogecoin - $0.002"
else:
    print """ "%s", we've been expecting you.
    Follow me.
    """ % player_one
    time.sleep(3)
    clock = 3
    while clock >-1:
        time.sleep(1)
        os.system("clear")
        print(clock)
        clock -=1
    os.system("clear")
    print "\t\tLevel 1"
    time.sleep(3)

print "\n\n\n\nUnder Construction. \nCome back soon."
