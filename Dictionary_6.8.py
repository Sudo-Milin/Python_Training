pet1 = {"Type":"Cat", "Owner":"Max"}
pet2 = {"Type":"Dog", "Owner":"Suzy"}
pet3 = {"Type":"Rabbit", "Owner":"John"}

pets = [pet1, pet2, pet3]

for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print("")

    
