# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def your_function(your_input):
  ... # do something with the input
  return some_final_value
  returned_value = your_function(your_input)
# Write your code below: 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
print(f_to_c(100))
def c_to_f(c_temp):
  f_temp=c_temp* (9/5) + 32
  return f_temp
c0_in_fahrenheit=0
print(c_to_f(c0_in_fahrenheit))
def get_force(mass, accrelaration):
  return mass* accrelaration
print (get_force(train_mass,train_acceleration ))
train_force=get_force(train_mass,train_acceleration)
print("The GE train supplies" ,train_force,"Newtons of force")
def get_energy( mass):
  energy=mass*(3*10**8)
  return energy
bomb_mass=1
bomb_energy=get_energy(bomb_mass)
print("A 1kg bomb supplies", bomb_energy, "Joules.")
def get_work(mass,acceleration,distance):
  work=get_force(mass,acceleration)*distance
  return work
train_work=get_work(train_mass, train_acceleration,train_distance)
print("The GE train does",train_work,"Joules of work over" ,train_distance ,"meters.")
