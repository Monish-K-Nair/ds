from typing import List, overload
from bitarray import bitarray

class CustomBitArray:
    def __init__(self) -> None:
        pass

    def get_bitarray(self,size:int=None, data:List=None):
        if data:
            return bitarray(data)
        if size:
            return bitarray(size)


print(CustomBitArray().get_bitarray(data=[1,0,True, False]))
print(CustomBitArray().get_bitarray(size=10))
print(len(CustomBitArray().get_bitarray(size=10)))