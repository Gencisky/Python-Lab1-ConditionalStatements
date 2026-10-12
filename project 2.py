by = int(input("Enter your birth year: "))

c = by % 12

d={0:"Monkey",1:"Rooster",2:"Dog",3:"Pig",4:"Rat",5:"Ox",6:"Tiger",7:"Rabbit",8:"Dragon",9:"Snake",10:"Horse",11:"Sheep"}
zs = d[c]

print("Your chinese zodiac sign is: ", zs)