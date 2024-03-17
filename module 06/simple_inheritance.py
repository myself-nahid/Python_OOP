class Gadget:
    def __init__(self, brand, price, color, origin):
        self.brand = brand 
        self.price = price
        self.color = color
        self.origin = origin

    def __repr__(self):
        return f'{self.brand} {self.price} {self.color} {self.origin}'

    def run(self):
        return f'Running laptop: {self.brand}'


class Laptop(Gadget):
    def __init__(self, brand, price, color, origin, memory, ssd):
        self.memory = memory
        self.ssd = ssd
        super().__init__(brand, price, color, origin)

    def __repr__(self):
        print(f'{self.memory} {self.ssd}')
        return super().__repr__()

HP = Laptop('Pavilion-15cw0000ax', 80000, 'white', 'china', '1tb', '250gb')
print(HP)