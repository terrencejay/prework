def hello_name(user_name):
    print("Enter your name:")
user_name = input('Enter your name: ')
print('Hello, ' + user_name)

#practice code

userAge = input('Enter your age: ')
print(user_name + '! You are ' + userAge + ' years old!')
def first_odd():
    for i in range(1,101):
        if i % 2 != 0:
            print(i)
first_odd()

def max_num_in_list(a_list):
    maximum = a_list[0]
    for i in range(len(a_list)):
        if a_list[i] > maximum:
            maximum = a_list[i]
    return maximum
a_list = [10, 20, 30, 40, 50]
print(max_num_in_list(a_list))

def is_leap_year(a_year):
    if(a_year % 400 == 0):
        return print("leap year")
    elif a_year % 100 == 0:
        return print("not a leap year")
    # Checking if the year is divisible by 4.
    elif a_year% 4 == 0:
        return print("leap year")
    # Otherwise False
    else:
        return print("not a leap year")
# Asking the user to enter year 
a_year = int(input('what year is it? '))
# Calling function is_leap_year
print(is_leap_year(a_year))

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
# Driver Code
a_list = [2,3,4,5,6,7]
print(is_consecutive(a_list))
a_list = [1,2,4,5]
print(is_consecutive(a_list))


