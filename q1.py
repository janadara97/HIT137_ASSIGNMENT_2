def encrypt(n, m, dummy_text):
    f1 = open("raw_text.txt", "w")
    f1.write(dummy_text)
    encrypted_text = ""

    for ch in dummy_text:
        if ch.islower():
            if 'a' <= ch <= 'm':
                cipherText = ord(ch) + (n * m)
                if cipherText > ord('z'):
                    cipherText = ord('a') + (cipherText - ord('z') - 1)
                encrypted_text += chr(cipherText) + "1"  # Add category marker
            elif 'n' <= ch <= 'z':
                cipherText = ord(ch) - (n + m)
                if cipherText < ord('a'):
                    cipherText = ord('z') - (ord('a') - cipherText - 1)
                encrypted_text += chr(cipherText) + "2"  # Add category marker
        elif ch.isupper():
            if 'A' <= ch <= 'M':
                cipherText = ord(ch) - n
                if cipherText < ord('A'):
                    cipherText = ord('Z') - (ord('A') - cipherText - 1)
                encrypted_text += chr(cipherText) + "3"  # Add category marker
            elif 'N' <= ch <= 'Z':
                cipherText = ord(ch) + m ** 2
                if cipherText > ord('Z'):
                    cipherText = ord('A') + (cipherText - ord('Z') - 1)
                encrypted_text += chr(cipherText) + "4"  # Add category marker
        else:
            encrypted_text += ch + "0"  # Marker for special characters

    f2 = open("encrypted_text.txt", "w")
    f2.write(encrypted_text)
    f2.close()

    return encrypted_text


def decrypt(n, m):
    f = open("encrypted_text.txt", "r")
    encrypted_content = f.read()

    decrypted_text = ""
    i = 0

    while i < len(encrypted_content):
        ch = encrypted_content[i]
        if i + 1 < len(encrypted_content) and encrypted_content[i + 1].isdigit():
            category = encrypted_content[i + 1]
            i += 1  # Skip to the next character after marker
            if category == "1":
                cipherText = ord(ch) - (n * m)
                if cipherText < ord('a'):
                    cipherText = ord('z') - (ord('a') - cipherText - 1)
                decrypted_text += chr(cipherText)
            elif category == "2":
                cipherText = ord(ch) + (n + m)
                if cipherText > ord('z'):
                    cipherText = ord('a') + (cipherText - ord('z') - 1)
                decrypted_text += chr(cipherText)
            elif category == "3":
                cipherText = ord(ch) + n
                if cipherText > ord('Z'):
                    cipherText = ord('A') + (cipherText - ord('Z') - 1)
                decrypted_text += chr(cipherText)
            elif category == "4":
                cipherText = ord(ch) - m ** 2
                if cipherText < ord('A'):
                    cipherText = ord('Z') - (ord('A') - cipherText - 1)
                decrypted_text += chr(cipherText)
            elif category == "0":
                decrypted_text += ch
        else:
            decrypted_text += ch
        i += 1

    return decrypted_text


def check_correctness(original, decrypted):
    if original == decrypted:
        print("Decryption is correct!")
    else:
        print("Decryption is incorrect.")


def main():
    dummy_text = "This is a dummy content for the ASSIGNMENT2 fdfdfdf ffdfdfd HHJHJJ jhjhjhjhj"
    n = 4
    m = 5
    print("Original Text:", dummy_text)

    # Encrypt the text
    encrypted_message = encrypt(n, m, dummy_text)
    print("Encrypted Text:", encrypted_message)

    # Decrypt the text
    decrypted_message = decrypt(n, m)
    print("Decrypted Text:", decrypted_message)

    # Check correctness
    check_correctness(dummy_text, decrypted_message)


main()

# Here we've got an issue in the decryption process
# Issue Explanation:
# The core problem lies in the mismatch between the categorization of characters during encryption and decryption.
# In encryption, characters are categorized based on their original range (e.g., 'a-m', 'n-z', 'A-M', 'N-Z').
# However, after the encryption shifts, the characters may move out of their original range, leading to a
# re-categorization during decryption. This re-categorization results in applying incorrect decryption logic.

# Example of the issue:
# - Original character: 'a' (belongs to 'a-m')
# - Encrypted character: 'u' (shifts out of 'a-m' and into 'n-z')
# - During decryption, 'u' is treated as belonging to 'n-z', applying the wrong decryption logic.

# Marker-Based Solution:
# To resolve this, a marker or tagging mechanism can be introduced during encryption to preserve the
# original category of the character. This marker allows the decryption process to correctly identify
# the original range of the character, ensuring the correct decryption logic is applied.

# Note:
# Marker tagging ensures that the character's transformation logic remains consistent across encryption
# and decryption, eliminating the risk of misclass