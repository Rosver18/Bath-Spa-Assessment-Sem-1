print("Exercise 7: Seeing the World")
print("    ")
#using a list to display the countries
world = ['America', 'Philippines', 'Japan', 'Korea', 'Mexico']

#using the variable by itself shows the original order of the list
print("Original order:")
print(world)

#using the sorted string shows the alphabetical order of the list
print("\nAlphabetical order:")
print(sorted(world))

#using the variable by itself reverts it back to the original order
print("\nOriginal order:")
print(world)

#using the sorted string with the reverse modification makes it a reverse alphabetical order
print("\nReverse alphabetical order:")
print(sorted(world, reverse=True))

#using the variable by itself reverts it back to the original order
print("\nOriginal order:")
print(world)

#using the reverse string reverses the order of the list
print("\nReversed order:")
world.reverse()
print(world)

#using the variable by itself reverts it back to the original order
print("\nOriginal order:")
world.reverse()
print(world)

#using the sorted string shows the alphabetical order of the list
print("\nAlphabetical order:")
world.sort()
print(world)

#using the sorted string with the reverse modification makes it a reverse alphabetical order
print("\nReverse alphabetical order:")
world.sort(reverse=True)
print(world)