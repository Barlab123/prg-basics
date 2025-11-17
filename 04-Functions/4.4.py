###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    if number < 0:
        abs(number)
    else:
        string = str(number)
        for char in string:
            int(string)
            suma += char 
    return suma

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')