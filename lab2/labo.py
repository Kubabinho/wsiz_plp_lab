from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 12, 13, 14]
result = [x ** 2 for x in numbers if x% 2==0]
print(result)

result1 = list(map(lambda x:x*2, numbers))

print(result1)

result2 = list(filter(lambda x:x%2==0, numbers))
print(result2)

total = reduce(lambda x,y: x+y, numbers)
print(total)


code = '''def hello(name):
    return "hello, "+ name
    

result3 = hello("Eniu")'''

exec(code)

print(result3)

a = 1
b = 50
input = "1+2+3*2+a+b"

output = eval(input)

print(output)