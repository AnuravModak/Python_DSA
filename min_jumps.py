import statistics
def minJumps(seats):
    position = []
    count = 0
    MOD = 10 ** 9 + 7
    lenn=len(seats)
    for i in range(lenn):

        # If current place is occupied
        if (seats[i] == 'x'):
            # Push the current position
            # in the vector
            position.append(i - count)
            count += 1
    print(position)


    ans = 0
    # The index of the median element
    med_index = (count - 1) // 2

    # The value of the median element
    med_val = position[med_index]
    print(med_val,med_index)

    # Traverse the position[]
    for i in range(len(position)):
        # Update the ans
        ans = (ans % MOD +
               abs(position[i] - med_val)
               % MOD) % MOD

    # Return the final count
    return ans % MOD


print(minJumps("....x..xx...x.."))
