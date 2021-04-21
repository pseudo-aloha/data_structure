My_dict = {}
page = []
point_to = dict()
outbranching = dict()
PR = dict()
PR_prime = dict()
content = []
DIFF = 0.001
d = 0.25
N = 500
for i in range(N):
    f = open('page'+str(i),'r')
    lines = f.read().split('\n')
    if (len(lines)>2):
        page.append(lines[:-3])
    else:
        page.append([])
    if (len(lines)>1):
        content.append(lines[-2])
    else:
        content.append('')
page.append([])
content.append('')
diff = DIFF+1
for i in range(N+1):
    outbranching['page'+str(i)] = len(page[i])
for i in range(N+1):
    for pages in page[i]:
        if not(pages in point_to):
            point_to[pages] = ['page'+str(i)]
        else:
            point_to[pages].append('page'+str(i))
for i in range(N+1):
    PR['page'+str(i)] = 1/(N+1)
    PR_prime['page'+str(i)] = 0
while(diff>=DIFF):
    diff = 0
    for i in range(N+1):
        PR_prime['page'+str(i)] = (1-d)/(N+1)
        for P in point_to['page'+str(i)]:
            PR_prime['page'+str(i)] += d*PR[P]/outbranching[P]
        diff += abs(PR_prime['page'+str(i)] - PR['page'+str(i)])
    PR = PR_prime.copy()
#sort page rank
pageRank = []
for i in range(N+1):
    insert_point = len(pageRank)
    pageRank.append(i)
    while PR['page'+str(i)] > PR['page'+str(pageRank[insert_point-1])]:
        insert_point -= 1
        temp = pageRank[insert_point]
        pageRank[insert_point] = i
        pageRank[insert_point+1] = temp
        if insert_point == 0:
            break
#write file for page rank
'''f = open('pr_85_001.txt','w')
for  p in pageRank:
    f.write('page'+str(p)+'\t'+str(outbranching['page'+str(p)])+'\t'+str(PR['page'+str(p)])[:10]+'\n')
f.close()'''
for i in range(N+1):
    sentence = content[i].split(' ')
    for word in sentence:
        if word != '':
            if not(word in My_dict):
                My_dict[word] = [i]
            elif not(i in My_dict[word]):
                My_dict[word].append(i)
'''f = open('reverseindex.txt','w')
sorted_alphabet = sorted(My_dict.keys())
for  word in sorted_alphabet:
    f.write(word+'\t')
    for p in My_dict[word]:
        f.write('page'+str(p)+' ')
    f.write('\n')
f.close()'''
def search_word(dictionary,word):
    if not(word in dictionary):
        return 'none'
    output_page = []
    for i in dictionary[word]:
        if len(output_page) == 0:
            output_page.append(i)
        elif len(output_page)<10:
            insert_point = len(output_page)
            output_page.append(i)
            if len(output_page) == 2:
                if PR['page'+str(i)] > PR['page'+str(output_page[0])]:
                    temp = output_page[0]
                    output_page[0] = i
                    output_page[1] = temp
            while (PR['page'+str(i)] > PR['page'+str(output_page[insert_point-1])]):
                insert_point -= 1
                temp = output_page[insert_point]
                output_page[insert_point] = i
                output_page[insert_point+1] = temp
                if insert_point == 0:
                    break
        elif len(output_page)>=10:
            insert_point = 10
            output_page.append(i)
            while PR['page'+str(i)] > PR['page'+str(output_page[insert_point-1])]:
                insert_point -= 1
                temp = output_page[insert_point]
                output_page[insert_point] = i
                output_page[insert_point+1] = temp
                if insert_point == 0:
                    break
            output_page = output_page[:10]
    new_output_page = []
    for i in output_page:
        new_output_page.append(str(i))
    str_output_page = ' '.join(new_output_page)
    return str_output_page

