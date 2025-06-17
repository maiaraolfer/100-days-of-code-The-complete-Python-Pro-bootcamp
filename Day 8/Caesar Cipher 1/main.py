alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
    
def encrypt(text, shift):
    encrypted_message = ""
    for letter in text.lower():
        if letter in alphabet:
            new_index = (alphabet.index(letter) + shift) % len(alphabet)
            encrypted_message += alphabet[new_index]
        else:
            encrypted_message += letter  # Keep spaces, punctuation, etc.
    print(f"Here's the encoded result: {encrypted_message}")

encrypt(text, shift)

# behind the scenes thinking:
#alphabet is a list with indexes from a = 0 to z = 25;
#shift = 1
#a = print(alphabet.index("z")+ shift) # z+1 = index 26, but there is no index 26 in alphabet list index;
# the index 26 should be index 0, which in this case, letter z would become letter a in encrypted message.
# to do this we can use % 26: in this scenario, z(25) + shift(1) = 26 % 26 = new index (0, or letter 'a' again)
# obtaining the remainder from new_index makes sure we wrap around the alphabet list, so that, 
# any new_index number would have a matching index for the encrypted message
 
 
 
 