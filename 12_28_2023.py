def is_armstrong_number(num):
    original_num = num  # Save the original number for comparison later
    i = 0
    while num > 0:
        num //= 10
        i += 1

    return required_sum(original_num, i) == original_num

def required_sum(num, i):
    s = 0
    
    while num > 0:
        digit = num % 10
        num //= 10
        s += pow(digit, i)
        
    return s
