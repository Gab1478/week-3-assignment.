# D1
def divider():
    print("="*34)
    
divider()
divider()


    # D2g
def greet_record(record_id):
    print(f"checking {record_id}")

greet_record("srv-01")
greet_record("srv-02")


# D3
def percent_of(part, total):
    """return part as a percentage of total"""
    return (part/ total)*100

result=percent_of(87,100)
print (result)
 
help(percent_of)


# D4
#the function will print 87.o but will not use return hence result will give you none.
def show_percent(part, total):
    print((part / total) * 100)

result = show_percent(87, 100)
print(result)

# D5
def within_limit(value, limit):
    return value <= limit
print(within_limit(87,100))
print(within_limit(100,87))
#they differ because 87 is less than 100 and 100 is more than 87.


# D6
def status_of(percent,warning_at=90):
    if percent>=100:
        return"OVERLIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return"OK"
print(status_of(95))
print(status_of(85))
print(status_of(85, 80))


    # D7
print(status_of(percent=95, warning_at=96))
print(status_of(warning_at=96, percent=95))
print(status_of(95, warning_at=96))
#line has an error because 96 has no keyword argument.


# D8
def total(numbers):
    return sum(numbers)
print (total(1,2,3))
print(total(10,20,30,40))
print(total())

# D9
def make_status():
    result = "OK"
    print("inside:", result)

make_status()
print("outside:", result)
#result was created inside the variable hence print() cannot access it because it is outside.


# D10
def double(n):
    n = n * 2
    return n

number = 21
print(double(number))
print(number)
#it remains 21 because changing n inside the function does not change number outside.


# D11
total = 100

def add_tax(price):
    price = price * 1.2
    return price

print(add_tax(total))
print(total)


# D12
def check_record(value, limit):
    difference=value-limit
    percent= (value/limit)*100
    return difference, percent
difference, percent=check_record(87.0,100.0)
print(difference)
print(percent)



# D13
import math
print(math.sqrt(16),
math.floor(24.8), round(math.pi,2))

# D14
import math
print (math.sqrt(81),
import random
print(random.randit(1, 6))
print(random.choice ({"OK", "WARNING","OVERLIMIT"}))


#D15
print(_name_)
def area_of_circle(radius)
    return math.pi* radius **2
if _name_=="_main_":
    print(round(area_of_circle(5), 2)
          )
#because they are outside the function.
