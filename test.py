


class Vierhoek:
    """_summary_
    """
    def __init__(self, l, b) -> None:
        """_summary_

        Args:
            l (_type_): _description_
            b (_type_): _description_
        """
        self.lengte=l
        self.breedte=b
        self.area = l*b
        self.omtrek = 2*(l+b)

    def set_lengte(self, l):
        self.lengte=l
        self.area = l*self.breedte

    def set_breedte(self, b):
        self.breedte=b
        self.area = b*self.lengte


vierkant = Vierhoek(2,3)
print(vierkant.area)
vierkant.set_breedte(5)
vierkant.set_lengte(15)
print(vierkant.area)


class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance




a = Dog(input("Wat is die hond se name?")) 
b = Dog(input("Wat is die hond se name?"))

print(a.name)
print(b.name)
print(a.kind)
print(b.kind)
      
