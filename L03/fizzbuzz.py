# ARMSTRONG CF-4 L03 - Project: FizzBuzz
# The finished program from the lesson videos (L03 V1 + V2), as Eng. Mazen Nasr builds it.
# Run it, type a number (for example 20) and press Enter.
# Multiples of 3 and 5 print FIZZBUZZ, multiples of 3 print FIZZ, multiples of 5 print BUZZ,
# the other even numbers are skipped and the other odd numbers are printed.
# Remember: the order of the conditions matters - the combined check (3 and 5) must come first.

n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    elif i % 2 == 0:
        continue
    else:
        print(i)
