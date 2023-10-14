start = int(input("enter the start of a range "))
end = int(input("enter the end of a range "))

even_sum = 0

for num in range(start, end + 1):
               if num % 2 == 0:
                       even_sum += num

print(f"the sum of even number in range {start} to {end} is: {even_sum}")