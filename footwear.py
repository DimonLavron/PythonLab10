class Footwear:
    amount = 0

    def __init__(self, manufacturer="Nike", price=99.99, size=42, color="black", type="sneakers", color_of_laces="black", material="leather"):
        self.manufacturer = manufacturer
        self.price = price
        self.size = size
        self.color = color
        self.type = type
        self.color_of_laces = color_of_laces
        self.material = material

    def __del__(self):
        return print(self.manufacturer + " footwear deleted")

    def __str__(self):
        return str(self.__dict__)

    @staticmethod
    def get_static_field():
        return Footwear.amount

def main():
    default_footwear = Footwear()
    shoes = Footwear("Armani", 299.99, 45, type="shoes", material="suede")
    sandals = Footwear("TheNorthFace", 49.99, 39, "brown", "sandals", None)

    print(default_footwear)
    print(shoes)
    print(sandals)
    print(Footwear.get_static_field())

if __name__ == "__main__":
    main()
