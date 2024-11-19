# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Loop through numbers from 20 to 50
for num in range(20, 51):
    if is_prime(num):
        print(f"{num} route bus is commutating Dehradun to Delhi.")
