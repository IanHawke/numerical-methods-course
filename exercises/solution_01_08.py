nstrips = 100
width = 1/nstrips
integral = 0
for point in range(nstrips):
    height = (1 - (point/nstrips)**2)**(1/2)
    integral = integral + width * height
print("The value is", integral)
