from collections import OrderedDict
od = OrderedDict()
for _ in range(int(input())):
    *item, quantity = input().split()
    try:
        od[' '.join(item)] += int(quantity)
    except KeyError:
        od[' '.join(item)] = int(quantity)
for item, quantity in od.items():
    print(item, quantity)
