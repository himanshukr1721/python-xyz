class Chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level
    
    def sip(self):
        print("taking a sip")
    
    def add_sugar(self, amount):
        print("added the sugar")

my_chai = Chai(sweetness=3, milk_level=3)

print("thaank oyu")

