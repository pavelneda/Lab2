import re,string,os
class Statistic:
    def __init__(self,filename):
        if not isinstance(filename,str):
            raise FileNotFoundError
        self.__filename=filename
    def symbols(self):
        if not os.path.isfile(self.__filename):
            raise FileNotFoundError
        f=open(self.__filename)
        text=f.read()
        symbols=len(text)-len(string.whitespace)
        f.close()
        return symbols
    def words(self):
        if not os.path.isfile(self.__filename):
            raise FileNotFoundError
        f=open(self.__filename)
        text=f.read()
        words=len(re.split(r'[,\ ]+',text))
        f.close()
        return words
    def sentences(self):
        if not os.path.isfile(self.__filename):
            raise FileNotFoundError
        f=open(self.__filename)
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
except TypeError:
    print("Type error")
except NameError:
    print("Name error")