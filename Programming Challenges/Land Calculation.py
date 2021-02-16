land_size = int(input("Enter land size in Sqr meter: "))

convert_to_acre = (land_size/43560) * 1

print("Acers: " + format(convert_to_acre, ".2f"))
