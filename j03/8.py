a = 10
b = 40
c = 30

if a < b:
    if b < c:
        print(1)
    else:
        print(2)

# if a > b and b < c:
#     print(1)
# elif a < b and b > c:
#     print(2)
# elif a < b and b < c:
#     print(3)

if (a < b or b < c) and 0:
    print(1)
elif a > b or b > c:
    print(2)
