from BIRDGameUI import *
from GameUtils import *



bg = BIRBGAME() 

# bg.letter("To: Noble PIGEON (YOU)","",["Hello my friend,","","The Kelvingrove is in disarray, you are the only pigeon i know who can restore order. Please return and take your rightful place as King of the pigeons"], "yours most dearly,", "Lord Kelvin")

# bg.WaitInput("press Enter to continue")

# bg.letter("I will not disappoint...","",["","",], "Internal Dialog", "")

# bg.WaitInput("press Enter to BEGIN GAME")

verify_events(r"EVENTS/Random")
verify_events(r"EVENTS/Special")

bg.humans_relations, bg.squirrels_relation, bg.pigeon_loyalty, bg.cash = 100,100,100,100
bg.flags = set()

while True:
    EndConditions(bg)
    if "RESTART" in bg.flags:
        bg.humans_relations, bg.squirrels_relation, bg.pigeon_loyalty, bg.cash = 100,100,100,100
        bg.flags = set("resurrected")
    elif "EXIT" in bg.flags:
        exit()

    if bg.cash < 0:
           do_event("EVENTS/Special/in_debt",bg) 
    else:
        do_random_event(bg) #do_event("EVENTS/Random/<EVENT YOU WANT TO CALL>",bg) # to test events :)