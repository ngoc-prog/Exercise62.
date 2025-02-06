class Product:
    def __init__(self, id, name, price, madein):
        self.id = id
        self.name = name
        self.price = price
        self.madein = madein

    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.price}\t{self.madein}"