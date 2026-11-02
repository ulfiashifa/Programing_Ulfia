pizza = ["pepperoni", "keju", "jamur"] 

pizza_teman = pizza[:] 
pizza.append("margherita") 
pizza_teman.append("meat lovers") 

print("Pizza favorit saya adalah:") 
for jenis_pizza in pizza: 
    print(jenis_pizza) 
    
print("\nPizza favorit teman saya adalah:") 
for jenis_pizza in pizza_teman: 
    print(jenis_pizza) 