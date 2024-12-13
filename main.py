from RSA import RSA

print("Starting........")

message = input("Please enter message-> ")

rsa = RSA(message)

rsa.result()