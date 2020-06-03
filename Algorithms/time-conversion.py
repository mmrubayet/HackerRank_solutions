t = input().strip()
h = int(t[0:2])
m = int(t[3:5])
s = int(t[6:8])
f = t[-2:]
if f == 'PM' and h != 12:
    h += 12
if f == 'AM' and h == 12:
    h = 0
print(('%02d:%02d:%02d') % (h, m, s))
