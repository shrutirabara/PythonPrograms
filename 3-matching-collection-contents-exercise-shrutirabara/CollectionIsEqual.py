class CollectionIsEqual :
    def __init__(self) :
        pass

    #Checks if both objects contain the same content regaurdless of type
    def isEqual(self, obj1, obj2) :
        s1 = set(obj1)
        s2 = set(obj2)
        return sorted(s1) == sorted(s2)
         

    #Checks if both objects have the same unique content, regaurdles of lengths
    def sharesUnique(self, obj1, obj2):
        s1 = set(obj1)
        s2 = set(obj2)

        unique = set(s1) | set(s2)
        if len(unique) == len(s1) or len(unique) == len(s2) :
            return True
        else :
            return False
       
    