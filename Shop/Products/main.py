list_columns = ['computers', 'mice', 'keyboards']
dict = {'computers': ['comp1', 'comp2', 'comp3'], 'mice': ['mouse1', 'mouse2', 'mouse3'], 'keyboards':['keyb1', 'keyb2', 'keyb3']}

# list= []

# for i in list_columns:
#     list_data = []
#     for data in dict[i]:
#         list_data.append(data)
#     list.append(list_data)

# print(list)

# list= []
# for column in dict:
#     list.append(dict[column])
# print(list)

list= []

for column in dict:
# each [] by column key name
    list_data = []
    for data in dict[column]:
        list_data.append(data)
    list.append(list_data)
# print(list) - [['comp1', 'comp2', 'comp3'], ['mouse1', 'mouse2', 'mouse3'], ['keyb1', 'keyb2', 'keyb3']]

list_data = []
for index in range(len(list[0])):
    list_pr = []
    for product_set in list:
        list_pr.append(product_set[index])
    list_data.append(list_pr)
print(list_data) #[['comp1', 'mouse1', 'keyb1'], ['comp2', 'mouse2', 'keyb2'], ['comp3', 'mouse3', 'keyb3']]
    