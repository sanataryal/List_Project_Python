from random import randint
user = []
while True:
    name = input("name: ")
    age = int(input("age: "))
    pw = input("pw: ")
    if age >= 18 and pw == "admin":
        ans = input("You are eligible to go inside, do you want to go? y/n : ")
        if ans == "y":
            print("added")
            user.append(name)
            print(user)
        elif ans=="n" and name == name in user:
            a = input("do you want to remove your name. y/n: ?")
            if a == "y":
                user.remove(name)
                print(user)
            else:
                print("No problem, thank you for your kind visit.The final list of users is:", user)
                break
    else:
        print("Invalid")