def search_words_and(dictionary,words):
    for word in words:
        if not(word in dictionary):
            return 'none'
    if len(words) == 1:
        return search_word(dictionary,words[0])
    else:
        candidate_page = dictionary[words[0]].copy()
        delete_list = []
        for i in range(1,len(words)):
            for p in candidate_page:
                if not(p in dictionary[words[i]]) and not(p in delete_list):
                    delete_list.append(p)
        for i in delete_list:
            candidate_page.remove(i)
        if len(candidate_page) == 0:
            return 'none'
        output_page = []
        for i in candidate_page:
            if len(output_page) == 0:
                output_page.append(i)
            elif len(output_page)<10:
                insert_point = len(output_page)
                output_page.append(i)
                if len(output_page) == 2:
                    if PR['page'+str(i)] > PR['page'+str(output_page[0])]:
                        temp = output_page[0]
                        output_page[0] = i
                        output_page[1] = temp
                while (PR['page'+str(i)] > PR['page'+str(output_page[insert_point-1])]):
                    insert_point -= 1
                    temp = output_page[insert_point]
                    output_page[insert_point] = i
                    output_page[insert_point+1] = temp
                    if insert_point == 0:
                        break
            elif len(output_page)>=10:
                insert_point = 10
                output_page.append(i)
                while PR['page'+str(i)] > PR['page'+str(output_page[insert_point-1])]:
                    insert_point -= 1
                    temp = output_page[insert_point]
                    output_page[insert_point] = i
                    output_page[insert_point+1] = temp
                    if insert_point == 0:
                        break
                output_page = output_page[:10]
    new_output_page = []
    for i in output_page:
        new_output_page.append(str(i))
    str_output_page = ' '.join(new_output_page)
    return str_output_page
def search_words_or(dictionary,words):
    if len(words) == 1:
        return search_word(dictionary,words[0])
    else:
        candidate_page = []
        for word in words:
            if word in dictionary:
                for i in dictionary[word]:
                    if not(i in candidate_page):
                        candidate_page.append(i)
        if len(candidate_page) == 0:
            return 'none'
        output_page = []
        for i in candidate_page:
            if len(output_page) == 0:
                output_page.append(i)
            elif len(output_page)<10:
                insert_point = len(output_page)
                output_page.append(i)
                if len(output_page) == 2:
                    if PR['page'+str(i)] > PR['page'+str(output_page[0])]:
                        temp = output_page[0]
                        output_page[0] = i
                        output_page[1] = temp
                while (PR['page'+str(i)] > PR['page'+str(output_page[insert_point-1])]):
                    insert_point -= 1
                    temp = output_page[insert_point]
                    output_page[insert_point] = i
                    output_page[insert_point+1] = temp
                    if insert_point == 0:
                        break
            elif len(output_page)>=10:
                insert_point = 10
                output_page.append(i)
                while PR['page'+str(i)] > PR['page'+str(output_page[insert_point-1])]:
                    insert_point -= 1
                    temp = output_page[insert_point]
                    output_page[insert_point] = i
                    output_page[insert_point+1] = temp
                    if insert_point == 0:
                        break
                output_page = output_page[:10]
    new_output_page = []
    for i in output_page:
        new_output_page.append(str(i))
    str_output_page = ' '.join(new_output_page)
    return str_output_page
f = open('list.txt','r')
f1 = open('result_25_001.txt','w')
lines = f.read().split('\n')
for words in lines:
    word_list = words.split(' ')
    if len(word_list) == 1:
        f1.write(search_word(My_dict,word_list[0])+'\n')
    else:
        if search_words_and(My_dict,word_list) == 'none':
            f1.write('AND none\n')
        else:
            answer = search_words_and(My_dict,word_list).split()
            f1.write('AND ')
            for ans in answer:
                f1.write('page'+str(ans))
            f1.write('\n')
        if search_words_or(My_dict,word_list) == 'none':
            f1.write('OR none\n')
        else:
            answer = search_words_or(My_dict,word_list).split()
            f1.write('OR ')
            for ans in answer:
                f1.write('page'+str(ans))
            f1.write('\n')
        
f.close()
f1.close()
