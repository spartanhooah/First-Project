temps = [221, 234, 340, -9999, 230] # -9999 means "no valid data"; should be ignored
new_temps = [temp / 10 for temp in temps if temp != -9999] # list comprehension

print(new_temps)