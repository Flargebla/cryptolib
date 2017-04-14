import string

class CaesarCipher(object):
    def __init__(self, key = 0):
        self.set_key(key)
        self.__update_tables()
    
    def __update_tables(self):
        original = string.ascii_lowercase + string.ascii_uppercase +\
                   string.punctuation + string.whitespace + string.digits
        shifted = original[self.key % len(original):] +\
                  original[:self.key % len(original)]

        self.__enc_table = string.maketrans(original, shifted)
        self.__dec_table = string.maketrans(shifted, original)
        
    def set_key(self, key):
        if(type(key) == int or type(key) == long):
            self.key = key
            self.__update_tables()
        else:
            raise TypeError("CaesarCipher.key must be int or long")

    def encrypt(self, pt):
        return str(pt).translate(self.__enc_table)
    
    def decrypt(self, ct):
        return str(ct).translate(self.__dec_table)
