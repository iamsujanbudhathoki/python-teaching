ultimate_result= 8
base = 2
power = 0
current_loop_index = 1

while current_loop_index != 8:
    remainer = current_loop_index % base
    if remainer == 0:
        power = power + 1
    
    current_loop_index +=1

print(power)


print(base ** power)

