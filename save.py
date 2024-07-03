print("ArthmOpe:")
#ArthmOpe
a = 10
b = 5
sum = a + b
difference = a - b
product = a * b
quotient = a / b
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

print("ManipStr:")
#ManipStr
greeting = "Hello"
name = "World"
message = greeting + ", " + name + "!"
print(message)            
print(message.lower())    
print(message.upper())    
print(message[0:5])      
 

print("CondStat:")
 #Condstat
number = 10
if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")


print("Lists:")
#Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits)             
print(fruits[1])          
fruits[2] = "blueberry"
print(fruits)           


print("Dictionaries:")
#Dictionaries
student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science"
}
print(student["name"])  
student["age"] = 21
print(student)   


print("Tuples:")
#Tuples
coordinates = (10, 20)
print(coordinates) 
print(coordinates[0])