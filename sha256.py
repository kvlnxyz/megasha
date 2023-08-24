initial_hash_values = [
    "01101010000010011110011001100111", # a
    "10111011011001111010111010000101", # b
    "00111100011011101111001101110010", # c
    "10100101010011111111010100111010", # d
    "01010001000011100101001001111111", # e
    "10011011000001010110100010001100", # f
    "00011111100000111101100110101011", # g
    "01011011111000001100111100011001", # h
]

constants = ['01000010100010100010111110011000', '01110001001101110100010010010001', '10110101110000001111101111001111', '11101001101101011101101110100101', '00111001010101101100001001011011', '01011001111100010001000111110001', '10010010001111111000001010100100', '10101011000111000101111011010101', '11011000000001111010101010011000', '00010010100000110101101100000001', '00100100001100011000010110111110', '01010101000011000111110111000011', '01110010101111100101110101110100', '10000000110111101011000111111110', '10011011110111000000011010100111', '11000001100110111111000101110100', '11100100100110110110100111000001', '11101111101111100100011110000110', '00001111110000011001110111000110', '00100100000011001010000111001100', '00101101111010010010110001101111', '01001010011101001000010010101010', '01011100101100001010100111011100', '01110110111110011000100011011010', '10011000001111100101000101010010', '10101000001100011100011001101101', '10110000000000110010011111001000', '10111111010110010111111111000111', '11000110111000000000101111110011', '11010101101001111001000101000111', '00000110110010100110001101010001', '00010100001010010010100101100111', '00100111101101110000101010000101', '00101110000110110010000100111000', '01001101001011000110110111111100', '01010011001110000000110100010011', '01100101000010100111001101010100', '01110110011010100000101010111011', '10000001110000101100100100101110', '10010010011100100010110010000101', '10100010101111111110100010100001', '10101000000110100110011001001011', '11000010010010111000101101110000', '11000111011011000101000110100011', '11010001100100101110100000011001', '11010110100110010000011000100100', '11110100000011100011010110000101', '00010000011010101010000001110000', '00011001101001001100000100010110', '00011110001101110110110000001000', '00100111010010000111011101001100', '00110100101100001011110010110101', '00111001000111000000110010110011', '01001110110110001010101001001010', '01011011100111001100101001001111', '01101000001011100110111111110011', '01110100100011111000001011101110', '01111000101001010110001101101111', '10000100110010000111100000010100', '10001100110001110000001000001000', '10010000101111101111111111111010', '10100100010100000110110011101011', '10111110111110011010001111110111', '11000110011100010111100011110010']


def string_to_binary(input):
    full_str = ""

    for x in input:
        full_str += format(ord(x), '08b')

    return full_str

def preprocess(input):
    input_len = len(input)
    input_len_binary = "01100000" # bin(input_len)

    input += "1"
    for x in range(351):
        input += "0"

    for x in range(7):
        input += "00000000"

    input += input_len_binary

    return input

def rotation(binary, amount):
    start = binary[32-amount:32]
    end = binary[0:32-amount]
    return start + end

def shift(binary, amount):
    start = "0" * amount
    end = binary[0:32-amount]
    return start + end

def words(input):
    blocks = []
    for x in range(16):
        slice = input[x*32:x*32+32]
        blocks.append(slice)

    return blocks

def sigma_zero(input):
    one = rotation(input, 7)
    two = rotation(input, 18)
    three = shift(input, 3)
    output = ""
    for x in range(32):
        addition = int(one[x]) + int(two[x]) + int(three[x])
        output += str(addition % 2)
    return output

def sigma_one(input):
    one = rotation(input, 17)
    two = rotation(input, 19)
    three = shift(input, 10)
    output = ""
    for x in range(32):
        addition = int(one[x]) + int(two[x]) + int(three[x])
        output += str(addition % 2)
    return output

def add_binary(one, two, three, four):
    value_int = 0
    for x in range(32):
        value_int += int(one[31-x]) * 2**x

    for x in range(32):
        value_int += int(two[31-x]) * 2**x

    for x in range(32):
        value_int += int(three[31-x]) * 2**x

    for x in range(32):
        value_int += int(four[31-x]) * 2**x

    value_int = value_int % (2**32)
    value_binary = bin(value_int)[2:]
    value_binary = (32-len(value_binary)) * "0" + value_binary

    return value_binary

