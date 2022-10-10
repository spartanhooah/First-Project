temps = [221, 234, 340, -9999, 230] # -9999 means "no valid data"; should be ignored
new_temps = [temp / 10 for temp in temps if temp != -9999] # list comprehension

print(new_temps)

# If you want to add an else, the for/in needs to be after the if/else
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps)