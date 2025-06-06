def sphere_volume(radius):
    volume = (4 / 3) * 3.14 * (radius ** 3)  
    return volume  

radius = float(input("Enter radius: "))

print("Volume is :", round(sphere_volume(radius), 2))
