import pdb
class Mask(object):

    def __init__(self, mask, type="mask"):
        """ bin is a string that begins with 0b
            int is always a number
            mask is a string of numbers between 0 and 7
        """

        if type == "bin":
            self._mask = self.convert_from_bin(mask)
        elif type == "int":
            self._mask = self.convert_from_int(mask)
        else:
            self._mask = mask

    @property
    def mask(self):
        return self._mask.zfill(3)

    @property
    def to_int(self):
        # take a mask like 777 and convert it into an integer for performing
        # bitwise operations.
        i = 0
        for value in list(str(self._mask)):
            i <<= 3
            i |= int(value)
        return i

    @property
    def to_bin(self):
        # take 777 and convert it into '0b111111111'
        return format(self.to_int, '#011b')

    @property
    def to_list(self):
        return list(self.to_bin[2:])

    def or_with(self, input):
        return to_int | Mask(input).to_int

    #def and_with():
    #def xor_with():

    @property
    def not_bits(self):
        notted_int = (self.to_int ^ 511)
        self._mask = Mask(bin(notted_int), 'bin').mask
        return True

    def bit(self,position):
        """ position 0 should become 8
            position 1 should become 7
            position 2 should become 6
            etc.
        """
        position = (position - 8) * -1
        return int(self.to_list[position])


    def convert_from_bin(self, b):
        """ take '0b111111111' and convert into 777 """

        b = "".join(list(b)[2:])     # drop off the 0b from the start
        b = b.zfill(9)
        mask = ''
        b = list(b)
        while len(b) != 0:
            bits = ""
            for i in range(0,3): bits += b.pop(0)     # grab three bits.
            mask += str(int(bits, 2))
        return mask

    def convert_from_int(self, i):
        """ take an integer and turn it into a mask.
            Eg. 511 == 777
        """

        mask = bin(i)
        return self.convert_from_bin(mask)
