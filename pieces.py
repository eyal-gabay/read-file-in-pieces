a = []

for i in open("/opt/SecLists/Discovery/Web-Content/all.txt"):
    if i.strip().isalnum() and not i.strip().isdigit():
        a.append(i.strip())

m = 100
i = 0
while 1:
    v = a[m * i:m * (i + 1)]
    if not v:
        break
    print(len(v))
    i += 1
