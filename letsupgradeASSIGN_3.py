
for i in range(1042000,702648205):
    order = len(str(i))
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        # print(sum)
        temp //= 10
    if i == sum:
        print(i,"is the First Armstrong Number")
        break
      

