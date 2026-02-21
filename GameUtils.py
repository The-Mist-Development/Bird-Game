import json
import os
import random


def verify_events(dirc):

    for e in os.scandir(dirc):
        if e.is_file():
            with open(e.path) as f:
                event = json.loads(f.read())#
                for line in event["opening"]["contents"]:
                    if len(line) > 110:
                        raise RuntimeError("Line in "+e.path+" Event content section is longer than 110 (it is "+str(len(line))+")")
                for line in event["yes_route"]["contents"]:
                    if len(line) > 110:
                        raise RuntimeError("Line in "+e.path+" Event content section is longer than 110 (it is "+str(len(line))+")")
                for line in event["no_route"]["contents"]:
                    if len(line) > 110:
                        raise RuntimeError("Line in "+e.path+" Event content section is longer than 110 (it is "+str(len(line))+")")

to_you = "To: King PIGEON (YOU)"
def do_event(eventName,bg):
    with open(eventName+".json") as f:
        event = json.loads(f.read())
    
    bg.letter("\033[38;5;243m"
                  "humans: "+str(bg.humans_relations) +
                  "   squirrels: " +str(bg.squirrels_relation) +
                  "   pigeons:" +str(bg.pigeon_loyalty)+
                  "   cash: "+str(bg.cash) + "\033[0m",
                  to_you,
                  event["opening"]["contents"], 
                  event["opening"]["signoff"]["regards"], 
                  event["opening"]["signoff"]["signature"])

    route = "unknown_route"
    while True:
        input_ = bg.WaitInput("Enter y to "+event["opening"]["option tags"]["y"]+"\n"+
                     "Enter n to "+event["opening"]["option tags"]["n"])

        if input_ =="y" or input_ == "Y":
            route = "yes_route"
            break
        elif input_ =="n" or input_ == "N":
            route = "no_route"
            break
    
    for flag in event[route]["results"]["new_flags"]:
        bg.flags.add(flag)

    bg.humans_relations += event[route]["results"]["humans_relations"]
    bg.squirrels_relation += event[route]["results"]["squirrels_relation"]
    bg.pigeon_loyalty += event[route]["results"]["pigeon_loyalty"]
    bg.cash  += event[route]["results"]["cash"]

    bg.letter("\033[38;5;243m"
                  "humans: "+str(bg.humans_relations) +
                  "   squirrels: " +str(bg.squirrels_relation) +
                  "   pigeons:" +str(bg.pigeon_loyalty)+
                  "   cash: "+str(bg.cash) + "\033[0m",
                  30*" " + "\033[38;5;243m"
                  "        "+("+" if event[route]["results"]["humans_relations"] >=0 else "" )+str(event[route]["results"]["humans_relations"]) +
                  "             "+("+"if event[route]["results"]["squirrels_relation"] >=0 else "" )+str(event[route]["results"]["squirrels_relation"]) +
                  "            "+("+"if event[route]["results"]["pigeon_loyalty"] >=0 else "" )+str(event[route]["results"]["pigeon_loyalty"])+
                  "          "+("+" if event[route]["results"]["cash"] >=0 else "" )+str(event[route]["results"]["cash"]) + "\033[0m",
                  event[route]["contents"], 
                  "", 
                  "")

    bg.WaitInput("press Enter to continue ")


def do_random_event(bg):
    events = [e for e in os.scandir("EVENTS/Random")]

    while True:
        e = random.choice(events)
        with open(e.path) as f:
            event = json.loads(f.read())

        run = True
        for flag in event["prerequisite flags"]:
            if not flag in bg.flags:
                run = False

        if run == True:
            do_event(e.path.split(".")[0],bg)
            break;

def HumanEnding(bg):
    do_event("EVENTS/Special/HumanDeath",bg) 

def squirelEnding(bg):
    do_event("EVENTS/Special/SquirrelDeath",bg) 

def pigeonEnding(bg):
    do_event("EVENTS/Special/PigeonDeath",bg) 

def EndConditions(bg):
    if bg.humans_relations < 0:
        HumanEnding(bg)
    elif bg.squirrels_relation < 0:
        squirelEnding(bg)
    elif bg.pigeon_loyalty < 0:
        pigeonEnding(bg)