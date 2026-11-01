def convert_to_binary(decimal_number):
    assert decimal_number >= 0
    if decimal_number == 0:
        return [0]
    binary_number = []
    while decimal_number > 0:
        binary_number.append(decimal_number % 2)
        decimal_number = decimal_number // 2
    return binary_number

def convert_to_decimal (binary_number):
    decimal_number = 0
    binary_position_value = 1
    for digit in binary_number:
        decimal_number = decimal_number + digit*binary_position_value
        binary_position_value = binary_position_value*2
    return decimal_number

def bitwise_add (bit_a, bit_b, carry_in):
    if bit_a == 0 and bit_b == 0:
        sum_bit = carry_in
        carry_out = 0
    elif bit_a != bit_b:
        sum_bit = 1 - carry_in
        carry_out = carry_in
    else:
        sum_bit = carry_in
        carry_out = 1
    return sum_bit, carry_out

def add(binary_a, binary_b):
    (size_a, size_b) = len(binary_a), len(binary_b)
    carry_in = 0
    binary_sum = []
    for bit_position in range(max(size_a, size_b)):
        bit_a = binary_a[bit_position] if bit_position < size_b else 0
        bit_b = binary_b[bit_position] if bit_position < size_a else 0
        (sum_bit, carry_out) = bitwise_add(bit_a, bit_b, carry_in)
        binary_sum.append(sum_bit)
    if carry_out == 1:
        binary_sum.append(carry_out)
    return binary_sum

def subtract(binary_a, binary_b):
    """
    Subtract b from a using two's complement: a - b.
    Bits are stored least-significant first (index i is worth 2**i),
    so "leading" zeros go at the END of the list.
    Assumes a >= b, so the result is never negative.
    Recipe:
      1. Pad:  add zeros to the end of b until it has as many bits as a.
      2. Flip: change every bit of the padded b (0 -> 1, 1 -> 0).
               This gives (2**n - 1) - b, with no borrowing needed.
      3. Add 1 to the flipped b. This gives 2**n - b,
               the two's complement of b.
      4. Add a to that result. This gives a - b + 2**n.
      5. Keep only the first n bits (n = len(a)). This drops the
               extra carry bit worth 2**n, leaving exactly a - b.
    Example (4 bits, values written normally, most-significant bit first):
      6 - 3:  3 = 0011 -> flip 1100 -> +1 1101 -> + 0110 = 10011
              -> drop extra carry -> 0011 = 3
    """
    size_a = len(binary_a)
    complement_size = len(binary_a) - len(binary_b)
    flipped_b = []
    for bit_b in binary_b: # 1 & 2
        flipped_b.append(1-bit_b)
    padded_flipped_b = flipped_b + [1]*complement_size
    b_twos_complement = add(padded_flipped_b, [1]) #3
    answer = add(binary_a, b_twos_complement)
    return answer[0:size_a]
    

