#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

import random

def generate_codes():
    three_digit_code = ''.join(str(random.randint(0, 9)) for _ in range(3))
    four_digit_code = ''.join(str(random.randint(1, 6)) for _ in range(4))
    print(f"Kolmenumeroinen koodi: {three_digit_code}")
    print(f"Nelinumeroinen koodi: {four_digit_code}")

generate_codes()