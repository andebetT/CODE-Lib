def is_power_of(number,base):
    if number<base and number!=1:
        return False
    if number==base or number==1:
        return True
    return is_power_of(number/base,base)
print(is_power_of(1,4))