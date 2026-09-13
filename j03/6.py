a = int(input("first number: "))
b = int(input("second number: "))


# way 1:

# if a > b:
#     print(f"{a} > {b}")
# if b > a:
#     print(f"{b} > {a}")
# if a == b:
#     print(f"{a} = {b}")

# way 2:

# if a == b:
#     print(f"{a} = {b}")
# else:
#     if a > b:
#         print(f"{a} > {b}")
#     else:
#         print(f"{b} > {a}")

# way 3:

if a == b:
    print(f"{a} = {b}")
elif a > b:
    print(f"{a} > {b}")
else:
    print(f"{b} > {a}")
