# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name,age,sex,bmi,num_of_children,smoker):
  estimated_cost=250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated cost for " + name + " is "+str(estimated_cost) + "dollars.")

# Initial variables for Maria 

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("Maria",20,0,26.2,3,0)


# Initial variables for Omar


# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost("Omar",35,1,22.2,0,1)
