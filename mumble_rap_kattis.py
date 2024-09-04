import re

antal = int(33)

sträng = "500kronorpåkontotmenmorsanhar5000"

nummer = re.findall(r'\d+', sträng)

integers = [int(num) for num in nummer]

högsta_integers = max(integers)

print(högsta_integers)