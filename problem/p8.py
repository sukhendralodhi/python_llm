

def euclidean_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points in 2D space.
    
    Parameters:
    point1 (tuple): A tuple representing the coordinates of the first point (x1, y1).
    point2 (tuple): A tuple representing the coordinates of the second point (x2, y2).
    
    Returns:
    float: The Euclidean distance between the two points.
    """
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance


# Example usage:
point_a = (3, 4)
point_b = (7, 1)
result = euclidean_distance(point_a, point_b)
print(f"The Euclidean distance between {point_a} and {point_b} is: {result}")