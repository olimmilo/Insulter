from random import randint

name = input("Say your name you idiot, with more than 2 letters or else: ")

alphabet = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 'K' : 10, 'L' : 11, 'M' : 12, 'N' : 13, 'O' : 14, 'P' : 15, 'Q' : 16, 'R' : 17, 'S' : 18, 'T' : 19, 'U' : 20, 'V' : 21, 'W' : 22, 'X' : 23, 'Y' : 24, 'Z' : 25, 'a' : 26, 'b' : 27, 'c' : 28, 'd' : 29, 'e' : 30, 'f' : 31, 'g' : 32, 'h' : 33, 'i' : 34, 'j' : 35, 'k' : 36, 'l' : 37, 'm' : 38, 'n' : 39, 'o' : 40, 'p' : 41, 'q' : 42, 'r' : 43, 's' : 44, 't' : 45, 'u' : 46, 'v' : 47, 'w' : 48, 'x' : 49, 'y' : 50, 'z' : 51}


nlistp = list(name)
nlist=[]

print((alphabet[nlistp[1]])%13820)


i = 0
p = 0
while i <= (len(nlistp)-1):
    let=nlistp[i]
    nlist.append(alphabet[let])
    i=i+1

num = nlist[p]
p = 1

while p <= (len(nlist)-1):
    num = num*nlist[p]
    p=p+1

num = num%13820

List = open("list.txt").readlines()

print("")
print(name, "you are a",List[num])
