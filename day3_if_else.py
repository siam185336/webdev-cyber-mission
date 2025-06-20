# Day 3: if, else, elif and Nested Conditions in Python.

# Topic 1: Basic If Statement.
age=int(input("Enter your age:"))                         # এখানে অবশ্যই input funcition কে int এ convert করতে হবে। কারন input funcition সবসময় string হিসেবে output দিয়ে থাকে।
if age >= 18:                                             # যদি ইউজারের বয়স ১৮ বছর এর সমান বা বেশি হয়ে থাকে, তাহলে কাজ করবে অন্যথায় কাজ করবে না।
    print("You are eligable for Vote.")

# Topic 2: If-Else Statement.
age=int(input("How old are you?"))
if age >= 18:
    print("You are adult")
else:
    print("You are Minor")

# Topic 3: If-Elif-Else Statement.
marks=int(input("Enter your mark:"))
if marks >=80:
    print("Congratulations, you got an \"A+\"")
elif marks >=70:
    print("Congratulations, you got an\"A\"")
elif marks >=60:
    print("Congratulations, you got an \"A-\"")
else:
    print("You are \"Fail\"")

# Topic 4: Nested if statement.
user=input("Username:")
password=int(input("Password:"))

if user == "admin":                
    if password == 1234:                #(১) এই প্রোগ্রামে elif ব্যবহার করা যেত না,কারণ প্রতিটি শর্ত আলাদা স্তরে (nested) আছে।প্রথম if চেক করছে ইউজারনেম ঠিক আছে কি না।যদি ঠিক থাকে, তাহলে তার ভেতরেই আরেকটা if দিয়ে পাসওয়ার্ড যাচাই করা হচ্ছে।
        print("Login Successful!")      # elif ব্যবহার করা যায় যখন একই স্তরে একাধিক শর্ত পরীক্ষা করতে চাই। কিন্তু এখানে যেহেতু দ্বিতীয় শর্তটি (পাসওয়ার্ড যাচাই) শুধু তখনই পরীক্ষা করা হবে যখন প্রথম শর্ত (ইউজারনেম যাচাই) সত্য হবে, তাই এখানে nested if ব্যবহার করা হয়েছে।কিছুটা gmail এর মতো, প্রথমে ইউজারনেম চেক করে, তারপর পাসওয়ার্ড চেক করে তার মতোই কাজ করছে।
    else:                               
        print("Wrong Password")
else:
    print("Wrong Username")            #(১) না, যদি username ভুল হয়, তাহলে password চাইবেই না। কিন্তু এখানে চাচ্ছে কারন আমরা username & password প্রথমেই input নিয়েছি।


# যদি তুমি চাও — username ঠিক হলে তবেই password চাওয়া হোক, তাহলে কোডটা এমনভাবে লিখতে হবে:
user = input("Username: ")

if user == "admin":
    password = input("Password: ")
    if password == "1234":
        print("Login Successful!")
    else:
        print("Wrong Password")
else:
    print("Wrong Username")

#এমন একটা কোড if elif else দিয়ে বানাতে চাই তাহলে:
user = input("Username:")
password = input("Password:")

if user == "admin" and password == "1234":
    print("Login Successful!")
elif user != "admin" and password == "1234":
    print("Wrong Username")
elif user == "admin" and password != "1234":
    print("Wrong Password")
else:
    print("Wrong Username and Password")

                                                                          # TASK:


# Question 1 :ইউজার থেকে বয়স নিয়ে ঠিক করুন সে প্রাপ্তবয়স্ক কিনা (18+ হলে)।
age=int(input("Enter your age:"))
if age>=18:
    print("You are Adult")
else:
    print("You are Minor")

# Question 2 :মার্কস নিয়ে গ্রেড সিস্টেম করুন (A+, A, A-, F).
mark=int(input("Enter your mark:"))
if mark >=80:
    if mark>90:
        print("Congratulations,You are the Best👍")
    print("A+")
elif mark >=70:
    print("A")
elif mark>=60:
    print("A-")
else:
    print("Sorry you are Fail!")

# কোড আরও clean/readable করতে চাইলে ভেতরের if mark > 90: অংশকে আলাদা করে প্রথমেই বসানো যেত, যেমন:

# if mark > 90:
#     print("Congratulations, You are the Best👍")
#     print("A+")
# elif mark >= 80:
#     print("A+")
# ...

# Question 3 : দুইটি সংখ্যা ইনপুট নিয়ে বড়টা বের করুন।
num1=input("Entern your 1st number:")
num2=input("Entern your 2nd number:")
if num1>num2:
    print("The big number is:",num1)
elif num1<num2:
    print("The big number is:",num2)
else:
    print("Two number are equal")

# Question 4 : লগইন সিস্টেম বানান (username & password চেক করে)
        # উপরে তিন ভাবে বানানো হয়েছে এখন আমি আমার মন মতো করে বানাচ্ছি।
username=input("Enter your username:")
if username == "siam185":
    password=input("Enter your password:")
    if password == "252663":
        print("Login Sucessfully.")
    else:
        print("Wrong Password")
else:
    print("Wrong Username.")

# Question 5 : Even/Odd Checker with Message.
number=int(input("Enter your value:"))
if number % 2 ==0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Question 6 :বয়স অনুযায়ী সিনার বা জুনিয়র নির্ধারণ|
age=int(input("Enter your age:"))
if age> 60:
    print("Senior Citizen.")
elif age>=18:
    print("Adult")
else:
    print("Minor")