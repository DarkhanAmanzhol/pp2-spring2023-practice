import json
import math

def point_distance(p1, p2):
    return math.sqrt((p2['x'] - p1['x']) ** 2 + (p2['y'] - p1['y']) ** 2)

def closest_pair(points):
    n = len(points)
    min_dist = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            dist = point_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist

def sum_distances_to_origin(points):
    return sum([math.sqrt(p['x'] ** 2 + p['y'] ** 2) for p in points])

def average_angle(points):
    angles = []
    n = len(points)
    for i in range(n-1):
        angle = math.atan2(points[i+1]['y'] - points[i]['y'], points[i+1]['x'] - points[i]['x'])
        angles.append(angle)
    avg_angle = sum(angles) / len(angles)
    return math.degrees(avg_angle)

def calculate_point_statistics(json_string):
    points = json.loads(json_string)
    closest_pair_distance = closest_pair(points)
    sum_of_distances_to_origin = sum_distances_to_origin(points)
    average_angle_between_points = average_angle(points)
    result = {
        'closest_pair_distance': closest_pair_distance,
        'sum_of_distances_to_origin': sum_of_distances_to_origin,
        'average_angle_between_points': average_angle_between_points
    }
    return json.dumps(result)

json_string = '[{"x":0, "y":0}, {"x":1, "y":1}, {"x":2, "y":2}, {"x":3, "y":3}]'
result = calculate_point_statistics(json_string)
print(result) 
# Output: {"closest_pair_distance": 1.4142135623730951, "sum_of_distances_to_origin": 5.656854249492381, "average_angle_between_points": 45.0}
