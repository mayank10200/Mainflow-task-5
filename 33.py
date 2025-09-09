from itertools import permutations

s = input("Enter a string to find all permutations: ")
perm = [''.join(p) for p in permutations(s)]
print("All permutations are:")
print(perm)
