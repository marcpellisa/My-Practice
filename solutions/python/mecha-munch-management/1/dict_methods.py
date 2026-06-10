"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """

    for items in items_to_add:
        if items in current_cart:
            current_cart[items] += 1
        else:
            current_cart[items] = 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    cart = {}
    add_item(cart,notes)
    return cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """

    for recipe_name, recipe_update in recipe_updates:
        ideas[recipe_name] = recipe_update
    return ideas

def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    return sorted(cart.items())


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """
    
    store_distribution = {}
    
    for product in sorted(cart, reverse=True):
        store_distribution[product] = [cart[product]] + aisle_mapping[product]

    return store_distribution


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """

    for products in fulfillment_cart:
        store_inventory[products][0] -= fulfillment_cart[products][0]
        if  store_inventory[products][0] == 0:
            store_inventory[products][0] = 'Out of Stock'
    return store_inventory
