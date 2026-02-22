from BIRDGameUI import *
from GameUtils import *


verify_events(r"EVENTS/Random")
verify_events(r"EVENTS/Special")

bg = BIRBGAME() 

bg.letter("","To: Noble PIGEON (YOU)",["Hello my friend,","","The Kelvingrove is in disarray, you are the only pigeon i know who can restore order.","Please return and take your rightful place as King of the pigeons"], "yours most dearly,", "Lord Kelvin")

bg.WaitInput("press Enter to continue")

bg.letter("","I will not disappoint...",["","","","\033[38;5;243m You Must keep All Values between  0 - 100 \033[0m"], "Internal Dialog", "")

bg.WaitInput("press Enter to BEGIN GAME")

bg.humans_relations, bg.squirrels_relation, bg.pigeon_loyalty, bg.cash = 50,50,50,50
bg.flags = set(["ART GALLERY"])

while True:
    EndConditions(bg)
    if "RESTART" in bg.flags:
        bg.humans_relations, bg.squirrels_relation, bg.pigeon_loyalty, bg.cash = 50,50,50,50
        bg.flags = set(["resurrected","ART GALLERY"])
    elif "EXIT" in bg.flags:
        exit()

    
    do_random_event(bg) #do_event("EVENTS/Random/<EVENT YOU WANT TO CALL>",bg) # to test events :)