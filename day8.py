# # def greet():
# #     print("i am avni")
# #     print("hlo world!")
# #     print("hahahahaha")

# # greet()



def call_with_me(name,address):
    print(f"hello,{name}. ")
    print(f"what do you want? {name} and where do you live {address}")
    print(f"how do you do? {name} and whre do you want to go {address}")
x = input("name: ")
y = input("address: ")
call_with_me(x,y)





alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("type your message:\n").lower()
shift = int(input("type the shift number:\n"))

   #for encode

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position= alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]

#     print(f"here is the encoded result: {cipher_text}")

 #for decode

# def decrypt(original_text, shift_amount):
#     output_text = ""
#     for letter in original_text:
#         shifted_position= alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]
#     print(f"here is the decoded result: {output_text}")
