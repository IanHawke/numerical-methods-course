nstrips = 4
width = 1/nstrips
integral = 0
for point in range(nstrips):
    height = (point/nstrips)**2
    integral = integral + width * height
print("The value is", integral)
