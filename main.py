import restaurantTables as r

# Print out the all-free restaurant layout
print("All-Free Restaurant Layout:")
for row in r.restaurant_tables:
  print(row)

print("\nPartially-Occupied Restaurant Layout:")
# Print out the test layout with some 'x' indicating occupied tables
for row in r.restaurant_tables2:
  print(row)
