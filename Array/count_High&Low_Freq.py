arr = [1, 1, 2, 2, 2, 3]

freq = {}

# Count frequency
for num in arr:
    freq[num] = freq.get(num, 0) + 1

maxFreq = float('-inf')
minFreq = float('inf')

maxElement = -1
minElement = -1

# Find highest and lowest frequency elements
for key, value in freq.items():
    if value > maxFreq:
        maxFreq = value
        maxElement = key

    if value < minFreq:
        minFreq = value
        minElement = key

print("Highest frequency element:", maxElement)
print("Lowest frequency element:", minElement)