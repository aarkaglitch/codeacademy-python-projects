# Add your code here
def analyse_smoker(smoker_status):
  print("the smoker status is "+str(smoker_status))
  if smoker_status==1:
    print("To lower your costs, you should consider quitting smoking")
  else:
    print("smoking for you is not and issue")
def analyse_bmi(bmi_value):
  print("Bmi value is"+str(bmi_value))
  if bmi_value>=30:
    print("Eat a salad you fat fuck")
  elif bmi_value>=25 and bmi_value<30:
    print("You should reduce your weight to reduce your insurance costs")
  elif bmi_value>=18.5 and bmi_value<25:
    print ("you are in the healthy BMI range")
  else :
    print ("you should gain weight to reduce your insurance costs")
        

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyse_smoker(smoker)
  analyse_bmi(bmi)
  return estimated_cost
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)
aarka_insurance_cost=estimate_insurance_cost(name="Aarka",age=29,sex=1,bmi=23,num_of_children=0,smoker=1)
