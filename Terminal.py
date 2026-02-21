import shutil
from threading import Thread
from time import sleep
import os
  
class Terminal():

    def __init__(self):
        self.size = shutil.get_terminal_size()
        self.__clear_terminal()
        
        self.width = self.size.columns
        self.height = self.size.lines-1

        self.text = [[" " for _ in range(self.size.columns)] for _ in range(self.size.lines-1)]

        self.calling = None
        self.__dependencies = []
        self.__changes_made = False

        self.debug = False
        self.typing = True

        t = Thread(target=self.__Keeper)
        t.daemon = True
        t.start()

    def __Keeper(self):
        while True:
            sleep(0.01)

            if self.calling != None:
                self.calling()
            
            if self.__changes_made:
                self.__changes_made = False

                self.__clear_text()
                for item in self.__dependencies:
                    item.draw()

                self.update_display()

    def update_display(self):
        if not self.debug:
            self.__clear_terminal()

        out = []
        for line in self.text:
            out.append("".join(line)[:self.size.columns])
        print("\n".join(out), flush=True)
                
    def __clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __clear_text(self):
        self.text = [[" " for x in range(self.size.columns)] for x in range(self.size.lines-1)]

    def clear(self):
        self.__dependencies = []
        self.change_made()

    def change_made(self):
        self.__changes_made = True

    def text_box(self,line_start,line_end,start,end, left = "", right = "",top = "", bottom = ""):
        new_text_box = Text_box(self,line_start,line_end,start,end,left,right,top,bottom)
        self.__dependencies.append(new_text_box)
        
        return new_text_box

    def remove_text_box(self,text_box):
        self.__dependencies.remove(text_box)

class Text_box:

    def __init__(self,terminal,line_start,line_end,start,end,left,right,top,bottom):
        self.terminal = terminal 

        self.line_start = line_start
        self.line_end = line_end
        self.start = start
        self.end = end
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

        self.text = ["" for _ in range(self.line_end - self.line_start)]


    def __call__(self,line,text):
    

        if len("".join([s for s in list(text) if s.isalnum()])) > self.end-self.start:
            raise RuntimeError(f"Too wide for box: {text}"+ " MAX WIDTH = "+str(self.end-self.start))
        if line > self.line_end - self.line_start:
            raise RuntimeError("Too tall for box")

        self.text[line] = text
        self.terminal.change_made()

    def print(self,lines,*texts):
        for i in range(len(lines)):
            self(lines[i],texts[i])
            self.terminal.change_made()

    def type(self,line,text,speed = 0.12):
        if self.terminal.typing:
            self.text[line] = ""

            self.__text = text
            self.__line = line
            self.__speed = speed

            t = Thread(target=self.__typer)
            t.start()
            t.join()
        else:
            self(line,text)

    def clear(self):
        self.text = ["" for x in range(self.line_end - self.line_start)]
        self.terminal.change_made()


    def __typer(self):
        for char in self.__text:
            
            self.text[self.__line] += char
            self.terminal.change_made()

            if char != " ":
                sleep(self.__speed)

    def draw(self):
        if self.top != "":
            for columns in range(self.start+1,self.end):
                self.terminal.text[self.line_start][columns] = self.top

        if self.bottom != "":
            for columns in range(self.start+1,self.end):
                self.terminal.text[self.line_end][columns] = self.bottom

        if self.left != "":
            for line in range(self.line_start,self.line_end+1):
                self.terminal.text[line][self.start] = self.left

        if self.right != "":
            for line in range(self.line_start,self.line_end+1):
                self.terminal.text[line][self.end] = self.right

        for line in range(self.line_end-self.line_start):
            for col in range(len(self.text[line])):
                if col< self.end-self.start-1:

                    self.terminal.text[self.line_start+line][self.start+col+1] = self.text[line][col]

    
