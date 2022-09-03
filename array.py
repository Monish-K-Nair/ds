import array as arr

a = arr.array('i', [1, 2, 3])

class CustomArray:

    def __init__(self, type, typecode=None, data=None):
        if data is None:
            data = []
        if type == 'int':
            self.array = self.__int_array(typecode=typecode, data=data)
        elif type == 'char':
            self.array =  self.__char_array(typecode=typecode, data=data)
        elif type == 'float':
            self.array = self.__float_array(typecode=typecode, data=data)

    def __int_array(self, typecode, data):
        return arr.array('i', data) if typecode is None else arr.array(typecode, data)

    def __char_array(self, typecode, data):
        return arr.array('u', data) if typecode in [None, 'u'] else arr.array(typecode, data.encode())

    def __float_array(self, typecode, data):
        return arr.array('f', data) if typecode is None else arr.array(typecode, data)

    def get_array(self):
        return self.array


print(CustomArray('char', data='abc').get_array())
print(CustomArray('char',typecode='b', data='abc').get_array())
print(CustomArray('char',typecode='B', data='abc').get_array())
print(CustomArray('int', data=[1,2,3]).get_array())
print(CustomArray('float', data=[1,2,3]).get_array())