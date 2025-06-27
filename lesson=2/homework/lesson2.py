name = (input ('whats your name:? '))
date_of_birth = (input('whats your date of birht:? ')) 
current_date = 2025
age = current_date - date_of_birth
print ('Name:',name)
print ('Age:' ,age)


txt = 'LMaasleitbtui'
car_names = ['audi','bmw','tesla','chevrolet','toyota'] 
found_cars = []
for car in car_names:
    if all (char in txt for char in car) :
        found_cars.append (car)
        print ('found car names:', found_cars)



txt = 'MsaatmiazD'
car_names = ['audi','bmw','tesla','chevrolet','toyota','nissan','mazda','matiz'] 
found_cars = []
for car in car_names:
    if all (char in txt for char in car) :
        found_cars.append (car)
        print ('found car names:', found_cars)


name = ['ilhom','yusuf']
name.reverse()
print (name)
