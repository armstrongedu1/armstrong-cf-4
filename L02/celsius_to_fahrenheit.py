# The following equation is used to calculate the Fahrenheit value: 9/5 * celsius + 32

cel = float(input())

def cel_to_fah(degree):
    fah = 9/5 * degree + 32
    return fah

print(cel_to_fah(cel))
