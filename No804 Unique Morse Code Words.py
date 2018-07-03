def uniqueMorseRepresentations(words):
    morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    character_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    morse_dict = {}
    for (i, j) in zip(character_list, morse_list):
        morse_dict[i] = j
    print(morse_dict)
    results = []
    for i in words:
        result = []
        for j in i:
            result.append(morse_dict[j])
        result_str = ''.join(result)
        results.append(result_str)
    #
    # new_results = []
    # print(results)
    # for i, j in enumerate(results):
    #     if j in results[i+1:]:
    #         pass
    #     else:
    #         new_results.append(j)


    return len(set(results))
words = ["gin", "zen", "gig", "msg"]
print(uniqueMorseRepresentations(words))