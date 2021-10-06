import re
class Statistic:
    def __init__(self,filename):
        self.filename=filename
    def process(self):
        f=open(self.filename,"r")
        text=f.read()
        symbols=len(text)-text.count('\n')-text.count(' ')
        words=len(text.split())
        sentences=len(re.split(r'[!\?\.]+',text))-1
        f.close()
        return symbols,words,sentences
A=Statistic("test.txt")
sym,wrd,snt=map(str,A.process())
print("Symbols:" + sym,"Words:" + wrd, "Sentences:" + snt)