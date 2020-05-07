if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    q_score = student_marks[query_name]
    print('{:.2f}' .format(sum(q_score)/len(q_score)))

    # ln, num = 0, 0
    # for x in student_marks:
    #     if x == query_name:
    #         ln = len(student_marks[x])
    #         for i in range(ln):
    #             num += student_marks[x][i]
    #         print('{:.2f}' .format(num/ln))
