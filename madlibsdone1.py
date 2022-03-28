
noun = input("Choose a noun: ")
verb = input("Choose a verb ending in ing: ")
adj = input("Choose an adjective: ")
pluralnoun = input("Choose a plural noun: ")
bodypart = input("Choose a bodypart: ")
num = input("Choose a number: ")
place = input("Choose a place: ")
verbq = input("Choose another verb ending in ing : ")






madlib1 = "On my way home from magic school, I dropped my {noun1} as I was {verb1}. So, I went home and cried because it was damaged. My mom found out and bought me {adj1} {pluralnoun1}\
    so I thanked her for the thought. Suddenly, my {bodypart1} started acheing. I realized that I was cursed and had {num1} days left to live. The only way to survive was to go to {place1}\
    and find the cure by {verb2} the grand mage. I am going to leave in a few days. Now, I am in my training arc. ".format(noun1 = noun, verb1 = verb, adj1 = adj, pluralnoun1 = pluralnoun, bodypart1=bodypart, num1= num, place1=place, verb2 = verbq)


madlib2 = "I like {pluralnoun1}. It makes me feel {adj1}. But, these days, I started using my {noun1} because it is more interesting to me. My life is pretty spectacular. I hurt my\
    {bodypart1} {num1} many times when I was younger, so I {verb1} to get around. When I am old, I plan to retire in {place1}, then my enemies will see me {verb2} to my grave.".format(noun1 = noun, verb1 = verb, adj1 = adj, pluralnoun1 = pluralnoun, bodypart1=bodypart, num1= num, place1=place, verb2 = verbq)

madlib3 = "Today is my birthday. I turned {num1} years old rtoday! My parents gifted me tickets to {place1} today. My sister gifted me a {adj1} {bodypart1} for fun. She said she picked it\
    from a grave. My friend gifted me {pluralnoun1} because they said I needed it. Out of nowhere, the fire alarm started {verb1}, so I had to end my party early. As I was {verb2} out,\
        I hit a wall and thought maybe the universe hated me.".format(noun1 = noun, verb1 = verb, adj1 = adj, pluralnoun1 = pluralnoun, bodypart1=bodypart, num1= num, place1=place, verb2 = verbq)





choice = int(input("Choose a story 1 to 3: "))
if choice == 1:
    print(madlib1)
elif choice == 2:
    print(madlib2)
elif choice == 3:
        print(madlib3)
else:
    print("Invalid. Choose again. ")