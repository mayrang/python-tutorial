result = 0
def add_numbers(num1, num2):
  global result
  result = num1 + num2
  return result

input1 = 30
input2 = 40
add_result = add_numbers(input1, input2)
print(f'{input1} + {input2} = {add_result}')
print(f'{input1} + {input2} = {result}')