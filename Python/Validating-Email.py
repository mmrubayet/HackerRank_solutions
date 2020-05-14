def fun(email):
    # return True if s is a valid email, else return False
    s = True
    try:
        username, url = email.split("@")
        website, extension = url.split(".")
    except ValueError:
        s = False
        return s

    if not username.replace("-", "").replace("_", "").isalnum():
        s = False
    elif not website.isalnum():
        s = False
    elif len(extension) > 3:
        s = False

    return s

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
