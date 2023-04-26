a=int(input('Введите четырехзначное число  '))
a1=a%10
a=a//10
a2=a%10
a=a//10
a3=a%10
a=a//10
a4=a%10
a=a//10
result=a1*1000+a2*100+a3*10+a4
print(result)
b=input()