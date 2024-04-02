def double(x: int) -> int: 
    return x * 2


def double_display(y: int): 
    print(y * 2)


double_display(2)

if __name__ == "__main__":
    print(double(3))

from b.a import double, double_display 

print(double(1))
double_display(4)