def encrypt(text: str, shift: int):
    print("\n\n\t\tEncrypted Message\n")
    text = text.upper()
    max_threshold = 90
    encrypted_chr = ''
    encrypted_ascii = ''

    for character in text:
        ascii_eq = ord(character)
        ascii_eq += shift

        if ascii_eq > max_threshold:
            ascii_eq -= 26

        encrypted_chr += chr(ascii_eq)
        encrypted_ascii += str(ascii_eq)

    for i in range(len(encrypted_chr)):
        char = encrypted_chr[i]
        ascii_pair = encrypted_ascii[i * 2:i * 2 + 2]
        print(f"\nEncrypted Character: {char} || Value: {ascii_pair}")
    
    print("\nEncrypted CHAR: ", encrypted_chr)
    print("\nEncrypted ASCII: ", encrypted_ascii)

    return [encrypted_chr, encrypted_ascii]

def decrypt(encrypted: str, shift: int):
    print("\n\n\t\tDecrypted Message\n")
    encrypted = encrypted.upper()
    min_threshold = 65
    decrypted_chr = ''
    decrypted_ascii = ''

    for i in range(0, len(encrypted), +2):
        ascii_str = encrypted[i] + encrypted[i+1]
        ascii_int = int(ascii_str)
        ascii_int -= shift

        if ascii_int < min_threshold:
            ascii_int += 26

        decrypted_chr += chr(ascii_int)
        decrypted_ascii += str(ascii_int)

    for i in range(len(decrypted_chr)):
        char = decrypted_chr[i]
        ascii_pair = decrypted_ascii[i * 2:i * 2 + 2]
        print(f"\nDecrypted Character: {char} || Value: {ascii_pair}")
    
    print("\nDecrypted CHAR: ", decrypted_chr)
    print("\nDecrypted ASCII: ", decrypted_ascii)

    return [decrypted_chr, decrypted_ascii]

while True:
    print(f"\n\n\tC A E S A R   C I P H E R   P R O G R A M\n\n")
    text = input("Enter text here: ")
    shift = int(input('Enter shift: '))

    encrypted_chr, encrypted_ascii = encrypt(text, shift)
    decrypted_ascii, decrypted_chr = decrypt(encrypted_ascii, shift)

