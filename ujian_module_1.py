#Question 1
# def calculate_years(principal,interest,tax,desired):
#     year=0
#     current_total=principal
#     while current_total<desired:
#         interest_earned=current_total*interest
#         tax_deducted=interest_earned*tax
#         current_total+=interest_earned-tax_deducted
#         year+=1
#     return year
# print(calculate_years(1000.00,0.05,0.18,1100.00))
# print(calculate_years(1200.00,0.17,0.05,2000.00))
# print(calculate_years(1500.00,0.07,0.6,5000.00))
# print(calculate_years(1500.00,0.07,0.6,1500.00))



#Question 2
# import math
# def expandedForm(num):
#     len_num=len(str(num))
#     final_list=[]
#     current_num=num
#     for i in range(len_num,-1,-1):
#         removed_num_digit=math.floor(current_num/(10**i))
#         current_num=current_num%(10**i)
#         removed_num=removed_num_digit*(10**i)
#         if removed_num==0:
#             pass
#         else:
#             final_list.append(removed_num)
#     output=""
#     for i in range(len(final_list)):
#         if i==len(final_list)-1:
#             output+=str(final_list[i])
#         else:
#             output+=str(final_list[i])+" + "
#     return output
# print(expandedForm(12))
# print(expandedForm(42))
# print(expandedForm(70304))
# print(expandedForm(70304000))



#Question 3
# def tower_builder(n_floors,block_size):
#     w, h=block_size
#     output=""
#     for i in range(n_floors):
#         for j in range(h):
#             for k in range((n_floors-i-1)*w):
#                 output+=" "
#             for k in range((i*2+1)*w):
#                 output+="*"
#             for k in range((n_floors-i-1)*w):
#                 output+=" "
#             output+="\n"
#     return output

# print(tower_builder(3,(2,3)))
# print(tower_builder(6,(2,1)))
