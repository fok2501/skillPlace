# 1st program. Версия 2- исправлена задача №3
print("(9**0.5*5)=",9**0.5*5)
# 2st program
print("(9.99>9.98 and 1000!=1000.1) is ",9.99>9.98 and 1000!=1000.1)
# 3st program
print("(2*2+2)=",2*2+2)
print("(2*(2+2))=",2*(2+2))
print("(2*2+2)=(2*(2+2))? is",(2*2+2)==(2*(2+2))) # подправил
# 4st program
a=str(123.456); print(a,type(a)) #проверяем,что у нас стринг
print(float(a),type(float(a))) #перевели в число
b=float(a) ;print(b,type(b)) #проверили, что так тоже работатет
print("И вот решение=",int((b*10)%10))
print("А вот решение одной строкой=",int((float(a)*10)%10)) # и по идее нужно уйти от переменной "a", тогда

print("Финал решение одной строкой=",int((float(str(123.456))*10)%10))

print("а мб здесь ожидался такой ответ=",int((float('123.456')*10)%10))