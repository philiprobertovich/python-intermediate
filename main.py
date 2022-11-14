def fourth_place(*args: list) -> list:
  """returns the fourth index item of a list

  Args:
      args: a list of items

  Returns:
      list: list index item
  """
  if len(args) > 3:
    return args[3]
  else:
    try:
      return args[3]
    except IndexError as error:
      print(error)
      print("The list is shorter than 4 items")

# Takes two numbers and subtracts one from the other
subtracter_lambda = lambda num_1, num_2: num_1 - num_2
(subtracter_lambda)(9, 5)

class Shoe:
  def __init__(self, US_size: int, color: str, smelly: bool =False) -> None:
    """Creates the Shoe class

    Args:
        US_size (int): size of the shoe
        color (str): color of the shoe
        smelly (bool, optional): whether the shoe is smelly or not. Defaults to False.
    """
    self.US_size = US_size
    self.color = color
    self.smelly = smelly

  def euro_size(self) -> str:
    """Converts a shoe size from US to Euro standards by adding 33

    Returns:
        str: A sentence telling the user what their shoe size is in european measurement standards
    """
    convert = self.US_size + 33
    print(f'Your size in European measurements is {convert} cm.')

my_shoe = Shoe(10, 'Black', smelly=False)
my_shoe.euro_size()

my_dads_shoe = Shoe(9, 'Blue', smelly=True)
my_dads_shoe.euro_size()

def galaxy(name: str, *space_debris: list, pluto_is_planet: bool =True, **planet_colors: dict) -> str:
  """Takes a name of the galaxy, a list of various space matter and objects, a boolean value whether Pluto is a planet, and a dictionary of planets and their colors, and produces a paragraph detailing all these arguements and how they make up the galaxy.

  Args:
      name (str): Name of the galaxy
      space_debris (list): List of various space objects and matter
      pluto_is_planet (bool, optional): A boolean variable of whether pluto is a planet or not. Defaults to True.
      planet_colors (dict): A dictionary of planets and their associated colors

  Returns:
      str: A paragraph of how all the different arguement comprise the galaxy
  """
  print(f'''
    The {name} is a galaxy in our universe. \n
    This galaxy contains vasts amounts of different 
    space matter including {space_debris}. \n
    In this galaxy, there are {len(planet_colors)} planets. \n
    Based on recent astronomical studies, astronomers have \n
    decided that the statement of Pluto being a planent is {pluto_is_planet}.  \n
    Here is a list of the planets and their colors:
  ''')
  for key in planet_colors.keys():
    print(f'''
    {key.capitalize()} is {planet_colors[key]}.
    ''')

galaxy(
  "Milky Way Galaxy", 
  'astroids', 
  'space dust', 
  'leprachauns', 
  mercury='gray',
  venus='yellowish white',
  earth='blue and green',
  mars='red',
  saturn='yellow-brown',
  jupiter='orange',
  uranus='light blue',
  neptune='deep see blue',
  pluto='brown'
)