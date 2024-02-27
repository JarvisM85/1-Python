
#Mixing positional and arbitrary arguments
def make_pizza(size,*toppings):
    print(f"\nMaking a {size}-inch pizza with following toppings :")
    for topping in toppings:
        print(f" -{topping}")
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green pepper','extra cheese')
