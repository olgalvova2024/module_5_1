class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self,new_floor):
            if new_floor <= self.number_of_floors:
                i = 1
                while i <= new_floor:
                    print(i)
                    i += 1
            else:
                print('Такого этажа не существует')

h1 = House('Московский', 9)
h2 = House('Самоцветы',15)

print(h1.name,h1.number_of_floors)
h1.go_to(8)
print(h2.name,h2.number_of_floors)
h1.go_to(20)







