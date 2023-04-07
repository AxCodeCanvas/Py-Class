# Display Process - 01

print("Hello Python")
language2 = "Java"
print("Hello Python", end="@")
print("Java")

# Display Process - 02

language = "Python"

print("Hello:", language, " and Java")

# P - 03

country = "Bangladesh"
country2 = "USA"

print('Country one is: {} and Country two is: {}'.format(country, country2))
print("Country one is: {c2} and Country two is: {c1}".format(c1=country, c2=country2))

# P - 04

print(f"Country are {country} and {country2}")
print(f'Country are {country2} and {country}')

# P - 05

num = 10.19181843847575

"""
%f - float
%d - int 
%s - string
"""

print(num)

print("%.3f" % num)

print("%d" % num)

print("%s" % country)

print("Country are %s and %s" % (country, country2))

Country1 = "Bangladesh"
Country2 = "USA"
Country3 = "Canada"

print("Country are %s, %s, and %s" % (Country3, Country2, Country1))