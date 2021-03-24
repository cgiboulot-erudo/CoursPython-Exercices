def factorial(number):
    # Votre code ici
    fact = 1
    for i in range(1, abs(number) + 1):
        fact = fact * i
    return number / abs(number) * fact

def run():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(8) == 40320
    assert factorial(-8) == -40320