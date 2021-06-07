# Write Python code which accepts name of a product and in turn returns their respective prices.
# Make sure to use dictionaries to store products and their respective prices.
# The dictionary should include at least 5 elements.

productInfo = {
    "Apple": 220,
    "Mango": 160,
    "Banana": 40,
    "Grapes": 80,
    "Guava": 110
}

p = input('Enter product name to get price per KG : ')

print('{x}'.format(x=productInfo.get(p, 'Product not found')))
