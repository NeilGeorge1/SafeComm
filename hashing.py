#useless algo 
class XorHash:
    def __init__(self):
        pass

    def hashReturn(self, message):
        hash_value = 0
        for character in message:
            char_num_value = ord(character)
            hash_value ^= char_num_value

        return hash_value 

#this is better
class FNV1:
    def __init__(self):
        pass

    def hashReturn(self, message):
        hash_value = 129017893745307
        prime_num = 130503412681443

        for character in message:
            char_num_value = ord(character)
            hash_value ^= char_num_value
            hash_value *= prime_num

            hash_value %= (2 ** 64 )

        return hash_value 

#this is fine use this
"""class MurmurHash:
    def __init__(self.message):
        pass"""

fnv1 = FNV1()
print(fnv1.hashReturn('Qwerty123'))
print(fnv1.hashReturn('Qwerty123')) 
