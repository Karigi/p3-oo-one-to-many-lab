class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self,name,pet_type,owner = ''):
        self.name = name
        self._owner = owner
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception("pet_type not in PET_TYPES")
        
        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner (self,value):
        if isinstance(value,Owner):
            self._owner = value
        else:
            raise Exception("Owner must be of Owner class")




class Owner:
    def __init__(self,name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self,pet):
        if not isinstance(pet,Pet):
            raise Exception("pet must be of class Pet")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted([pet for pet in Pet.all if pet.owner == self],key= lambda pet: pet.name)



