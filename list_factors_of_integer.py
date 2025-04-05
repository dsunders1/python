def factors(number):
  factors_list = []
  for i in range(1, number + 1):
    if number % i == 0:
      factors_list.append(i)
  return factors_list

number = 80
print("Factors of", number, "are:", factors(number))
