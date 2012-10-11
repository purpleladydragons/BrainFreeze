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
        while myarray.myget() > 0:
            myeval(stuff[1])
    while count < len(stuff) and stuff[0] != 'while':
        if stuff[count] == '[':
            leftcount = 1
            rightcount = 0
            stptr = count+1
            while leftcount > rightcount:
                if stuff[stptr] == '[':
                    leftcount += 1
                if stuff[stptr] == ']':
                    rightcount += 1
                stptr += 1
                if stptr >= len(stuff) and leftcount > rightcount: 
                    print "Missing closing ]"
                    quit()
                
            myind = count
            myend = stptr
            newstuff = stuff[myind+1:myend-1] #stptr is guaranteed to inc by 1 after equality; exlusive slicing 
            #del stuff[myind:myend]
            count += len(stuff[myind:myend])-1
            myeval(['while',newstuff])
        elif stuff[count] == ']':
            print stuff
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
