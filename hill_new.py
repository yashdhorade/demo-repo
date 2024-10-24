# Hill Cipher in Python

def HillCipher(message, key):
    # Create key matrix and message vector
    keyMatrix = [[ord(key[i * 3 + j]) % 65 for j in range(3)] for i in range(3)]
    messageVector = [[ord(message[i]) % 65] for i in range(3)]
    
    # Encrypt the message
    cipherMatrix = [(sum(keyMatrix[i][j] * messageVector[j][0] for j in range(3)) % 26) for i in range(3)]
    
    # Convert to ciphertext
    CipherText = ''.join(chr(c + 65) for c in cipherMatrix)
    print("Ciphertext:", CipherText)

# Driver Code
if __name__ == "__main__":
    message = "POH"
    key = "GYBNQKURP"
    HillCipher(message, key)
