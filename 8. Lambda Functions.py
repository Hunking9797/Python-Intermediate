# lambda arguments: expression
# give 2d points as list of tuples sort them according to their y coordinates

points2D=[(1,2),(15,1),(5,-1),(10,4)]

# traditional way of sorting based on y coordinate
def sort_y_coordinates(x):
    return x[1]

points2D_sorted = sorted(points2D,key=sort_y_coordinates)
print(points2D)
print(points2D_sorted)

# sorting using lambda function
print('\nSorted using lambda function')
points2D_sorted = sorted(points2D,key=lambda x: x[1])
print(points2D_sorted)

# sorting according to sum of the coordinates
print('\nSorted based on sum of coordinates')
points2D_sorted_on_sum = sorted(points2D,key=lambda x: x[0]+x[1])
print(points2D_sorted_on_sum)
