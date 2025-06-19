# Day 2: Input-Output, Print, and String Formatting in python.

# Topic 1: Input and Output in Python.
name= input("Enter your name:")                                             # input funcition সবসময় ‍string হিসেবে ইনপুট নেয়।
print("Hello", name)
print(f"Hello {name}")

# Topic 2: Type casting in python.
age=input("Enter your age:")                                                # যদি input নাম্বার হয়, তাহলে int() বা float() দিয়ে কনভার্ট করতে হবে।
print(type(age))                                                            # এটি str টাইপ হবে। কারন input ফাংশন সমসময় string হিসেবে েইনপুট নেয়।
age2=int(age)                                                               # এখন আমরা string কে int টাইপে কনভার্ট করলাম।
print(type(age2))
print("You are", age2, "years old.")
print(f"you are {age2} years old.")

# Topic 3: Print and String Formatting.
name= "Syfuddin"
age=22
print("My name is", name, "and I am", age, "years old.")                                      # সাধারন নিয়ম, print ফাংশন দিয়ে একাধিক ভ্যারিয়েবল প্রিন্ট করা যায়।
print(f"My name is {name} and I am {age} years old.")                                         # f-string ব্যবহার করে সহজে ফরম্যাট করা যায়।

# EXAMPLE:
num1=int(input("Enter first number: "))                          # input ফাংশন দিয়ে ইনপুট নেয়া হচ্ছে এবং int() দিয়ে কনভার্ট করা হচ্ছে।
num2=int(input("Enter second number: "))                         # input ফাংশন দিয়ে ইনপুট নেয়া হচ্ছে এবং int() দিয়ে কনভার্ট করা হচ্ছে।

"""num11=(input("Enter first number: "))                         #চাইলে উপরের মতোও করতে পারি। আবার triple কোটেশন ব্যবহার করে একাধিক লাইন কমেন্ট করা হয়েছে এভাবেও করতে পারবো।
num111=(input("Enter second number: "))                          #যেভাবেই করিনা কেন উওর একই হবে।
num1=int(num11)
num2=int(num111)"""

print("Sum:", num1 + num2)                                          # সাধারন নিয়মে প্রিন্ট করা হয়েছে।
print("Subtraction:", num1 - num2)                                  # সাধারন নিয়মে প্রিন্ট করা হয়েছে।
print("Multiplication:", num1 * num2)                               # সাধারন নিয়মে প্রিন্ট করা হয়েছে।
print("Division:", num1 / num2)                                     # সাধারন নিয়মে প্রিন্ট করা হয়েছে।
print("Modulus:", num1 % num2)                                      # সাধারন নিয়মে প্রিন্ট করা হয়েছে।


print(f"Sum: {num1 + num2}")                                        # f-string ব্যবহার করে প্রিন্ট করা হয়েছে।
print(f"Subtraction:{num1 - num2}")                                 # f-string ব্যবহার করে প্রিন্ট করা হয়েছে।
print(f"Multiplication: {num1 * num2}")                             # f-string ব্যবহার করে প্রিন্ট করা হয়েছে।
print(f"Division: {num1 / num2}")                                   # f-string ব্যবহার করে প্রিন্ট করা হয়েছে।
print(f"Modulus: {num1 % num2}")                                    # f-string ব্যবহার করে প্রিন্ট করা হয়েছে।


                                                                              # TASK:

                                                                              
# Question 1: ইউজারের নাম, বয়স, শহরের নাম ইনপুট নিন এবং নিচের মত প্রিন্ট করুন:আমি Rahim, আমার বয়স 22 এবং আমি Dhaka শহরে থাকি।
name = input ("Enter your name:")
age =int (input ("Enter your age:"))
city = input ("Enter your city:")
 
print("I am", name, ", I am ",age, "years old and I live in",city, ".")                           # সাধারন নিয়মে প্রিন্ট করা হয়েছে।
print(f"I am {name}, I am {age} years old and I live in {city}.")                                 # f-string ব্যবহার করে প্রিন্ট করা হয়েছে।

# Question 2: একটি ক্যালকুলেটর তৈরি করুন যেটা:ইউজার থেকে দুইটি সংখ্যা নিবে এবং যোগ, বিয়োগ, গুণ, ভাগ, ভাগশেষ করে রেজাল্ট দেখাবে।
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)                                         # সাধারন নিয়মে প্রিন্ট করা হয়েছে।
print("Subtraction:", num1 - num2)                                 # সাধারন নিয়মে প্রিন্ট করা হয়েছে।
print("Multiplication:", num1 * num2)                              # সাধারন নিয়মে প্রিন্ট করা হয়েছে।
print("Division:", num1 / num2)                                    # সাধারন নিয়মে প্রিন্ট করা হয়েছে।
print("Modulus:", num1 % num2)                                     # সাধারন নিয়মে প্রিন্ট করা হয়েছে।

print(f"Sum: {num1 + num2}")                                       # f-string ব্যবহার করে প্রিন্ট করা হয়েছে।
print(f"Subtraction: {num1 - num2}")                               # f-string ব্যবহার করে প্রিন্ট করা হয়েছে।
print(f"Multiplication: {num1 * num2}")                            # f-string ব্যবহার করে প্রিন্ট করা হয়েছে।
print(f"Division: {num1 / num2}")                                  # f-string ব্যবহার করে প্রিন্ট করা হয়েছে।
print(f"Modulus: {num1 % num2}")                                   # f-string ব্যবহার করে প্রিন্ট করা হয়েছে।