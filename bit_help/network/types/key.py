class Key:
    def __init__(self, public, private):
        self.__public = public
        self.__private = private
    
    @property 
    def public(self):
        return self.__public

    @property
    def private(self):
        return self.__private
