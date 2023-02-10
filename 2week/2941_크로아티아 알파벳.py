## 44 ms
Alphas = input()


Croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in Croatia :
    Alphas = Alphas.replace(i,"*")


print(len(Alphas))


## 이전 코드 (36ms)
# cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
#
# input_list = list(map(str, input()))
# input_list = input_list + ["0"] * 100
#
# count = 0
#
# i = 0
# for _ in range(len(input_list) + 5):
#     i = i
#
#     try:
#         if input_list[i] == "0":
#             break
#         else:
#             pass
#
#         if input_list[i] + input_list[i + 1] in cro_alpha:
#             if input_list[i] + input_list[i + 1] + input_list[i + 2] in cro_alpha:
#                 count += 1
#                 i += 3
#             else:
#                 count += 1
#                 i += 2
#         else:
#             if input_list[i] + input_list[i + 1] + input_list[i + 2] in cro_alpha:
#
#                 count += 1
#                 i += 3
#             else:
#                 count += 1
#                 i += 1
#     except:
#
#         break
#
# print(count)



