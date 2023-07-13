country_data = open('countries.txt', 'r')

print(country_data.readable())

'''print(country_data.readline())
print(country_data.readline())'''
#prints lines one by one by saving which last line it read.

# print(country_data.readlines()) # Gives a list
# print(country_data.readlines()[1])

for lines in country_data.readlines() :
    print(lines)

country_data.close()