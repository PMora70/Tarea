"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1 
    return current_cart

    
def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """
    new_user_cart = {}
    for note in notes:
        new_user_cart[note] = new_user_cart.get(note, 0) + 1
        
    return new_user_cart

    
def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """
    for recipe_name, ingredients in recipe_updates:
        ideas[recipe_name] = ingredients

    return ideas
    

def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """
    cart = dict(sorted(cart.items()))
    return cart


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {}
    for article, cart_data in sorted(cart.items(), reverse = True):
        quantity = cart_data
        aisle_data = aisle_mapping[article]
        aisle = aisle_data[0]
        shelf = aisle_data[1]
        fulfillment_cart[article] = [quantity, aisle, shelf]

    return fulfillment_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """
    updated_inventory = store_inventory.copy()
    for article, data in fulfillment_cart.items():
        quantity = data[0]
        inventory_data = store_inventory[article]
        inventory_quantity = inventory_data[0]
        aisle = inventory_data[1]
        shelf = inventory_data[2]
        final_quantity = inventory_quantity - quantity
        if final_quantity == 0:
            final_quantity = "Out of Stock"
        updated_inventory[article] = [final_quantity, aisle, shelf]

    return updated_inventory
        
    
