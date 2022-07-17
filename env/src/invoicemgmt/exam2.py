s = list(input())
t = list(input())

def isEqual(s,t):
    s = s.sort()
    t = t.sort()
    # print(s)
    # print(t)
    if s==t:
        return True
    else:
        return False

count = 0
for i in range(len(s)):
    if isEqual(s,t):
        continue
    else:
        s.pop(0)
        t.pop(0)
        count = count+2
print(count)

