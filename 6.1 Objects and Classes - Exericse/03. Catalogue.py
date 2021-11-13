class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        return list(filter(lambda x: x if x[0] == first_letter else None, self.products))

    def __str__(self):
        string = ''
        string += f'Items in the {self.name} catalogue:\n'
        sorted_products = sorted(self.products)
        string += '\n'.join(sorted_products)
        return string
