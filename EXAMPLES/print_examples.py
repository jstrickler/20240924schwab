city = 'Orlando' 
temperature = 85
hit_count = 5
average = 3.4563892382

print(city, temperature, hit_count, average, sep=" ")
print()

print(city, end=' ')  # Print space instead of newline at the end
print(temperature)
print()

# Item separator is comma + space
print(city, temperature, hit_count, average, sep=",")
print()

# Item separator is empty string
print(city, temperature, hit_count, average, sep="")
print()

print("The temperature in", city, "is", temperature)

print(f"The temperature in {city} is {temperature}")

result = 22 / 7
print(f"Result is {result}")
print(f"Result is {result:.2f}")

percentage = .88

print(f"{percentage:.0%}")

print(f"2 + 2 is {2 + 2}")

# >= 3.6

