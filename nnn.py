def sum_divisors(n):
  sum = 0
  m = 1
  while m < n :
    if n%m == 0 :
      sum = sum + m
    else :
      m += 1
  return sum
x = int(input("Enter number: "))
print("Calculating..............")
print(sum_divisors(x))
