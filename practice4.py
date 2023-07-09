def rev_string(x):
    return x[::-1]

def max_num(list):
    return max(list)

def mult_list(list):
    if len(list) == 0:
        return 0
    prod = list[0]

    if len(list) > 1:
        for i in list[1:]:
            prod = prod * i

    return prod


def num_within(num1,num2,number_range):
    if num1 <= number_range:
        if num2 <= number_range:
            return True
        else:
            return False
    else:
        return False

triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      length = len(row_prev)+1
      for i in range(length):
        if i == 0:
          row.append(1)
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    for row in triangle:
      print(row)



print(rev_string("Hello!"))
print(max_num([8,2,6]))
print(num_within(6,2,5))
print(mult_list([2,2,4]))
pascal(5)