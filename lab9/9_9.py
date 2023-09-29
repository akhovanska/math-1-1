def max_dictionary(d):
    maxi = max(d.values())
    res = 10 ** 4
    for i in d:
        if d[i] == maxi and i < res:
            res = i
    return res

test_amount = int(input())

for test_number in range(test_amount):
    v = int(input())
    vote_dictionary = {}
    for i in range(v):
        vote = int(input())
        if vote in vote_dictionary:
            vote_dictionary[vote] += 1
        else:
            vote_dictionary[vote] = 1
    print(max_dictionary(vote_dictionary))
