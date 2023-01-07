# Literaly follows the rails rule to arrange the string,
# creating a list for each rail and inserting the letters
# in the corresponding rail, concatenating all rails in the end
def encode_rail_fence_cipher(string, n):
    rails = [""] * n
    index = 0
    up = True
    for letter in string:
        rails[index] += letter
        if index == n - 1:
            up = False
        elif index == 0:
            up = True
        if up:
            index += 1
        else:
            index -= 1
    return "".join(rails)


# Note that each rail is composed by all letters that were in
# indexes that had the same module (remain of division).
# For the first rail the module would be 0, for the second
# it would be 1 or new_n-1, where new_n is the number of letters
# used for a pattern be seen in the rails
#
# example:
# ABCDEFGHIJ, n=3
# A    E   I      -> index mod4 = 0        ([A, E, I]             -> [0, 4, 8] % 4 = 0)
# B  D F H J     -> index mod4 = 1 or 3   ([B, D, F, H, J] -> [1, 3, 5, 7, 9] % 4 = 1 or 3)
#  C    G        -> index mod4 = 2        ([C, G]                   -> [2, 6] % 4 = 2)
#
# new_n = 4 (ABCD) (EFGH) (IJ--)
def decode_rail_fence_cipher(string, n):
    size = len(string)
    new_n = 2 * (n - 1)

    message = [""] * size
    indexes = []
    for k in range((new_n // 2) + 1):
        modules = [k, new_n - k]
        indexes += numbers_with_module(size, new_n, modules)
    count = 0
    for index in indexes:
        message[index] = string[count]
        count += 1
    return "".join(message)


# Returns a list with all numbers that have module in the "module"
# variable (a list) and is smaller than "number" variable
def numbers_with_module(number, divisor, module):
    numbers = []
    for n in range(number):
        if n % divisor in module:
            numbers.append(n)
    return numbers
