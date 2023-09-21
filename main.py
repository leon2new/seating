import random
import excel

path = 'tab.xlsx'
my_class_list = excel.excel_import(path)
лоаплгыв



number_desks = [4, 5, 5]
total_desks = sum(number_desks)
max_dist = 2
row_count = len(number_desks)
max_desks = max(number_desks)

desks = []






for element in number_desks:
    i = 0
    temp_row = []
    while i < max_desks:
        if i < element:
            temp_row.append([1, 1])
        else:
            temp_row.append([0, 0])
        desks.append(temp_row)
        i +=1
print(desks)



#
#     j = 0
#     while j < len(number_desks):
#         if j < number_desks[i]:
#             temp_ordinary.append([1, 1])
#         else:
#             temp_ordinary.append([0, 0])
#
#
#
#
#
#     temp_favorite = []
#     temp_ordinary = []
#     j = 0
#     while j < max_desks:
#         if j <= (max_dist - 1):
#             temp_favorite.append([1, 1])
#         else:
#             if j < number_desks[i]:
#                 temp_ordinary.append([1, 1])
#             else:
#                 temp_ordinary.append([0, 0])
#         j += 1
#     vip_desks.append(temp_favorite)
#     ordinary_desks.append(temp_ordinary)
#     i += 1
# # print(vip_desks)
# # print(ordinary_desks)
#
# favorite_student = []
# ordinary_student = []
# favorite_girls = []
# favorite_boys = []
# ordinary_girls = []
# ordinary_boys = []
# favorite_student_coints = 0
# ordinary_student_coints = 0
#
# student_coints = len(my_class_list)
# # print(student_coints)
# i = 0
# while i < student_coints:
#     if my_class_list[i][2] in [1]:
#         favorite_student.append(my_class_list[i][:2])
#         favorite_student_coints += 1
#     else:
#         ordinary_student.append(my_class_list[i][:2])
#         ordinary_student_coints += 1
#     i += 1
# # print("Избранные ", favorite_student)
# # print(favorite_student_coints)
# # print("Обычные ", ordinary_student)
# # print(ordinary_student_coints)
#
# # Разделим favorite_student список на мальчиков и девочек, Создадим функцию для этого
# for student in favorite_student:
#     if student[1] == 'f':
#         favorite_girls.append(student[0])
#     else:
#         favorite_boys.append(student[0])
# for student in ordinary_student:
#     if student[1] == 'f':
#         ordinary_girls.append(student[0])
#     else:
#         ordinary_boys.append(student[0])
#
# # начнем рассадку детей
# # определим сколько у нас есть вип мест
#
# vip_place_coint: int = max_dist * 3 * 2
# # print(vip_place_coint)
# # print(favorite_girls)
#
# # Сравним количество vip детей и мест
# vip_place_count = max_dist * 3 * 2
#
# random.shuffle(ordinary_boys)
# random.shuffle(ordinary_girls)