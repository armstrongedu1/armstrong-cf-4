def my_func():
    name = input()
    age = int(input())

    if age <= 10:
        print("welcome " + name)
    else:
        print("Sorry " + name)

for i in range(4):
    my_func()
