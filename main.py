str = "hello world"
print(str[0])

# outputs - h

print(str[8])

# outputs - 4

print(str[2:])

# outputs - llo world
# starts from index 2 and ends at last Index

print(str[:4])

# outputs - hell
# starts from starting index and ends at index n-1

print(str[3:7])

# outputs - lo w
# starts from index 3 and ends at index 6

print(str[::3])

# outputs - hlwl
# starts from index 0 and ends at last index and skip 2(=3-1) character after printing a character

print(str[::-1])

# output - reverses the string without using reverse function