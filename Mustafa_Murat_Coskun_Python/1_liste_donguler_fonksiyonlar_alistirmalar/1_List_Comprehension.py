

#List Comprehension :Listeleri Anlama
#Listeler üzerinde gerçekleştirilen işlemleri kısa kod blokları ile çözer.


#CTRL + K + U Yorum satırı geri getirme
#CTRL + K + C Yorum satırı yapma


ugurlu_sayilar=[307,1844,571,1453]

def new_salary(x):
    return x

# null_list=[]

# for sayilar in ugurlu_sayilar:
#     null_list.append(new_salary(sayilar))
    
# print(null_list)



############################################################################################

# null_list=[]
# null_list1=[]
# for sayilar in  ugurlu_sayilar:
#     if sayilar >600:
#         null_list.append(new_salary(sayilar))


        
#     else:
#         null_list1.append(new_salary(sayilar*2))
        
# print(null_list)
# print(null_list1)
#############################################################################################


a=[new_salary(sayilar*2)  if sayilar >600 else new_salary(sayilar) for sayilar in ugurlu_sayilar]  
print( a)

##############################################################################################