def add_six_binary(h, alpha_e, che, k, w):
    value_int = 0
    for x in range(32):
        value_int += int(h[31-x]) * 2**x

    for x in range(32):
        value_int += int(alpha_e[31-x]) * 2**x

    for x in range(32):
        value_int += int(che[31-x]) * 2**x

    for x in range(32):
        value_int += int(k[31-x]) * 2**x

    for x in range(32):
        value_int += int(w[31-x]) * 2**x

    value_int = value_int % (2**32)
    value_binary = bin(value_int)[2:]
    value_binary = (32-len(value_binary)) * "0" + value_binary

    return value_binary

def add_two_binary(one, two):
    value_int = 0
    for x in range(32):
        value_int += int(one[31-x]) * 2**x

    for x in range(32):
        value_int += int(two[31-x]) * 2**x

    value_int = value_int % (2**32)
    value_binary = bin(value_int)[2:]
    value_binary = (32-len(value_binary)) * "0" + value_binary

    return value_binary


def computation(input):
    w = input
    for x in range(48):
        index = x+16
        one = sigma_one(w[index - 2])
        two = w[index - 7]
        three = sigma_zero(w[index - 15])
        four = w[index - 16]
        new_val = add_binary(one, two, three, four)
        w.append(new_val)

    return w

def alpha_sigma_zero(input):
    one = rotation(input, 2)
    two = rotation(input, 13)
    three = rotation(input, 22)
    output = ""
    for x in range(32):
        addition = int(one[x]) + int(two[x]) + int(three[x])
        output += str(addition % 2)
    return output

def alpha_sigma_one(input):
    one = rotation(input, 6)
    two = rotation(input, 11)
    three = rotation(input, 25)
    output = ""
    for x in range(32):
        addition = int(one[x]) + int(two[x]) + int(three[x])
        output += str(addition % 2)
    return output

def choose(e, f, g):
    output = ""
    for x in range(32):
        if (e[x] == "0"):
            output += g[x]
        else:
            output += f[x]

    return output

def maj(a, b, c):
    output = ""
    for x in range(32):
        zeros = 0
        ones = 0
        if (a[x] == "0"):
            zeros += 1
        else:
            ones += 1

        if (b[x] == "0"):
            zeros += 1
        else:
            ones += 1

        if (c[x] == "0"):
            zeros += 1
        else:
            ones += 1
        
        if (zeros > ones):
            output += "0"
        else:
            output += "1"

    return output


def t_one(h, e, f, g, k, w):
    alpha_e = alpha_sigma_one(e)
    che =choose(e,f,g)
    return add_six_binary(h, alpha_e, che, k, w)

def t_two(a, b, c):
    alpha_a = alpha_sigma_one(a)
    majority = maj(a,b,c)
    return add_two_binary(alpha_a, majority)

def solve_eight(input):
    T_one = t_one(initial_hash_values[7], initial_hash_values[4], initial_hash_values[5], initial_hash_values[6], constants[0], input[0])
    T_two = t_two(initial_hash_values[0], initial_hash_values[1], initial_hash_values[2])
    h = initial_hash_values[6]
    g = initial_hash_values[5]
    f = initial_hash_values[4]
    e = add_two_binary(initial_hash_values[3], T_one)
    d = initial_hash_values[2]
    c = initial_hash_values[1]
    b = initial_hash_values[0]
    a = add_two_binary(T_one, T_two)

    for x in range(63):
        index = x+1

        T_one = t_one(h, e, f, g, constants[index], input[index])
        T_two = t_two(a, b, c)
        h = g
        g = f
        f = d
        e = add_two_binary(d, T_one)
        d = c
        c = b
        b = a
        a = add_two_binary(T_one, T_two)

    return [a, b, c, d, e, f, g, h]

def add_eights(input):
    a = add_two_binary(input[0], initial_hash_values[0])
    b = add_two_binary(input[1], initial_hash_values[1])
    c = add_two_binary(input[2], initial_hash_values[2])
    d = add_two_binary(input[3], initial_hash_values[3])
    e = add_two_binary(input[4], initial_hash_values[4])
    f = add_two_binary(input[5], initial_hash_values[5])
    g = add_two_binary(input[6], initial_hash_values[6])
    h = add_two_binary(input[7], initial_hash_values[7])

    return [a, b, c, d, e, f, g, h]

def binary_to_hex(input):
    output = ""
    for x in input:
        decimal = int(x, 2)
        hexa = hex(decimal)
        splice = hexa[2:]
        output += splice

    print(output)


input_string = "RedBlockBlue"
input_binary = string_to_binary(input_string)

input_pre = preprocess(input_binary)
word_blocks = words(input_pre)
computed = computation(word_blocks)
eights = solve_eight(computed)
eights_arr = add_eights(eights)
binary_to_hex(eights_arr)

