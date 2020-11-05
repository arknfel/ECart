class Curr:
    
    # At initialization, func set_value() sets values for
    # cents and pounds properly in terms floating-point 
    def __init__(self, value, measure):
        
        self.cents = None
        self.pounds = None
        self.set_val(value, measure)

    # Conversion is set to account for only 2 digits
    # after the floating-point, the rest is ommited.
    def set_val(self, value, measure):

        # If the passed value is measured as cents,
        # conversion is set for pounds and vise-versa.
        if measure == 'cents':
            self.cents = int(value)  # int
            self.pounds = self.cents/100  # float
        
        if measure == 'pounds':
            self.pounds = value  # float
            self.cents = int(self.pounds*100)  # int

    # Operators add, subt and multiply are utilizing func
    # set_value() to keep the integrity of the conversion.

    def add(self, value, measure):
        self.set_val(self.cents + Curr(value, measure).cents, 'cents')
        return self
    
    def subt(self, value, measure):
        self.set_val(self.cents - Curr(value, measure).cents, 'cents')
        return self
    
    def multiply(self, value):
        self.set_val(self.cents * value, 'cents')
        return self


# A simple data-structure that will help us
# to store information of items in a cart
class Item:
    
    def __init__(self, name, price, qnt):
        
        self.name = name
        self.price = Curr(price, 'pounds')  # assuming, catalog stores prices as pounds (float)
        self.qnt = qnt
        self.cost = Curr(self.price.cents * self.qnt, 'cents')


class Cart:
    
    # order is the user's input to the program
    def __init__(self, order, catalog, mods):

        # cached data
        self.items = {}
        self.cost = Curr(0, 'cents')

        # Fill cart with counted items
        # calculate the total cost for each item
        # calculate the total cost of the cart

        for item in order:

            if item in self.items:
                self.items[item].qnt += 1
                self.items[item].cost.add(self.items[item].price.cents, 'cents')

            else:
                self.items[item] = Item(name=item, price=catalog[item], qnt=1)

            self.cost.add(self.items[item].price.cents, 'cents')
        
        self.taxed = Curr(self.cost.cents, 'cents').multiply(mods['Taxes'])

        # print(f'${self.cost.pounds}')

    def apply_tax(self, modifier):

        self.cost.multiply(modifier)

        # print(self.cost.cents)
        # print(f'${self.cost.pounds}')
        
    def bill(self, offers=None):
        
        out = "\n"+f"Subtotal: ${self.cost.pounds}"+"\n"
        out += f"Taxes: {Curr(self.taxed.cents, 'cents').subt(self.cost.cents, 'cents').pounds}"+"\n"
        
        if offers:
            out += "Discounts:\n"
            for offer in offers:
                if offer.conds:
                    line = 4*" " + offer.__repr__() + "\n"
                    out += line

        out += f"Total: ${self.taxed.pounds}"+"\n"
        
        print(out)


class Offer:
    
    def __init__(self, item, conds, discount, string, mods):

        self.item = item
        self.conds = conds
        self.discount = discount
        self.string = string

        if mods and item.name in mods and False not in conds:
            self.conds = True
        else:
            self.conds = False


    def __repr__(self):

        return f"{self.string}  - ${self.discount}"
