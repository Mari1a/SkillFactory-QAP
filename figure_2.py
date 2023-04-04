from figure import Rectangle, Square, Circle
# далее создаем два прямоугольника
rest_1 = Rectangle(3,4)
rest_2 = Rectangle(12,5)
# вывод двух наших прямоугольников
print(f"прямоугольник №1 S= {rest_1.get_area()} прямоугольник №2 S={rest_2.get_area()}")

square_1 = Square(5)
square_2 = Square(10)
print(f"квадрат №1 S= {square_1.get_area_Square()},квадрат №2 S=  {square_2.get_area_Square()}")

сircle_1 = Circle(4)
сircle_2 = Circle(7)
print(f"S №1 круга = {сircle_1.get_area_Circle()} S №2 руга = {сircle_2.get_area_Circle()}")


figures = [rest_1, rest_2, square_1, square_2, сircle_1, сircle_2]
for figure in figures:
    if isinstance(figure, Square):
        print("S-квадратa", figure.get_area_Square())
    elif isinstance(figure,Circle):
        print("S- круга",figure.get_area_Circle())
    else:
        print("S-прямоугольника",figure.get_area())
        
 
