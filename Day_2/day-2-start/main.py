# #Data Types
# #Strings
# print("Hello World"[8])
# print("123" + "345")
# print(len("Hello World"))

# #Integers
# print(123 + 345)
# 123_456_789  #underscores in numbers it is same as 123,456,789
# # print(len(123)) it gives an error because len() function is used for strings only

# #Floats
# 123.45

# #Booleans
# True
# False

# #Functions
# #Type() function
# num_char = len(input("What is your name? "))
# print(type(num_char))

# #Type conversion
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters")

# print(70 + float("100.5"))
# print(str(70) + str(100))

# #Mathematical Operations
# 2 + 3
# 7 - 4
# 3 * 2
# 4 / 2
# 2 ** 3

# # PEMDASLR: () ** * / + - (Parentheses, Exponents, Multiplication and Division, Addition and Subtraction)
# print(3 * (3 + 3) / 3 - 3)

print(8 / 3)
print(round(8 / 3))
print(round(8 / 3, 2))
print(2.666666666, 2)
print(8 // 3)  #floor division
print(type(8 // 3))
print(type(4 / 2))

results = 4 / 2
results /= 2
print(results)

score = 0
score += 1
print(score)
print("Your score is " + str(score))

score = 0
height = 1.8
iswinning = True
print("Your score is " + str(score) + " your height is " + str(height) +
      " you are winning is " + str(iswinning))
print(
    f"Your score is {score}, your height is {height}, you are winning is {iswinning}"
)
