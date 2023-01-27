list_of_guests = ["Guest1", "Guest2", "Guest3", "Guest4", "Guest5"]

for name in list_of_guests:
    print(f"Hello {name}! You are welcomed at our dinner party.")

print("\nGuest3 cannot make it.\n")

list_of_guests[list_of_guests.index("Guest3")] = "Guest6"


for name in list_of_guests:
    print(f"Hello {name}! You are welcomed at our dinner party.")

print("\nHey guys! I found a bigger table.\n")

list_of_guests.insert(0, "Guest7")
list_of_guests.insert(5, "Guest8")
list_of_guests.append("Guest9")


for name in list_of_guests:
    print(f"Hello {name}! You are welcomed at our dinner party.")

