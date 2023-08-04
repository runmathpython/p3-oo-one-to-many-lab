class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception("invalid pet type")
        self._pet_type = pet_type
    
    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self, value):
        if not (isinstance(value, Owner) or not value):
            raise TypeError("Owner must be an instance of Owner class.")
        self._owner = value

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of Pet class.")
        pet.owner = self
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key = lambda pet: pet.name)

    def sort_pets_by_name(self):
        return sorted(self.pets(), key = lambda pet: pet.name)
    