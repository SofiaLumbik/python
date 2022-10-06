name = str(input ('Введите имя'))
surname = str(input('Введите фамилию'))
birthyear = int(input('Введите год рождения'))
print (name,"_",surname,"_",birthyear)
name,surname = surname,name #меняем имя и фамилию местами
birthyear = birthyear+60 #прибавляем 60 к году рождения
print (name,surname,birthyear)