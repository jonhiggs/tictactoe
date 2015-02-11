class Mask(object):

    def __init__(self, mask, type="mask"):
        if type == "bin":
            self._mask = self.convert_from_bin(mask)
        elif type == "int":
            self._mask = self.convert_from_int(mask)
        else:
            self._mask = mask

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


    def convert_from_bin(self, bin):
        # take '0b111111111' and convert into 777

        bin = list(bin)[2:]     # drop off the 0b from the start
        mask = ''
        #pdb.set_trace()
        while len(bin) != 0:
            bits = "".join(bin[-3:])
            mask += str(int(bits, 2))
            bin = bin[:-3]
        return int(mask)

    def convert_from_int(self, i):
        # take an integer and turn it into a mask.
        # eg 511 == 777

        a = list(format(i, '#011b'))
        a.pop(0)
        a.pop(0)
        "".join(a)

        mask = "0b"
        for row in range(0, 3):
            v = str(a.pop(0) + a.pop(0) + a.pop(0))
            mask += v

        return mask
