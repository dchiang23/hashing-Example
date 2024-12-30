import random

def makeList(size: int, limit: int)->list[int]:
    list = []
    for i in range(limit):
        number = random.randint(1,size)
        list.append(number)
    return list

def findSumOperands(list_numbers: list[int], x: int)->list[tuple[int]]:
    """_summary_

    Args:
        list_numbers (list): list of numbers that we are checking for sum
        x (int): the sum that we want

    Returns:
        list[tuple]: returns a list of numbers that add up to x
    """
    in_list = {}
    unique_Pairs = set()

    for num in list_numbers:
        complement = x - num
        if complement in in_list:
            unique_Pairs.add(tuple(sorted((complement, num))))
        in_list[num] = True
    
    return list(unique_Pairs)

def main():
    test1 = findSumOperands(makeList(20,10000000),30)
    print(test1)
    test2 = findSumOperands(makeList(60, 100000), 40)
    print(test2)
    test3 = findSumOperands(makeList(10,100), 10)
    print(test3)
    test4 = findSumOperands(makeList(5,10),10)
    print(test4)

if __name__ == "__main__":
    main()

            


    