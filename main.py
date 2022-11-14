def fourth_place(*args):
  if len(args) > 3:
    return args[3]
  else:
    try:
      return args[3]
    except IndexError as error:
      print(error)
      print("The list is shorter than 4 items")

subtracter_lambda = lambda num_1, num_2: num_1 - num_2
(subtracter_lambda)(9, 5)

class Shoe:
  def __init__(self, US_size, color, smelly=False):
    self.US_size = US_size
    self.color = color
    self.smelly = smelly

  def euro_size(self):
    convert = self.US_size + 33
    print(f'Your size in European measurements is {convert} cm.')

my_shoe = Shoe(10, 'Black', smelly=False)
my_shoe.euro_size()

my_dads_shoe = Shoe(9, 'Blue', smelly=True)
my_dads_shoe.euro_size()
  