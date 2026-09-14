
# 5. Cylinder Surface Painting Cost
rate_of_painting_per_sq_ft = 20
pi = 3.14159

# Taking sample inputs since radius and height are not provided in the problem statement
radius = 5
height = 10

# Curved surface area formula: 2 * pi * r * h
curved_surface_area = 2 * pi * radius * height
total_painting_cost = curved_surface_area * rate_of_painting_per_sq_ft

print("Total painting cost:", round(total_painting_cost, 2), "Rupees")
