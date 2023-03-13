import ru_local as ru

print(ru.INTR)
petrol_gln = float(input())

'''
1 gallon equals 3.7854 liters.
1 barrel of oil equals 19.5 gallons of petrol.
1 gallon of petrol equals 20 pounds of carbon dioxide.
1 gallon of petrol equals 115000 BTU.
1 gallon of ethanol equals 75700 BTU.
1 gallon of petrol costs $3.00.
'''

petrol_ltr = petrol_gln * 3.7854
oil_brl = petrol_gln / 19.5
carbon_dioxide = petrol_gln * 20
petrol_BTU = petrol_gln * 115_000
ethanol = petrol_BTU / 75_700
cost = petrol_gln * 3.00

print(ru.PTRL_LT, petrol_ltr)
print(ru.OIL, oil_brl)
print(ru.CRBN_DXD, carbon_dioxide)
print(ru.THNL, ethanol)
print(ru.CST, cost)

PTRL_PR_PRS = 0.8
PPL_NSK = 1_625_631
PPL_RUSSIA = 146_980_061
petrol_nsk = PTRL_PR_PRS * PPL_NSK
petrol_r_day = PTRL_PR_PRS * PPL_RUSSIA
petrol_r_year = petrol_r_day * 365

print(ru.PTRL_NSK, petrol_nsk)
print(ru.PTRL_R, petrol_r_year)
