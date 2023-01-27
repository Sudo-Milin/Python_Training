Person1 = {"first_name": "John", "last_name": "Doe", "age": 23, "city": "Paris"}

Person2 = {"first_name": "Dean", "last_name": "Lewis", "age": 25, "city": "Sydney"}

Person3 = {"first_name": "Jay", "last_name": "Dixit", "age": 24, "city": "Delhi"}

people = [Person1, Person2, Person3]

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print("")
