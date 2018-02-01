import list.txt

from random import randint

num = randint(1,1383)

i=0
   List=[""]
   for Line in inFile:
      List[i]=Line.split(",")
      i+=1

print(List[num])
