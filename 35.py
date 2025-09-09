from collections import Counter

lst = list(map(int, input("Enter numbers separated by space: ").split()))
count = Counter(lst)
duplicates = [item for item, freq in count.items() if freq > 1]
print("Duplicate elements are:", duplicates)
