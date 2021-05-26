# Factorail
def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f

# unique
def unique(l):
    li = []
    for i in l:
        if l.count(i) == 1:
            li.append(i)
    print(li)
    
# duplicates    
def duplicates(l):
    li = []
    for i in l:
        if i not in li:
            li.append(i)
    print(li)

