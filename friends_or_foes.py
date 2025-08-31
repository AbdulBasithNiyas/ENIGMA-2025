name = input()
honesty_arr = input().split()

print(honesty_arr)

dishonesty_count = 0

for x in honesty_arr:
    if x == 'D':
        dishonesty_count += 1

percentage = (dishonesty_count/len(honesty_arr))*100

print(percentage)

if percentage < 1.0:
    print('H')
else:
    print('D')
