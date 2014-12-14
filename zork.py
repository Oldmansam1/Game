class luke1:
  def __init__(self, species, legs, color):
    self.species = species
    self.legs = legs
    self.color = color
        
luke = luke1('Doctor who fanatic', 2, 'white')
sam = luke1('Wizzard', 2, 'Perfectly tanned')
print('Lets learn about two muggles named Luke and Sam')
print('Say \'Ok\' if you would like to continue')
learn = input('Type here: ')
if learn == 'Ok':
  print('Alright then')
else:
  print('''Go away then...
    wait wait stay. I need to tell you and I won't let you leave.''')
print('I can tell you what species they are, how many legs the have, or what their nateraul skin color is!')
info_input = [sam.species, sam.legs, sam.color, luke.species, luke.legs, luke.color]
input_1 = input('Type \'species\', \'legs\', or \'color\':')
if input_1 == 'species':
  print('do you want to know about Luke or Sam?')
  input_1 = input('Type \'Luke\' or \'Sam\' to become an educated being: ')
  if input_1 == 'Sam':
    print(sam.species)
  if input_1 == 'Luke':
    print(luke.species)
elif input_1 == 'legs':
  print('do you want to know about luke or Sam?')
  if input_1 == 'Sam':
    print(sam.legs)
  if input_1 == 'Luke':
    print(luke.legs)
elif input_1 == 'color':
  print('do you want to know about luke or Sam?')
  if input_1 == 'Sam':
    print(sam.color)
  if input_1 == 'Luke':
    print(luke.color)
  

  

