'''
    Задача 2 Yandex cup 2021
'''

class Tile:
    def __init__(self, ul,ur, dl, dr):
        self.ul = ul
        self.ur = ur
        self.dl = dl
        self.dr = dr
    def d0(self):
        return ([self.ul, self.ur, self.dl, self.dr])
    def d90(self):
        return ([self.dl, self.ul, self.dr, self.ur])
    def d180(self):
        return ([self.dr, self.dl, self.ur, self.ul])
    def d270(self):
        return ([self.ur, self.dr, self.ul, self.dl])

def print_T(a):
    print(a[0], a[1])
    print(a[2], a[3])

class Stack:
    def __init__(self, tile, nextt):
        self.tile = tile
        self.next = nextt

class OneLinkedList:
    def __init__(self, last, tile, nextt):
        self.last = last
        self.tile = tile
        self.next = nextt

def parseTile(f, s):
    tiles = []
    while (len(s) > 0):
        tile = Tile(f[0], f[1], s[0], s[1])
        f = f[2:]
        s = s[2:]
        tiles.append(tile)
    return(tiles)

def checkTiles(t1, t2):
    t1L = t1.d0()
    if (t1L == t2.d0()):
        return True
    if (t1L == t2.d90()):
        return True
    if (t1L == t2.d180()):
        return True
    if (t1L == t2.d270()):
        return True
    return False

k = int(input())
headList = OneLinkedList(None, None, None)
curr = headList
for i in range(k):
    a = input()
    b = input()
    tile = Tile(a[0], a[1], b[0], b[1])
    curr.tile = tile
    last = curr
    curr = OneLinkedList(None, None, None)
    last.next = curr
    curr.last = last
curr = headList
while curr.next != None:
    print_T(curr.tile.d0())
    curr = curr.next
n,m = input().split()
n = int(n)
m = int(m)
if (n * m > k * 4):
    print("NO")
else:
    headStack = Stack(None, None)
    curr = headStack
    for i in range(n//2):
        first = input()
        second = input()
        tiles = parseTile(first, second)
        for i in tiles:
            curr.tile = i
            last = curr
            curr = Stack(None, None)
            last.next = curr
    curr = headStack
    while curr.next != None:
        print_T(curr.tile.d0())
        curr = curr.next
    currS = headStack
    flag = False
    while currS.next != None:
        picture = currS.tile
        currL = headList
        while currL.next != None:
            if checkTiles(picture, currL.tile) == True:
                currS = currS.next
                if currL.last != None:
                    currL.last.next = currL.next
                if currL.next != None:
                    currL.next.last = currL.last
                flag = True
                break
            currL = currL.next
        if flag == False:
            break
    if flag == False:
        print("NO")
    else:
        print("YES")
        
