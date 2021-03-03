# sum = 0
# for data in range(1, 50):
#     if sum > 100:
#         break
#         pass
#     else:
#         sum += data
#         pass
# print(sum, data)

# for item in range(1, 101):
#     if item % 2 == 1:
#         continue
#         pass
#     else:
#         print(item, end=' ')
#         pass
for data in range(1, 100):
    if data == 50:
        break
        pass
    elif data % 2 == 0:
        continue
        pass
    else:
        print(data, end=' ')
