import jieba

if __name__ == '__main__':
    word_string_list = open('huawei.txt', mode='r', encoding='utf8').readlines()
    new_word_string_list = list()
    for w in word_string_list:
        if w == '\n':
            continue
        w = w.replace('\n', '')
        new_word_string_list.append(w)
    print(len(word_string_list))
    print(len(new_word_string_list))
    print(new_word_string_list)
    word_string = ''.join(new_word_string_list)
    print(word_string)
    cut_result = jieba.cut_for_search(word_string)
    word_count = dict()
    for r in cut_result:
        if r in word_count:
            word_count[r] += 1
        else:
            word_count[r] = 1
    print(sorted(word_count.items(), key=lambda d:d[1], reverse=True))
