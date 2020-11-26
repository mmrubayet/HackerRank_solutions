def climbingLeaderboard(ranked,player):
    ind = len(set(ranked))
    score = 0
    highscore = len(ranked)-1
    while score!=len(player):
        while player[score] > ranked[highscore] and highscore>-1:
            highscore-=1
            if ranked[highscore]!=ranked[highscore+1]:
                ind-=1
        if player[score] == ranked[highscore]:
            yield ind
        else:
            yield ind+1
        score+=1
input()
ranked = list(map(int,input().split()))
input()
player = list(map(int,input().split()))

print(*climbingLeaderboard(ranked,player),sep="\n")














'''
n = int(input().strip())
ranked = sorted(set(list(map(int, input().rstrip().split()))), reverse=True)
m = int(input().strip())
player = list(map(int, input().rstrip().split()))

for i in player:
    ind = len(ranked)
    while i >= ranked[ind] :
        ranked.pop()
    print(ind+1)

#     for (i = 0; i < m; ++i) {
#         scanf("%d", &score);
#         while (top && score >= stack[top]) --top;
#         printf("%d\n", top+1);


''
def climbingLeaderboard(ranked, player):
    ranked = sorted(set(ranked), reverse=True)
    for i in player:
        ind = len(ranked)

        while i >= ranked[ind] :
             ranked.pop()
             if ind < 0: break
        print(ind+1)

ranked_count = int(input().strip())
ranked = list(map(int, input().rstrip().split()))
player_count = int(input().strip())
player = list(map(int, input().rstrip().split()))

climbingLeaderboard(ranked, player)
'''
