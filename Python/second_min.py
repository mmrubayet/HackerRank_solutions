score = list(map(int, input().split()))
mn = min(score)
while min(score) == mn:
    score.remove(min(score))
print(min(score))
