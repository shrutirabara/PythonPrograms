from CollectionIsEqual import CollectionIsEqual
import unittest

class CollectionIsEqualTest(unittest.TestCase) :
    def setUp(self):
        self.check_equality = CollectionIsEqual()

    #Checks if both objects contain the same content regaurdless of type
    def test_isEqual(self) :
        
        #Create a list and a tuple with the exact same contents
        obj1 = [1,2,3,4,5]
        obj2 = (1,2,3,4,5)

        #Should return true
        self.assertTrue(self.check_equality.isEqual(obj1, obj2))

    #Checks if both objects have the same unique content, regaurdles of lengths
    def test_sharesUnique(self) :

        #Creates 2 lists with the same contents, but both contain duplicates
        obj1 = (1,1,1,2,3,4,4,4,5,6,7,7)
        obj2 = (1,1,1,1,2,3,4,4,4,4,5,5,5,6,6,6,6,6,7,7,7,7,7)

        self.assertTrue(self.check_equality.sharesUnique(obj1, obj2))


if __name__ == "__main__" :
    unittest.main()
