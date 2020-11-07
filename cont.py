import argparse

from models import Curr, Item, Cart, Offer



parser = argparse.ArgumentParser()
parser.add_argument("-curr", type=str)
parser.add_argument('-o','--order', nargs='+', help='<Required> Set flag', required=True)

# main thread
if __name__ == "__main__":

    # Globals, represents the data resource of
    # the program, can be implemented as a db.

    catalog = {
        'T-shirt': 10.99,
        'Pants': 14.99,
        'Jacket': 19.99,
        'Shoes': 24.99
    }

    mods = {
        'Shoes': 0.1,
        'Jacket': 0.5,
        'Taxes': 1.14
    }


    args = parser.parse_args()

    cart = Cart(args.order, catalog, mods)

    offers = []

    # applying Shoes offer
    if 'Shoes' in cart.items:
        item = cart.items['Shoes']
 
        shoesOffer = Offer(
            item,
            [True],
            Curr(item.cost.cents, 'cents').multiply(mods[item.name]).pounds,
            f"10% off {item.name}:",
            mods
        )

        offers.append(shoesOffer)

    # applying Jacket offer
    if 'Jacket' in cart.items and 'T-shirt' in cart.items:
        item = cart.items['Jacket']
        J = item.qnt
        S = cart.items['T-shirt']
        D = J//S

        jacketOffer = Offer(
            item,
            [item.qnt > 0, related.qnt//2 > 0],
            Curr(item.price.cents, 'cents').multiply(mods[item.name] * min(J, D)).pounds,
            f"50% off {item.name}:",
            mods
        )

        offers.append(jacketOffer)
    
    cart.bill(offers)


