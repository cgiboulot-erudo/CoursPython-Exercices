def is_number_correct(number):
    # Votre code ici
    result = number >= 10 and number <= 20
    diff = 0
    if result == False:
        if number < 10:
            diff = 10 - number
        elif number > 20:
            diff = 20 - number
    return (result, diff)

def run():
    assert is_number_correct(0) == (False, 10)
    assert is_number_correct(10) == (True, 0)
    assert is_number_correct(20) == (True, 0)
    assert is_number_correct(21) == (False, -1)
    assert is_number_correct(50) == (False, -30)
    assert is_number_correct(15) == (True, 0)
