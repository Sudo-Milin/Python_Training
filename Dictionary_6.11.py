cities = {
    "New York": {
        "Country": "America",
        "Population": "84.2 lakhs",
        "Fun Fact": "More than 800 languages are spoken in New York City, making it the most linguistically diverse city in the world."
        },
    "Delhi": {
        "Country": "India",
        "Population": "1.9 crores",
        "Fun Fact": "Delhi has Asia's Largest Wholesale Market for Fruit and Vegetables."
        },
    "Tokyo": {
        "Country": "Japan",
        "Population": "1.4 crores",
        "Fun Fact": "Tokyo was originally named Edo."
        },
    }

for keys, values in cities.items():
    print(keys)
    for key, value in values.items():
        print(f"\t{key}: {value}")
    print("")
