def add(input1s):
    dig_scrap = input1s.split("add ")
    dig_refine = dig_scrap[-1]
    numbers = dig_refine.split(" and ")
    num_a = numbers[0]
    num_b = numbers[1]
    sum_ab = int(num_a) + int(num_b)
    return sum_ab

def plus(input1s):
    numbers = input1s.split(" plus ")
    num_a = numbers[0]
    num_b = numbers[1]
    sum_ab = int(num_a) + int(num_b)
    return sum_ab


#Subtraction


def diffandsub(input1s):
    dig_scrap = input1s.split("sub ")
    dig_refine = dig_scrap[-1]
    numbers = dig_refine.split(" and ")
    num_a = numbers[0]
    num_b = numbers[1]
    diff_ab = int(num_a) - int(num_b)
    return diff_ab

def diffandsubtract(input1s):
    dig_scrap = input1s.split("subtract ")
    dig_refine = dig_scrap[-1]
    numbers = dig_refine.split(" and ")
    num_a = numbers[0]
    num_b = numbers[1]
    diff_ab = int(num_a) - int(num_b)
    return diff_ab

def diffandminus(input1s):
    dig_scrap = input1s.split("minus ")
    dig_refine = dig_scrap[-1]
    numbers = dig_refine.split(" and ")
    num_a = numbers[0]
    num_b = numbers[1]
    diff_ab = int(num_a) - int(num_b)
    return diff_ab


def diffFromsub(input1s):
    dig_scrap = input1s.split("sub ")
    dig_refine = dig_scrap[-1]
    numbers = dig_refine.split(" from ")
    num_a = numbers[1]
    num_b = numbers[0]
    diff_ab = int(num_a) - int(num_b)
    return diff_ab

def diffFromsubtract(input1s):
    dig_scrap = input1s.split("subtract ")
    dig_refine = dig_scrap[-1]
    numbers = dig_refine.split(" from ")
    num_a = numbers[1]
    num_b = numbers[0]
    diff_ab = int(num_a) - int(num_b)
    return diff_ab

def diffFromminus(input1s):
    dig_scrap = input1s.split("minus ")
    dig_refine = dig_scrap[-1]
    numbers = dig_refine.split(" from ")
    num_a = numbers[1]
    num_b = numbers[0]
    diff_ab = int(num_a) - int(num_b)
    return diff_ab


# Multiplication

def multiply(input1s):
    dig_scrap = input1s.split("multiply ")
    dig_refine = dig_scrap[-1]
    numbers = dig_refine.split(" and ")
    num_a = numbers[0]
    num_b = numbers[1]
    product_ab = int(num_a) * int(num_b)
    return product_ab

# Division

def divideAnd(input1s):
    dig_scrap = input1s.split("divide ")
    dig_refine = dig_scrap[-1]
    numbers = dig_refine.split(" and ")
    num_a = numbers[0]
    num_b = numbers[1]
    product_ab = int(num_a) / int(num_b)
    return product_ab

def divideBy(input1s):
    dig_scrap = input1s.split("divide ")
    dig_refine = dig_scrap[-1]
    numbers = dig_refine.split(" by ")
    num_a = numbers[0]
    num_b = numbers[1]
    product_ab = int(num_a) / int(num_b)
    return product_ab

def divideFrom(input1s):
    dig_scrap = input1s.split("divide ")
    dig_refine = dig_scrap[-1]
    numbers = dig_refine.split(" from ")
    num_a = numbers[1]
    num_b = numbers[0]
    product_ab = int(num_a) / int(num_b)
    return product_ab
