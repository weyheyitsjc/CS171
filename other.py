def pizza_maker(size, topping, *extra):
     print('%s inch pizza with %s' % (size, topping), end=' ')
     for other in extra:
          print(other, end='  ')
pizza_maker('16', 'pepperoni', 'mushroom')