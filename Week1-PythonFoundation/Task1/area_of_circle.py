# This proogram calculates area of a circle fom its radius

import math                                                             # Import math module to use pi
radius = float(input("enter the radius of circle: "))                   # takes radius from th user
area = math.pi*radius**2                                                # calculate area using  pi * radius squared
print("the area of circle with radius:", radius, "is:",area)            # prints the area