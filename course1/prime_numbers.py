max_number = 20 # change this number to 1000 
prime_numbers = []
number=1

while number < max_number:
    count=0
    for i in range(1, len(prime_numbers)):
        if number % i == 0:
            count=count+1
    if count < 2:
        prime_numbers.append(number)                
    number = number +1

print(prime_numbers)    

    
