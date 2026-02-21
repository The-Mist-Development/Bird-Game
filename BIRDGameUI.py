import Terminal as TR

class BIRBGAME(TR.Terminal):

    def __init__(self):
        TR.Terminal.__init__(self)
        humans_relations, squirels_relation, pigeon_loyalty, cash = 0,0,0,0

    def letter(self,sender_addressline1,sender_addressline2,contents,signoff,sig):
        self.clear()
        
        letter_box = self.text_box(3,25,10,120)

        letter_box.type(1, sender_addressline2,speed = 0.07)

        full_letter,indices = ([
                   " "*30+ sender_addressline1,
                   sender_addressline2 ],[0,1])
        
        full_letter,indices = (full_letter+contents,indices+[6+x for x in range(len(contents))])
       
        full_letter,indices = (full_letter + [
                  " "*60 + signoff,
                  " "*60 + sig],indices+[19,21])

        letter_box.print(indices,*full_letter)

    def WaitInput(self,prompt):
        prompt = "\033[38;5;243m"+prompt+"\033[0m"
        input_prompt_box = self.text_box(26,28,10,120)
        prompt = prompt.split("\n")+[" "]
        input_prompt_box.print([0,1],*prompt)
        self.update_display()
        return input()