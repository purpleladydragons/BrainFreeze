import sys

class MyArray():
    def __init__(self):
        self.array = [0,0,0,0,0,0,0,0]
        self.pos = 0
    def myget(self):
        return self.array[self.pos]
    def myset(self,val):
        self.array[self.pos] = val
    def moveright(self):
        self.pos += 1
    def moveleft(self):
        self.pos -= 1

myarray = MyArray()
def myeval(stuff):
    global myarray
    count = 0
    if stuff[0] == 'while':
        while myarray.myget() != 0:
            myeval(stuff[1])
    while count < len(stuff):
        if stuff[count] == '[':
            myind = count
            myend = stuff[count:].index(']')+len(stuff[:count])
            newstuff = stuff[myind+1:myend]
            del stuff[myind:myend]
            myeval(['while',newstuff])
        elif stuff[count] == ']':
            raise SyntaxError("wroooooooooong")
        elif stuff[count] == '+':
            myarray.myset(myarray.myget()+1)
        elif stuff[count] == '-':
            myarray.myset(myarray.myget()-1)
        elif stuff[count] == '>':
            myarray.moveright()
        elif stuff[count] == '<':
            myarray.moveleft()
        elif stuff[count] == '.':
            sys.stdout.write(chr(myarray.myget()))
            #print chr(myarray.myget())
        elif stuff[count] == ',':
            inp = raw_input("")[0]
            myarray.myset(ord(inp))
        count += 1



def parse(tokens):
    parseable = []
    for i in range(len(tokens)):
        char = tokens[i]
        parseable.append(char)
    return parseable


if len(sys.argv) < 2:
    print 'Usage:python brainfreeze.py yourbffile'
    quit()
with open(sys.argv[1]) as mystring:
    prog = mystring.read()
    proglist = []
    proglist = [char for char in prog if char in '+-<>[],.']
    myeval(parse(proglist))
