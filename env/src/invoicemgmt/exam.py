
x = []
y = []

m = int(input())
a = input()
a = list(a)
a = [int(i) for i in a]
# print(a)

n = int(input())
b = input()
b = list(b)
b = [int(i) for i in b]
# print(b)



c = a+b
for i in c:
    if i%2==1:
        x.append(i)
x.sort()

for i in c:
    if i%2==0:
        y.append(i)
y.sort(reverse=True)
c = x+y


def middle_num(lst):
    l = len(lst)
    if l%2==0:
        print(lst[l//2-1]," ",lst[l//2])
    else:
        print(lst[(l//2)])

middle_num(c)




