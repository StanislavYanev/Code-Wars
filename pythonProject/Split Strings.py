def solution(s):
    string_list = list(s)
    if len(string_list) % 2 != 0:
        string_list.append("_")
    text_list = []
    for i in range(1,len(string_list)+1,2):
        word = f"{string_list[i-1]}{string_list[i]}"
        text_list.append(word)
    return text_list

print(solution('abcdef'))



# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']