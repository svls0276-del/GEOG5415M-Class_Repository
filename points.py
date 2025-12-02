# points.py
# A simple py file that contains a list of points and a function that reads
# the list and returns the points

# ****************** EDIT BELOW ******************
# Add your point as a new item in the list. 
# Create a new line for your point, and don't forget the square brackets and the comma
# Poinst should be in the following format:
# [ latitude, longitude, "description" ],

points_list = [
    [  53.808478, -1.5527924, "University of Leeds" ],
    [  53.840032, -1.6432286, "Nick's neighbourhood" ],
    

    # Add more points here

    # [ latitude, longitude, "description" ],
    # [ latitude, longitude, "description" ],
    [  53.814665, -1.6376061, "Fran's favourite bakery"],
    
    [  53.800622, -1.5483202, "The Leeds Art Gallery!" ],
    [  53.798874, -1.5408800, "Rayan's Favourite Japanese Restaurant" ],

]

def get_points():
    """Return the list of points"""
    return points_list
