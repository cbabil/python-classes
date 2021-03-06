'''
Created on July 01 2015

'''


class Tree:

    def __init__(self, key, data):
        '''
        Create a new Tree object with a key and its data. 
        Also initialize empty L & R subtrees.
        '''
        self.key = key
        self.data = data
        self.left = self.right = None

    def insert(self, key, data):
        '''
        Insert a new element into the tree in the correct 
        position with its associated data.
        '''
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Tree(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Tree(key, data)
        else:
            raise ValueError("Attempt to insert duplicate value.")

    def walk(self):
        '''
        Generate the keys from the tree in sorted order.
        '''
        if self.left:
            for n in self.left.walk():
                yield n
        yield self.key
        if self.right:
            for n in self.right.walk():
                yield n

    def find(self, key):
        '''
        Returns the data associated with the key.
        If the key is not present in the tree, a KeyError 
        exception is raised.
        '''
        if key == self.key:
            return self.data
        elif key < self.key:
            if self.left:
                return self.left.find(key)
            else:
                raise KeyError("%r does not exist." % key)
        else:
            if self.right:
                return self.right.find(key)
            else:
                raise KeyError("%r does not exist." % key)

if __name__ == '__main__':
    t = Tree("t", "T")
    for key, data in zip('python', 'PYTHON'):
        t.insert(key, data)
    print(list(t.walk()))
    print("Data of key %r is %r" % ('t', t.find('t')))