weight =5
#ground shipping
def ground_shipping(weight):
  if weight <=2:
    ground_ship=20+(weight*1.5)
  elif weight >=2 and weight <=6:
    ground_ship=20+(weight*3)
  elif weight >=6 and weight <=10:
    ground_ship=20+(weight*4)
  else :
    ground_ship=20+(weight*4.75)
  return ground_ship
print (ground_shipping(8.4))
#premium ground shipping 
premium_ground_shipping=125
#ground shipping
def ground_shipping(weight):
  if weight <=2:
    ground_ship=20+(weight*1.5)
  elif weight >=2 and weight <=6:
    ground_ship=20+(weight*3)
  elif weight >=6 and weight <=10:
    ground_ship=20+(weight*4)
  else :
    ground_ship=20+(weight*4.75) 
print (premium_ground_shipping)
#drone shipping
def drone_shipping(weight ) :
  if weight <=2:
    drone_ship=(weight*4.5)
  elif weight >=2 and weight <=6:
    drone_ship=(weight*9)
  elif weight >=6 and weight <=10:
    drone_ship=(weight*12)
  else :
    drone_ship=(weight*14.5)
  return drone_ship 
print (drone_shipping(1.5))
#pre calculation 
ground_ship= ground_shipping(weight)
drone_ship= drone_shipping(weight)

def cheapest_method(drone_ship,ground_ship,premium_ground_shipping):
  if drone_ship>ground_ship and drone_ship>premium_ground_shipping:
    return drone_ship
  elif ground_ship>premium_ground_shipping and ground_ship>drone_ship:
    return ground_ship
  else :
    return premium_ground_ship

print (cheapest_method(drone_ship,ground_ship,premium_ground_shipping))
