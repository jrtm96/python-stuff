
def is_divisible(a,b):  # This function is from our textbook section 6.4
    if a % b == 0:     # If a % b is 0
        return True    # this function returns "True",
    else:              # otherwise,
        return False   # it will return "False".

# now, we define is_power function which takes two arguments and will call is_divisible.
def is_power(a,b):  
    if a == 1 or a == b:# 2 base cases: that both take a true argument combined
  # the only positive integer with a power of '1' is '1', also, if 'a' is equal to 'b', 'a' is a power of 'b'
        return True
    elif b == 1:     #base case: so 'b' cannot be 1
        return False
    elif a == b:     #base case: also, if 'a' is equal to 'b', 'a' is a power of 'b'
        return True  # so funtion will return true
    elif not is_divisible(a,b):  # base case: calling previous defined function to argue these variables
        return False             # if the above call is True, will return False
    else:
        return is_power(int(a/b),b) # this is a recursive call, it calls itself.

#calling test cases
print ("is _power(10,2) returns: ", is_power(10,2))   # will return "False"
print ("is_power(27,3) returns: ", is_power(27,3))    # will return "True"
print ("is _power(1,1) returns: ", is_power(1,1))     # will return "True"
print ("is_power(10,1) returns: ", is_power(10,1))    # will return "False"
print ("is power(3,3) returns: ", is_power(3,3))      # will return "True"
