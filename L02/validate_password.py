password = input()
repeat = input()

def validate(p1,p2):
    if p1 == p2:
        print("Correct")
    else:
        print("Wrong")

validate(password, repeat)
