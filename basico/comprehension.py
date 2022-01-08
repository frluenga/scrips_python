numbers = range(10)
print(numbers)
new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}

print(new_dict_comp)
