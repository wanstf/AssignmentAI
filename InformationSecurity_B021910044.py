from pickle import TRUE

BITS = ('0', '1')
ASCII_BITS = 7

def display_bits(b):
    """Convert list of {0, 1}* to string"""
    return ''.join([BITS[e] for e in b])

def seq_to_bits(seq):
    return [0 if b == '0' else 1 for b in seq]

def pad_bits(bits, pad):
    """Pads seq with leading 0s up to length of pad"""
    assert len(bits) <= pad
    return [0] * (pad - len(bits)) + bits

def convert_to_bits(n):
    """COnvert an integer 'n' to bit array"""
    result = []
    if n == 0:
        return [0]
    while n > 0:
        result = [(n % 2)] + result
        n = int(n / 2)
    return result

def string_to_bits(s):
    def char_to_bit(c):
        return pad_bits(convert_to_bits(ord(c)), ASCII_BITS)
    return [b for group in
            map(char_to_bit, s)
            for b in group]

def bits_to_char(b):
    assert len(b) == ASCII_BITS
    value = 0
    for e in b:
        value = (value * 2) + e
    return chr(value)

def list_to_string(p):
    return ''.join(p)

def bits_to_string(b):
    return ''.join([bits_to_char(b[i:i + ASCII_BITS])
                    for i in range(0, len(b), ASCII_BITS)])

def otp(m, key):
    assert len(m) == len(key)
    return [(mm + kk) % 2 for mm, kk in zip(m, key)]

def XOR(A, B):
    return ''.join([chr(x ^ y) for x, y in zip(bytes(A, 'ascii'), bytes(B, 'ascii'))])

def crib_drag(text, c):
    for i in range(0, len(text) - len(c) + 1):
        pt = text[i:(i + len(c))]
        print("\t{0}:{1}".format(i,XOR(pt,c)))


#ENCRYPTION
print("\n")
print("ENCRYPTION")

key = string_to_bits("the keys")

X1 = string_to_bits("Zhaffuan")
X2 = string_to_bits("Wanchooo")

Y1 = otp(X1, key)
Y2 = otp(X2, key)

Y1Y2 = otp(Y1, Y2)

print("Key: " + str(key))
print("\n")

#Encryption of Message 1
print("Message 1: Zhaffuan")
print("Message 1: " + str(X1))
print("Ciphertext 1: " + str(Y1))
print("\n")

#Encryption of Message 2
print("Message 2: Wanchooo")
print("Message 2: " + str(X2))
print("Ciphertext 2: " + str(Y2))
print("\n")

#Y1 and Y2
print("Ciphertext 1: " + str(Y1))
print("Ciphertext 2: " + str(Y2))
print("Y1 XOR Y2: " + str(Y1Y2))
print("\n")


#DECRYPTION 
print("DECRYPTION")

Y1 = XOR("Zhaffuan", "the keys")
Y2 = XOR("Wanchooo", "the keys")
Y1Y2 = XOR("Zhaffuan", "Wanchooo")

while(TRUE):
    print("Input My Name")
    guess = input()
    crib_drag(Y1Y2, guess)