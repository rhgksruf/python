# a = [1,2,3,4,5]
# b = []
# for i in a:
#     b.append(i**2)
# print(b)

# c = ["hello","world","python","programming"]
# d = []
# for i in c:
#     d.append(len(i))
# print(d)

a = ["apple","banana","cherry","date"]
b = []
for i in a:
    b.append(a.extend(i))
print(b)





