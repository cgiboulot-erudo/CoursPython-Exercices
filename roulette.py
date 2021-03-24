from random import randint

def roulette():
       number = -1;
       while (type(number) != type(0) or number < 0 or number > 49):
              number = input("Entrez un numéro (entre 0 et 49) : ")

              try:
                     number = int(number)
                     if number < 0 or number > 49:
                            print(f"Vous devez choisir un numéro entre 0 et 49. (Numéro choisi : {number})")
              except:
                     print("Veuillez renseigner un nombre.")

       print("-=-=-=-")

       mise = -1;
       while (type(mise) != type(0) or mise < 0):
              mise = input("Entrez votre mise (supérieur à 0) : ")

              try:
                     mise = int(mise)
                     if mise < 0:
                            print(f"Vous ne pouvez pas miser une somme inférieur à 0. (Votre mise : {mise})")
              except:
                     print("Veuillez renseigner un nombre.")

       print("-=-=-=-")

       is_pair = number % 2 == 0
       color = "rouge"
       if is_pair:
              color = "noir"
       print(f"Vous jouez pour le {number} {color} et vous misez {mise}")

       print("-=-=-=-")

       result = randint(0, 49)
       is_pair_result = result % 2 == 0
       res_color = "rouge"
       if is_pair_result:
              res_color = "noir"
       print(f"La bille sortie est le numéro {result} {res_color}")

       print("-=-=-=-")

       if number == result:
              print(f"Bravo vous avez gagné 3 fois votre mise ! (Gain : {3 * mise})")
       elif color == res_color:
              print(f"Dommage. Mais grâce au même couleur vous récupérez la moitié de votre mise. (Gain : {mise / 2})")
       else:
              print("Vous avez tout perdu. (Gain : 0)")

roulette()
