# Examples:
#
# Input : 55
# Output : 55  in Binary :  0b110111
#          55 in Octal :  0o67
#          55  in Hexadecimal :  0x37

# Input : 282
# Output : 282  in Binary :  0b100011010
#          282 in Octal :  0o432
         # 282  in Hexadecimal :  0x11a

# Python program to convert decimal to binary,
# octal and hexadecimal

# Function to convert decimal to binary
def decimal_to_binary(dec):
    decimal = int(dec)

    # Prints equivalent decimal
    print(decimal, " in Binary : ", bin(decimal))
    print(decimal, " in Binary : ", bin(decimal)[2:])


# Function to convert decimal to octal
def decimal_to_octal(dec):
    decimal = int(dec)

    # Prints equivalent decimal
    print(decimal, "in Octal : ", oct(decimal))
    print(decimal, "in Octal : ", oct(decimal)[2:])



# Function to convert decimal to hexadecimal
def decimal_to_hexadecimal(dec):
    decimal = int(dec)

    # Prints equivalent decimal
    print(decimal, " in Hexadecimal : ", hex(decimal))
    print(decimal, " in Hexadecimal : ", hex(decimal)[2:])


# Driver program
dec = 32
decimal_to_binary(dec)
decimal_to_octal(dec)
decimal_to_hexadecimal(dec)

# Output:

# 32 in Binary: 0b100000
# 32 in Octal: 0o40
# # 32 in Hexadecimal: 0x20