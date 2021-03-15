N = input()
points = input()

# string to list
points = points.split()

points = [int(i) for i in points]

maximum_value = max(points)

modified_points = list()

for i in range(len(points)):
    value = (points[i] / maximum_value) * 100
    modified_points.append(value)

average = sum(modified_points, 0.0) / len(modified_points)
print(average)

