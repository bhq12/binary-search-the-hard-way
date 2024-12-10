import sys
class CustomBooleanFalseIterator:

    def __getitem__(self, index):
        # very big number to stop people linear scanning
        if index > (sys.maxsize - 1):
            raise IndexError('Index out of range')
        return False

    def __len__(self):
        return sys.maxsize

class CustomBooleanTrueIterator:

    def __getitem__(self, index):
        # very big number to stop people linear scanning
        if index > (sys.maxsize - 1):
            raise IndexError('Index out of range')
        return True

    def __len__(self):
        return sys.maxsize

class CustomBooleanTrueFalseIterator:

    def __getitem__(self, index):
        # very big number to stop people linear scanning
        if index > (sys.maxsize - 1):
            raise IndexError('Index out of range')

        if index < 10:
            return True

        return False

    def __len__(self):
        return sys.maxsize
