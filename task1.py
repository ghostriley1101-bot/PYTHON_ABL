
total = int(input("Total classes: "))
attended = int(input("Classes attended: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details")
else:
    percentage = attended / total * 100
    extra = 0

    while percentage < 75:
        total += 1
        attended += 1
        extra += 1
        percentage = attended / total * 100

    print("Classes needed:", extra)
    print("Final attendance:", round(percentage, 2))
