def tri(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "not a triangle"
    print(" forms a triangle")
    if a == b == c:
        print("Equilateral triangle.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Right-angled triangle")
    elif a == b or b == c or a == c:
        print(" Isosceles triangle")
    else:
       pass
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
result =tri(a, b, c)
print(result)