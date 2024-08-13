def numTeams(self, rating) -> int:
    output = 0
    for i in range(len(rating)):
        for j in range(i + 1, len(rating)):
            for k in range(j + 1, len(rating)):
                if (rating[i] < rating[j] < rating[k]) or rating[i] > rating[j] > rating[k]:
                    output += 1
    return output


#Better way to get solve it
def numTeams1(self, rating) -> int:
    output = 0
    for i in range(len(rating)):
        lessleft = 0
        lessright = 0
        moreleft = 0
        moreright = 0
        for j in range(0, i):
            if rating[j] < rating[i]:
                lessleft += 1
            if rating[j] > rating[i]:
                moreleft += 1
        for j in range(i + 1, len(rating)):
            if rating[j] > rating[i]:
                moreright += 1
            if rating[j] < rating[i]:
                lessright += 1
        output += lessleft * moreright
        output += lessright * moreleft
    return output
