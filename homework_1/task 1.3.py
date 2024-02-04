text = "si vis pacem para bellum"
parts = text.split()
result = ' '.join(parts[len(parts) // 2:] + parts[:len(parts) // 2])
print(result)
