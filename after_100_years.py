name = raw_input("What is your name? ")
print("Your name is " + name + ". Is this correct?")

checking = raw_input().lower()

while checking != "yes":
    name = raw_input("Please enter your name: ")
    print("Your name is " + name + ". Is this correct?")
    checking = raw_input().lower()
    
age = raw_input("How old are you, " + name + "?")
print("Your are " + age + " years old. Is this correct?")

second_check = raw_input().lower()

while second_check != "yes":
    age = raw_input("Please enter your age: ")
    print("You are " + age + " years old. Is this correct?")
    second_check = raw_input().lower()
    
age_in_int = int(age)
sum = age_in_int + 100
print("In 100 years, you will be " + str(sum) + " years old.")