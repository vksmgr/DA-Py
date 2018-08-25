#fiels

path = "D:\PyCharmWorkspace\Projects\DA-Py\hello.txt"
f = open(path)

with open(path) as f:
    lines = [x.rstrip() for x in f]
print(lines)
f.close()