import sys
sys.path.append("/home/bebopkenny/cpsc233p/hw5/")

from mathematics import whoami as math_whoami
from mathematics.numbers import series, simple
from mathematics.geometry import circle, cube, rectangle

def main():
    # Test mathematics.whoami
    print(math_whoami.getname())
    
    # Test series module
    print(series.sum(list=[1, 2, 3, 4]))
    print(series.average(list=[1, 2, 3, 4]))

    # Test simple operations
    print(simple.addition(left=5, right=3))
    print(simple.subtraction(left=5, right=3))
    print(simple.multiplication(left=5, right=3))
    print(simple.division(left=6, right=3))

    # Test rectangle module
    print(rectangle.perimeter(length=5, width=3))
    print(rectangle.area(length=5, width=3))

    # Test circle module
    print(circle.circumference(radius=5))
    print(circle.area(radius=5))

    # Test cube module
    print(cube.surface_area(side=3))
    print(cube.volume(side=3))

if __name__ == "__main__":
    main()