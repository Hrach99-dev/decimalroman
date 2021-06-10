
# def roman_to_decimal(roman_number):
#     roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     decimal = 0
#     if len(roman_number) == 1:
#         return roman[roman_number]

#     for i in range(len(roman_number) - 1):
#         if roman[roman_number[i]] < roman[roman_number[i + 1]]:
#             decimal -= roman[roman_number[i]]
#         else:
#             decimal += roman[roman_number[i]]

#     decimal += roman[roman_number[-1]]

#     return decimal


def decimal_to_roman(decimal_number):
    roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    decimal = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    
    roman_number = ''
    count = 0
    for i in range(len(decimal)):
        while decimal_number >= decimal[i]:
            decimal_number -= decimal[i]
            roman_number += roman[i]

    return roman_number


def main():

    # decimal_number = roman_to_decimal('IX')
    # print(decimal_number)
    roman_number  = decimal_to_roman(1753)
    print(roman_number)



if __name__ == '__main__':
    main()