# Task 5: filter()

prices = [100, 250, 400, 1200, 50, 2000, 850]

greater = list(filter(lambda x: x > 500, prices))

smaller = list(filter(lambda x: x <= 500, prices))

print("Greater than 500")
print(greater)

print("Less than or equal to 500")
print(smaller)