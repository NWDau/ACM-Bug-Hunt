line = input();
line = line.splt()
e = int(line[1])
f = int(line[2])
c = int(line[3])

t = f+f
d = 0
while(t<= c):
    b=t//c
    t=t%c
    t+=b
    d+=b
print(d);
