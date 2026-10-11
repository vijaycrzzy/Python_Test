int_val = 42
float_val=10.5
num_for_str=10
str_num = "250"
zero_val = 0
nonzero_val = 7

int_to_float=float(int_val)
print(f"Integer to floating-point number : {int_val} ({type(int_val).__name__}) -> {int_to_float} ({type(int_to_float).__name__})")

float_to_int=int(float_val)
print(f"floating-point number to Integer : {float_val} ({type(float_val).__name__}) -> {float_to_int} ({type(float_to_int).__name__})")

int_to_str=str(num_for_str)
print(f"Integer to String : {num_for_str} ({type(num_for_str).__name__}) -> {int_to_str} ({type(int_to_str).__name__})")

str_to_int = int(str_num)
print(f"String to Integer:  '{str_num}' ({type(str_num).__name__}) -> {str_to_int} ({type(str_to_int).__name__})")

zeroval_to_bool= bool(zero_val)
nonzeroval_to_bool= bool(nonzero_val)
print(f"Integer to Boolean : {zero_val} ({type(zero_val).__name__}) -> {zeroval_to_bool} ({type(zeroval_to_bool).__name__})")
print(f"Integer to Boolean : {nonzero_val} ({type(nonzero_val).__name__}) -> {nonzeroval_to_bool} ({type(nonzeroval_to_bool).__name__})")