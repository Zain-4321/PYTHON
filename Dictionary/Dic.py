# DICTIONARY

# chai_types={"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
# print(chai_types["Green"])

# chai_types={"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
# chai_types["Green"]="Fresh"
# print(chai_types)

# AISA KARNAY SE SIRF KEY MILTI HAI
# chai_types={"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
# for chai in chai_types:
#   print(chai)

# yeh key or value dono dayga
# chai_types={"Masala":"Spicy","Ginger":"Zesty","Green":"Mild","Coffee":"Black"}
# for chai in chai_types:
#   print(chai,chai_types[chai])


# DOSRA TAREEQA YE HAI 
# chai_types={"Masala":"Spicy","Ginger":"Zesty","Green":"Mild","Coffee":"Black"}
# for key,value in chai_types.items():
#   print(key,value)

# chai_types={"Masala":"Spicy","Ginger":"Zesty","Green":"Mild","Coffee":"Black"}
# if "Masala" in chai_types:
#   print("Yes,I have Masala Chai")


# ADDING VALUE KEY
# chai_types={"Masala":"Spicy","Ginger":"Zesty","Green":"Mild","Coffee":"Black"}
# chai_types["Earl Grey"]="Citrus"
# print(chai_types)

# squared_num={x:x**2 for x in range(6)}
# print(squared_num)

# SAB KO CLEAR KARDAYGA
# squared_num={x:x**2 for x in range(6)}
# print(squared_num.clear())

# ismain hum nai mukhtalif key ko ek value assign kardi
key=["Biryani","Qorma","Nihari"]
default_value="Delicious"
new_dic=dict.fromkeys(key,default_value)
print(new_dic)