import collections



x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
x3,y3 = map(int, input().split())
xl=[x1,x2,x3]
yl=[y1,y2,y3]

cxl = collections.Counter(xl)
cyl = collections.Counter(yl)
print(xl,yl)