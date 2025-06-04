cars = 100 #atribuindo um número inteiro
spaceInACar = 4.0 #atribuindo um número real
drivers = 30 #atribuindo um número inteiro
passengers = 90 #atribuindo um número inteiro
carsNotDriven = cars - drivers #operação aritmética entre inteiro e inteiro
carsDriven = drivers # atribuição de valor entre variáveis sem operação
carpoolCapacity = carsDriven * spaceInACar #atribuindo o resultado de uma operação aritmética entre inteiro e real
averagePassengersPerCar = passengers / carsDriven #atribuindo o resultado de uma operação aritmética entre inteiro e inteiro

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", carsNotDriven, "empty cars today.")
print("We can transport", carpoolCapacity, "people today.")
print( "We have", passengers, "to carpool today.")
print("We need to put about", averagePassengersPerCar, "in each car.")
print(10/5)
     