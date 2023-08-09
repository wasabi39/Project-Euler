using Combinatorics

combinations = permutations([0,1,2,3,4,5,6,7,8,9], 10)
i = 0

for item in combinations
    global i
    if i == 999999
        print(item)
    end
    i += 1
end