import random 
###Set up
c = int(input("Enter the initial amount of money: "))
p = float(input("Enter the probability of winning (between 0 and 1): "))
q = 1 - p
N = int(input("Enter the goal amount of money: "))
real_count = 0
countW = 0
result = []
###fonction of simulation    
def simulate_game(c, p, N):
    count = 0
    while c > 0 and c < N:
        if random.uniform(0, 1) < p:
            c += 1
            count += 1
        else:
            c -= 1
            count += 1
    if c == N:
        return True, count
    else:
        return False, count

###simulate 1000 times and store result and count number of win
for i in range(1000):
    result[i] = simulate_game(c, p, N)
    if result[i][0] == True:
            countW += 1
    real_count = real_count + result[i][1]
average_count = real_count/len(result)
print(f"The number of win in 1000 session is {countW} and on average in 1 session the player play {average_count} ")



