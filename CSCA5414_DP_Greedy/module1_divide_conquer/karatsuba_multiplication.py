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
    carry = 0
    binary_sum = []
    for bit_position in range(max(size_a, size_b)):
        bit_a = binary_a[bit_position] if bit_position < size_a else 0
        bit_b = binary_b[bit_position] if bit_position < size_b else 0
        (sum_bit, carry) = bitwise_add(bit_a, bit_b, carry)
        binary_sum.append(sum_bit)
    if carry == 1:
        binary_sum.append(carry)
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
    padding_size = len(binary_a) - len(binary_b)
    padded_b = binary_b + [0]*padding_size # 1
    flipped_padded_b = []
    for bit_b in padded_b: # 2
        flipped_padded_b.append(1-bit_b)
    b_twos_complement = add(flipped_padded_b, [1]) #3
    answer = add(binary_a, b_twos_complement) #4
    return answer[0:size_a] #5
    

def grade_school_multiplication(binary_a, binary_b):
    """
    Multiply a and b using grade-school (long) multiplication in binary.
    Bits are stored least-significant first (index i is worth 2**i).
    Idea: same as decimal long multiplication, but each digit of b is
    0 or 1, so each row is either a shifted copy of a, or nothing.
    Recipe:
      1. Start with result = 0 and shifted_a = a.
      2. For each bit of b, lowest first:
           - if the bit is 1, add shifted_a to the result;
           - shift shifted_a one place up (put a 0 at the FRONT of
             the list), which multiplies it by 2, ready for the next bit.
      3. Return the result.
    Example (values written normally, most-significant bit first):
      5 x 3:   101          (5)
             x  11          (3)
               101   bit 1 -> add a            (5)
              1010   bit 1 -> add a shifted    (10)
              ----
              1111                              (15)
    Running time: up to n additions of about n bits each -> Theta(n^2).
    """
    shifted_a = binary_a
    result = [0]
    for bit_b in binary_b:
        if bit_b == 1:
            result = add(result, shifted_a)
        shifted_a = [0] + shifted_a
    return result

def karatsuba_multiply (binary_a, binary_b):
    """
    Multiply a and b using Karatsuba's divide-and-conquer algorithm.
    Bits are stored least-significant first (index i is worth 2**i),
    so the LOW half of a number is the FIRST part of its list.
    Idea: split each number into a low half and a high half at the
    same position m:
        a = a_high * 2**m + a_low
        b = b_high * 2**m + b_low
    Multiplying out needs four products:
        a * b = (a_high*b_high) * 2**(2m)
              + (a_high*b_low + a_low*b_high) * 2**m
              + (a_low*b_low)
    Trick: get the middle part with ONE multiplication instead of two:
        (a_low + a_high) * (b_low + b_high)
            = a_low*b_low + [a_low*b_high + a_high*b_low] + a_high*b_high
        so  middle = sum_product - low_product - high_product
    Recipe:
      1. Base case: if either number has 2 bits or fewer,
         use grade-school multiplication.
      2. Split a and b at the same position m into low and high halves.
      3. Three recursive calls:
           low_product  = a_low  * b_low
           high_product = a_high * b_high
           sum_product  = (a_low + a_high) * (b_low + b_high)
      4. middle = sum_product - low_product - high_product
      5. Recombine:
           result = high_product shifted up by 2m
                  + middle       shifted up by m
                  + low_product
         (shifting up by k = putting k zeros at the FRONT of the list)

    Example (decimal, split after 1 digit, so shifts are powers of 10):
      12 x 34:  a_high=1, a_low=2, b_high=3, b_low=4
        low_product  = 2*4 = 8
        high_product = 1*3 = 3
        sum_product  = (2+1)*(4+3) = 21
        middle       = 21 - 8 - 3 = 10
        result       = 3*100 + 10*10 + 8 = 408

    Running time: 3 half-size multiplications + Theta(n) work to combine:
        T(n) = 3T(n/2) + Theta(n)  ->  Theta(n^(lg 3)) ~ Theta(n^1.585)
    """
    (size_a, size_b) = len(binary_a), len(binary_b)
    if size_a <= 2 or size_b <=2:
        return grade_school_multiplication(binary_a, binary_b)
    else:
        middle_point = size_a // 2
        a_low_half = binary_a[0:middle_point]
        a_high_half = binary_a[middle_point:]
        b_low_half = binary_b[0:middle_point]
        b_high_half = binary_b[middle_point:]
