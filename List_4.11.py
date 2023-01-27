pizzas = ["Pizza1", "Pizza2", "Pizza3", "Pizza4", "Pizza5", "Pizza6"]

for pizza in pizzas:
    print(f"I like {pizza}.")
print("I love pizza very much!")

friend_pizza = pizzas.copy()

pizzas.append("Pizza7")
friend_pizza.append("Pizza8")

if pizzas != friend_pizza:
    print("\nBoth list are different\n")

print("\nMy favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("\nMy friends favorite pizzas are: ")
for pizza in friend_pizza:
    print(pizza)
