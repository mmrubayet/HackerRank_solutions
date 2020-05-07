def count_substring(string, substring):
    sum_ = 0
    for i in range(len(string)-len(substring)+1):
        if string[i:i+len(substring)] == substring:
            sum_ += 1
    return sum_

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
