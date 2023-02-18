products = input()

array_products = products.split(" ")# string to list, ‘here is’ => [‘here’, ‘is’]
results = ", ".join(array_products) # list to string, adds comma ‘,’ or anything

print(f"I have {results} in my shopping cart.") # string formatter f”lol {value}”
