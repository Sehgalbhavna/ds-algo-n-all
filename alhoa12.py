s = "1:2, 5:10, 11:20"
l = s.split(",")
print(l)
r = []
stack = set()
for i in l:
    c = i.strip()
    print(c.sort())
    stack.add(c)
    print(stack.sort(key=lambda x: x[0]))
print(r)