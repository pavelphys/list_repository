class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

class Bird:
    
    objInstancesCount = 0
    
    def __init__(self, name, id, age):
        self._name = name
        self._id = id
        self._age = age
        Bird.objInstancesCount = Bird.objInstancesCount + 1 
        
    # getter
    @property
    def name(self):
            return self._name
    # setter
    @name.setter
    def name(self, n):
            if(n != "Иван"):
                self._name = n
    
    # getter
    @property
    def age(self):
            return self._age
    # setter
    @age.setter
    def name(self, age):
            if(age >= 0):
                self._age = age
            else:
                self._age = 0
    
    # getter
    @property
    def id(self):
            return self._id
        
    def info(self):
        print("Имя: " + self._name)
        print("Идентификационный номер: " + str(self._id))
        print("Возраст: " + str(self._age))