# function to check if number is prime 
def isPrime(n: number):
if n <= 1
   return False
i = 2
while i <= Math.sqrt(n):
    if n % i == 0:
        return False
    i += 1    # i is a variable that holds the divisible number
return True


# function to display the prime numbers

def on_button_pressed_a():
    count = 0
    current number = 2
    while count < 10:
        if isPrime(current_number):
           basic.show_number(current_number)
           count += 1
        current_number += 1
        basic.pause(5000)


input.on_button_pressed(Button.A, on_button_pressed_a)




