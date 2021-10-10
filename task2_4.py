import re
class Statistic:
    def __init__(self,filename):
        if type(filename)==str:
            self.filename=filename
        else:
            raise FileNotFoundError
    def symbols(self):
        f=open(self.filename,"r")
        text=f.read()
        symbols=len(text)-text.count('\n')-text.count(' ')
        f.close()
        return symbols
    def words(self):
        f=open(self.filename,"r")
        text=f.read()
        words=len(text.split())
        f.close()
        return words
    def sentences(self):
        f=open(self.filename,"r")
        text=f.read()
        sentences=len(re.split(r'[!\?\.]+',text))-1
        f.close()
        return sentences
try:
    A=Statistic("test.txt")
    sym=str(A.symbols())
    wrd=str(A.words())
    snt=str(A.sentences())
    print("Symbols:" + sym,"Words:" + wrd, "Sentences:" + snt)
except FileNotFoundError:
    print("File not found")
except NameError:
    print("Name error")