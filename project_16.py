##### calculate the water bill for each family in an apartment


Apartment = {1:5,2:3,3:6,4:2,5:1,6:4,7:3,8:2}

cost = int(input("enter the cost of water use of the apartment: "))
ppl = 0

for first_for in range(1,9):
    p = Apartment[first_for]
    ppl += p

EMC = cost / ppl

for second_for in range(1,9):
    p_1 = Apartment[second_for]
    CPF = p_1*EMC
    print(f'the cost of water used for\n\rfamiliy number {second_for} that they contain {Apartment[second_for]} person is: %6.4f' %CPF +'\n')


#############

# Apartment = {1:5,2:3,3:6,4:2,5:1,6:4,7:3,8:2}

# cost = int(input("enter the cost of water use of the apartment: "))
# count = 1
# ppl = 0
# while count <= 8:
#     for first_for in range(1,9):
#         M = Apartment[first_for]
#         ppl += M
#     EMC = cost / ppl
#     M_1 = Apartment[count]
#     CPF = p_1*EMC
#     print(f'the cost of water used for familiy number {count} is: %6.4f' %CPF)
#     count += 1

# print("done!")
