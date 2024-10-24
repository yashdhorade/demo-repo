# Rail Fence Cipher Encryption
def encrypt(text, key):
    if key == 1:
        return text  # No change in the case of a single rail
    rail = [''] * key
    row, step = 0, 1
    for char in text:
        rail[row] += char
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step
    return ''.join(rail)

# Rail Fence Cipher Decryption
def decrypt(cipher, key):
    if key == 1:
        return cipher  # No change for single rail
    rail = [[''] * len(cipher) for _ in range(key)]
    idx, step, row = 0, 1, 0
    for _ in cipher:
        rail[row][idx] = '*'
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row, idx = row + step, idx + 1
    idx = 0
    for r in range(key):
        for c in range(len(cipher)):
            if rail[r][c] == '*':
                rail[r][c] = cipher[idx]
                idx += 1
    result, row, step = [], 0, 1
    for c in range(len(cipher)):
        result.append(rail[row][c])
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step
    return ''.join(result)

# Example usage
print(encrypt("attack at once", 2))
print(decrypt("atc toctaka ne", 2))
