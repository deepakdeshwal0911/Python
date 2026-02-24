salaries = list(map(float, input("Enter salaries: ").split()))

# Remove below minimum wage (example: 10000)
salaries = [s for s in salaries if s >= 10000]

# Add 5% bonus
for i in range(len(salaries)):
    if salaries[i] > 50000:
        salaries[i] += salaries[i] * 0.05

# Sort descending
salaries.sort(reverse=True)

print("Processed Salaries:", salaries)
print("Top 3 Salaries:", salaries[:3])
