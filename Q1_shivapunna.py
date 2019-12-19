coins = [9,6,5,1]
#coins = [25,10,5]
v = 11
#v = 30



def getMinCoins(coins, v):
    v_memory = dict()
    v_memory[0] = 0
    for i in range(1, v+1):
            cur_min = None
            for c in coins:
                if i < c:
                    continue
                else:
                    if v_memory[i-c] == 0 or v_memory[i-c]:
                        value = 1+v_memory[i-c]
                    else:
                        continue

                    if not cur_min:
                        cur_min = value
                    elif value < cur_min:
                        cur_min = value

            v_memory[i] = cur_min

    print(v_memory[v] if v_memory[v] else "Change with coins not possible")


getMinCoins(coins, v)

