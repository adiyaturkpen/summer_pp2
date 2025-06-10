def solve(numheads, numlegs):
    R=(numlegs-2*numheads)//2 
    C = 35 - R 
    print("Chickens:",C,"Rabbits:",R)
solve(35, 94)

'''c+r=35
   2c+4r=94
   2(35-r)+4r=94
   2r=24
   r=12'''
