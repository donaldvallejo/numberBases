#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    # digits_and_letters = string.digits + string.ascii_letters 

    digits = digits[::-1]
    sum = 0
    for i in range(len(digits)):
        # result = int(digits[i]) * base ** i
        ind = '0123456789abcdef'.index(digits[i])
        #print("inddddd:::::::",ind)
        result = ind * base ** i
        sum += result
    return sum

    # TODO: Decode digits from binary (base 2)
    # ...
    # TODO: Decode digits from hexadecimal (base 16)
    # ...
    # TODO: Decode digits from any base (2 up to 36)
    # ...


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

# loop to do the repeated division
# get the remainders and divisors
# save the remainders
# return the final number result as a string
# somehow deal with hex digits

#while
    #divisor = number / base
    # remainder = ??
    digits_and_letters = string.digits + string.ascii_letters 
    # print(digits_and_letters)
    new_number = number
    final_digits = ""
    while new_number != 0:
        remainder = new_number % base
        if base == 16:
            remainder = digits_and_letters[remainder]
        # print("remainder", remainder)
        new_number = new_number // base
        # print("divisor", new_number)
        final_digits += str(remainder)
    # print(final_digits)
    return final_digits[::-1]

# string.digits + string.ascii_letters 
# new_number = numbers
# final_digits = ""
# while new_number != 0:

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...
    base10result = decode(digits, base1)
    finalresult = encode(base10result, base2)
    return finalresult

    # string = decode(digits, base1)
    # return encode(int(string), base2)

print(convert("1000", 2, 16))
# print(finalresult)

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


# if __name__ == '__main__':
#     main()
    # print(encode(12, 2)) # expect to see 1100
    # print(encode(64206, 16)) # face

    print(convert("101", 2, 16))
    print(convert("1010", 2, 16))