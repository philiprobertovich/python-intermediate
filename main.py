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