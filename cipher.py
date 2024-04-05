def caesar_cipher(text, shift=5):
    text = text.lower()
    encrypted_text = ''
    
    for char in text:
        # Check if the character is an alphabet
        if char.isalpha():
            # Find the position of the character in the alphabet and apply the shift
            shifted_pos = (ord(char) - ord('a') + shift) % 26
            # Append the shifted character to the encrypted text
            encrypted_text += chr(shifted_pos + ord('a'))
        else:
            # If character is not an alphabet, append it as it is
            encrypted_text += char
            
    return encrypted_text

sentence = input("Please enter a sentence: ")
# Encrypt the sentence
encrypted_sentence = caesar_cipher(sentence)
print(f"The encrypted sentence is: {encrypted_sentence}")