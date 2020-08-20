nstrips = 10
width = 1/nstrips
integral = 0
for point in range(nstrips):
    height = (point/nstrips+0.5*width)**2
    integral = integral + width * height
print("The value is", integral)
