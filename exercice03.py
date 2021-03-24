def is_product_negative(a, b):
    # Votre code ici
    return (a < 0 or b < 0) and (a > 0 or b > 0)

def run():
    assert is_product_negative(6, 7) == False
    assert is_product_negative(1, 0) == False
    assert is_product_negative(-1, 5) == True
    assert is_product_negative(1, -5) == True
    assert is_product_negative(-1, -5) == False
