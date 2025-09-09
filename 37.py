import heapq

lst = list(map(int, input("Enter numbers separated by space: ").split()))
k = int(input("Enter value of k: "))
largest = heapq.nlargest(k, lst)
print(f"{k} largest elements are: {largest}")
