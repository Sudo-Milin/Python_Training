food = ("Pizzas", "Sandwiches", "Burgers", "Fries", "Sizzlers")

for item in food:
    print(item)

try:
    food[1] = "Desserts"

except(TypeError):
    print("\nYou cannot modify a tuple\n")

food = ("Pizzas", "Sandwiches", "Burgers", "Wraps", "Desserts")

for item in food:
    print(item)
