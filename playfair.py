# Playfair Cipher - Simplified Version

# Remove spaces and convert to lowercase
def preprocess(text):
    return text.replace(" ", "").lower()

# Generate 5x5 matrix for the key
def generateKeyTable(key):
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    matrix, used = [], set()
    key = preprocess(key)

    for char in key + alphabet:
        if char not in used:
            used.add(char)
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

# Split plaintext into digraphs and insert filler if needed
def splitDigraphs(text):
    digraphs, i = [], 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'z'
        if a == b:
            digraphs.append(a + 'x')
            i += 1
        else:
            digraphs.append(a + b)
            i += 2
    if len(digraphs[-1]) == 1:
        digraphs[-1] += 'z'
    return digraphs

# Find character position in matrix
def findPosition(matrix, char):
    for row in range(5):
        if char in matrix[row]:
            return row, matrix[row].index(char)

# Apply encryption rules
def encryptDigraph(matrix, a, b):
    row1, col1 = findPosition(matrix, a)
    row2, col2 = findPosition(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

# Encrypt the entire plaintext
def playfairEncrypt(text, key):
    matrix = generateKeyTable(key)
    digraphs = splitDigraphs(preprocess(text))
    return ''.join([encryptDigraph(matrix, a, b) for a, b in digraphs])

# Example usage
plaintext = "instruments"
key = "monarchy"
ciphertext = playfairEncrypt(plaintext, key)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
