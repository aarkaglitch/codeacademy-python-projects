# create the initial variables below
age = 35
smoker = 1
sex = 1
bmi = 27.3
num_of_children = 2 


# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
# Age Factor
print('wrt to age')
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")
age+=4
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost=new_insurance_cost-insurance_cost
print("Change in insurance cost is "+str(change_in_insurance_cost)+"dollars")
age=35
# BMI Factor
print('wrt to Bmi')
bmi+=3.1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost=new_insurance_cost-insurance_cost
print('new insurance cost '+str(new_insurance_cost)+" dollars")
change_in_insurance_cost=new_insurance_cost-insurance_cost
print("Change in insurance cost is "+str(change_in_insurance_cost)+"dollars")

# Male vs. Female Factor
print('change wrt to sex')
bmi=27.3
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
hange_in_insurance_cost=new_insurance_cost-insurance_cost
print('new insurance cost '+str(new_insurance_cost)+" dollars")
change_in_insurance_cost=new_insurance_cost-insurance_cost
print("Change in insurance cost is "+str(change_in_insurance_cost)+"dollars")
