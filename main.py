import ru_local as ru

print(ru.intr)
petrol_gln = float(input())

petrol_ltr = petrol_gln * 3.7854                                # 1 gallon equals 3.7854 liters
oil_brl = petrol_gln / 19.5                                     # 1 barrel of oil equals 19.5 gallons of petrol
carbon_dioxide = petrol_gln * 20                                # 1 gallon of petrol equals 20 pounds of carbon dioxide
petrol_BTU = petrol_gln * 115_000                               # 1 gallon of petrol equals 115000 BTU
ethanol = petrol_BTU / 75_700                                   # 1 gallon of ethanol equals 75700 BTU
cost = petrol_gln * 3.00                                        # 1 gallon of petrol costs $3.00

print(ru.ptrl_lt, petrol_ltr)
print(ru.oil, oil_brl)
print(ru.crbn_dxd, carbon_dioxide)
print(ru.thnl, ethanol)
print(ru.cst, cost)

PTRL_PR_PRS = 0.8
PPL_NSK = 1_625_631
PPL_RUSSIA = 146_980_061
petrol_nsk = PTRL_PR_PRS * PPL_NSK
petrol_r_day = PTRL_PR_PRS * PPL_RUSSIA
petrol_r_year = petrol_r_day * 365
print(ru.ptrl_nsk, petrol_nsk)
print(ru.ptrl_r, petrol_r_year)
