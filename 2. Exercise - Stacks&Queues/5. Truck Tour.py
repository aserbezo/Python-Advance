from collections import  deque

def add_user_input(n):
    petrol = deque()
    for i in range(n):
        command=input().split(' ')
        petrol.append(command)
    return petrol


number_petrol_pumps =int(input())

left_fuel=0
start=[]
counter=0
petrol = add_user_input(number_petrol_pumps)


while  petrol and len(start)<len(petrol):
    pump_to_check=petrol[0]
    fuel=int(petrol[0][0])
    distance=int(petrol[0][1])
    fuel+=left_fuel
    if fuel<distance:
        petrol.popleft()
        petrol.append(pump_to_check)
        start=[]
    else:
        left_fuel=fuel-distance
        start.append(counter)
        petrol.popleft()
    counter+=1

print(start[0])
