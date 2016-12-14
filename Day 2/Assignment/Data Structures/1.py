state = {
    'maharashtara': ['mumbai', 'pune', 'nasik'],
    'karnataka': ['bangalore', 'mysore'],
    'tamilnad': ['chennai', 'madurai']
}

statenumber ={}

print(state)

state['maharashtara'].append('nagpur')

print("After adding: ", state)

for i in state.keys():
    statenumber[i] = len(state[i])

print("Number: ", statenumber)

state['tamilnad'].remove('madurai')

print("After removing", state)


