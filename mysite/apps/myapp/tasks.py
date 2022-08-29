import random
from celery import shared_task
from datetime import datetime
# @shared_task(name="sum_two_numbers")
# def add(x, y):
#     return x + y

# @shared_task(name="multiply_two_numbers")
# def mul(x, y):
#     total = x * (y * random.randint(3, 100))
#     return total

# @shared_task(name="sum_list_numbers")
# def xsum(numbers):
#     return sum(numbers)

@shared_task
def periodic():
    # current_time = datetime.now()
    print("Schedule Task")
    # print(current_time)
    
@shared_task
def add(a,b):
    return a+b
    
