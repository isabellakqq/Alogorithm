cities = ['London', 'Paris', 'Paris', 'Los Angeles', 'New York']
ind = list(range(5))
zip_cities = zip(cities, ind)

sorted_cities = sorted(zip_cities)
print(list(sorted_cities))