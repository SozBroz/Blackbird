#for a in locations:
#    print("city: " + a['city'])
#    print("country: " + a['country'])
#    print("sim: " + a['sim'])
#    print("dest_port:",a['dest_port'])

print('hi')
for i,a in enumerate(locations):
    if "\n" in a['dest_port']:
        print(i)

print('hi2')