import json
import os


def verify_events():
    p = r"EVENTS/"

    for e in os.scandir(p):
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
    with open("EVENTS/"+eventName+".json") as f:
        event = json.loads(f.read())
    
    bg.letter("\033[38;5;243m"
                  "humans: "+str(bg.humans_relations) +
                  "   squirels: " +str(bg.squirels_relation) +
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
            route = "yes_route"
            break

    
    bg.humans_relations += event[route]["results"]["humans_relations"]
    bg.squirels_relation += event[route]["results"]["squirels_relation"]
    bg.pigeon_loyalty += event[route]["results"]["pigeon_loyalty"]
    bg.cash  += event[route]["results"]["cash"]

    bg.letter("\033[38;5;243m"
                  "humans: "+str(bg.humans_relations) +
                  "   squirels: " +str(bg.squirels_relation) +
                  "   pigeons:" +str(bg.pigeon_loyalty)+
                  "   cash: "+str(bg.cash) + "\033[0m",
                  "",
                  event[route]["contents"], 
                  "", 
                  "")

    bg.WaitInput("press Enter to continue ")

def HumanEnding():
    pass

def squirelEnding():
    pass

def pigeonEnding():
    pass

def EndConditions(humans_relations, squirels_relation, pigeon_loyalty, cash):
    if humans_relations < 0:
        HumanEnding()
    if squirels_relation < 0:
        squirelEnding()
    if pigeon_loyalty < 0:
        pigeonEnding()