from BIRDGameUI import *
from GameUtils import *



bg = BIRBGAME() 

# bg.letter("To: Wandering PIGEON (YOU)","",["Hello lord.","","The Kelvingrove is in disarray, please come back; you are our KING!!"], "yours dearly,", "PEASANT PIGEON")

# bg.WaitInput("press Enter to continue")

# bg.letter("my people need me...","",["","",], "Internal Dialog", "")

# bg.WaitInput("press Enter to BEGIN GAME")

verify_events()


bg.humans_relations, bg.squirels_relation, bg.pigeon_loyalty, bg.cash = 100,100,100,-10
while True:
    do_event("standardEvent",bg)

    # if cash < 0:
    #     bg.letter("\033[38;5;243m"
    #               "humans: "+str(humans_relations) +
    #               "   squirels: " +str(squirels_relation) +
    #               "   pigeons:" +str(pigeon_loyalty)+
    #               "   cash: "+str(cash) + "\033[0m",
    #               to_you,
    #               ["Hello mr PIG-eon.","","You have debts, i assume you wont mind if we collect some interest."], 
    #               "yours dearly,", 
    #               "Big gun, Loan piranas Ltd.")

    #     bg.WaitInput("press Enter to continue (your subjects property was pillaged)")