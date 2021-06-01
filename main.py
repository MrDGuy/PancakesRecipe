#define the ingredients
cupsOfFlour = 2.5
cupsOfMilk = 1
numEggs = 2
tblsButter = 3
tspSugar = 4

#Begin preparation
print("Melting Butter")
meltedButter = tblsButter
print("Mixing Dry ingredients")
cupsOfFlour = 0
tspSugar = 0
for i in range(numEggs):
    print("Crack Egg")
    print("Pour egg")
    print("Throw out shell")
    numEggs = numEggs - 1
    print(str(numEggs) + " eggs left")
print("Mixing rest of ingredients")
cupsOfMilk = 0

#Make Pancakes
pancakeMixture = 4.0
finishedPancakes = 0
while True:
    print("Pour 1/4 cup on skillet")
    pancakeMixture = pancakeMixture - 0.25
    print("Flip")
    print("Serve Pancake")
    finishedPancakes = finishedPancakes + 1
    if pancakeMixture == 0:
        break

print(str(finishedPancakes) + " pancakes served")
