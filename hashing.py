#useless algo 
class XorHash:
    def __init__(self, message):
        self.hash_value = 0
        self.message = message

    def hashReturn(self):
        for character in self.message:
            char_num_value = ord(character)
            self.hash_value ^= char_num_value

        return self.hash_value 

#this is better
class FNV1:
    def __init__(self):
        self.hash_value = 129017893745307
        self.prime_num = 130503412681443

    def hashReturn(self, message):
        for character in message:
            char_num_value = ord(character)
            self.hash_value ^= char_num_value
            self.hash_value *= self.prime_num

            self.hash_value %= (2 ** 64 )

        return self.hash_value 

#this is fine use this
"""class MurmurHash:
    def __init__(self.message):
        pass"""