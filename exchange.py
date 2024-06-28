container1="Milk"
container2="Water"

 ##You can change from here
#container3=container2 
#container2=container1
#container1=container3
##But in python do it easier like:
container1, container2 = container2, container1
##You can change till here
print(f"Container1 contains {container1}")
print(f"Container2 contains {container2}")