# List in Python

countries = ['India', 'Japan', 'Nigeria', 'Australia']
countries2 = list(('India', 2, True, 'Australia'))

print(countries)

for country in countries:
    print(country)

print(countries[0])

print(countries[1][2]) #should give 2nd index from japan(which is 1st index of countries)

print(countries[0][1:]) #gives substring

print(type(countries))
