from dataclasses import dataclass

# 원래 이전 구현처럼 n n+1 뭐 이런 식으로 하려 했으나 기각 후 sign, n 가지는 구조체로 번경
@dataclass
class Point:
    """
    Point in added list. flag = true if the sign is in head
    """
    n: int
    flag: bool
    def __str__(self):
        if(self.flag):
            return f"({self.n})+"
        else:
            return f"({self.n})-"

"""
Argument given list by adding 0 to front, n+1 to end. 0 and n+1 is not affected by any reversals.
"""
def argument_list(arr: list[int]) -> list[int]:
    n : int = len(arr)
    arr2 : list[int] = [0] + arr
    arr2.append(n+1)
    return arr2

def extend_list(arr: list[int]) -> list[Point]:
    arr2 : list[Point] = []
    nmax = len(arr) - 2
    for n in arr:
        if(n == 0):
            arr2.append(Point(0, True))
        elif(n == nmax + 1):
            arr2.append(Point(n, False))
        else:
            arr2.append(Point(n, True))
            arr2.append(Point(n, False))
    return arr2

def main():
    print("Sorting signed permutation by reversals.")
    test_list: list[int] = [-3, -1, 4, 5, 2]
    argumented = argument_list(test_list)
    extended = extend_list(argumented)
    print(*extended)

if __name__ == "__main__":
    main()
