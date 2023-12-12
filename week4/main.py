from math_operations import basic_operations, power_operation
#test basic_operation
result_basic = basic_operations(10,5)
print("Basic operation result:", result_basic)
#Test power_operation
result_power = power_operation(2, 3)
print("Power Operation Result:", result_power)
# Test power_operation with modulo
result_power_modulo = power_operation(2, 3, modulo=5)
print("Power Operation with Modulo Result:", result_power_modulo)
