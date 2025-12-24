from dataclasses import dataclass
import math

INF: int = 10**20

# 원래 이전 구현처럼 n n+1 뭐 이런 식으로 하려 했으나 기각 후 sign, n 가지는 구조체로 번경
@dataclass
class Node:
    """
    Node(Point) in added list. flag = true if the sign is in head
    """
    n: int
    flag: bool
    M_minus: int
    m_minus: int
    M_plus: int
    m_plus: int
    rev: bool
    inQ_M: bool
    inQ_m: bool
    parent: 'Node' = None
    left: 'Node' = None
    right: 'Node' = None
    size: int  = 1
    def __init__(self, n, flag):
        self.n = n
        self.M_minus = -INF
        self.m_minus = 0
        self.rev = False
        self.inQ_M = True
        self.inQ_m = True
        self.left = None
        self.right = None
        self.flag = flag
        
    def __str__(self):
        if(self.flag):
            return f"[({self.n})+ left: {self.left}, right : {self.right}]"
        else:
            return f"[({self.n})- left : {self.left}, right : {self.right}]"
        
    def get_value(self):
        return self.n if self.flag else -self.n
   
def is_identity_pair(pi_i: Node, pi_j: Node) -> bool:
    """
    Check if two Nodes are identity pair
    
    |pi_i| - |pi_j| = 1
    :param pi_i: First Node
    :type pi_i: Node
    :param pi_j: Second Node
    :type pi_j: Node
    :return: Bool value indicating if they are identity pair
    :rtype: bool
    """
    return  abs(abs(pi_i.n) - abs(pi_j.n)) == 1

def is_good_pair(pi_i: Node, pi_j: Node) -> bool:
    """
    Checking if two Nodes form a good pair
    
    :param pi_i: First Node
    :type pi_i: Node
    :param pi_j: Second Node
    :type pi_j: Node
    :return: Bool value indicating if they are identity pair and has diffrent sign.
    :rtype: bool
    """
    if not is_identity_pair(pi_i , pi_j):
        return False
    sign_i = 1 if pi_i.flag else -1
    sign_j = 1 if pi_j.flag else -1
    return sign_i * sign_j < 0

def find_adjacencies(arr: list[int]) -> list[tuple[int, int]]:
    """
    Finding adjancencies
    
    :param arr: original permutation
    :type arr: list[int]
    :return: list of adjacencies
    :rtype: list[tuple[int, int]]
    """
    adj = []
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] == 1:
            adj.append((i, i+1))
    return adj

def argument_list(arr: list[int]) -> list[int]:
    """
    Argument given list by adding 0 to front, n+1 to end. 0 and n+1 is not affected by any reversals.
    """
    n : int = len(arr)
    arr2 : list[int] = [0] + arr
    arr2.append(n+1)
    return arr2

def extend_list(arr: list[int]) -> list[Node]:
    arr2 : list[Node] = []
    nmax = len(arr) - 1
    for n in arr:
        if(n == 0):
            arr2.append(Node(0, True))
        elif(n == nmax):
            arr2.append(Node(n, False))
        elif(n < 0):
            arr2.append(Node(n, True))
            arr2.append(Node(n, False))
        elif(n > 0):
            arr2.append(Node(n, False))
            arr2.append(Node(n, True))
    return arr2

def main():
    print("Sorting signed permutation by reversals.")
    test_list: list[int] = [-2, 3, 1]
    argumented = argument_list(test_list)
    print(*argumented)
    extended = extend_list(argumented)
    print(*extended)

if __name__ == "__main__":
    main()
