def solution(n, words):
    result = [words[0][0]]
    for i,word in enumerate(words):
        
        if word not in result and result[-1][-1] == word[0]:
            result.append(word)

        else:
            return [i%n + 1,(i//n) + 1]
    return [0,0]