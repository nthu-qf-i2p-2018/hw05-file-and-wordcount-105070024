
# coding: utf-8

# In[12]:


import string
import csv
import json

def main(filename):
    
    txtfile = open(filename)
    lines = txtfile.readlines()

    all_words = []
    list1 = []
    
    for line in lines:
        words = line.split()
    
    
        for word in words:
            translator = str.maketrans(' ',' ',string.punctuation)
            k = word.translate(translator)
            all_words.append(k)
    df = set(all_words)
    df.remove('') 
    for w in df:
        counter = all_words.count(w)
        list1.append(w)
        list1.append(counter)
    
    with open("wordcount.csv","w+",newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['word', 'count'])
        for k in range(0,len(list1),2):
            w=list1[k]
            counter=list1[k+1]
            writer.writerow([w,counter])
        csv_file.close()

    dictionary=dict()
    for t in range(0,len(list1),2):
        dictionary[list1[t]]=list1[t+1]
    with open("wordcount.json","w+",newline='') as json_file:
        json.dump(dictionary,json_file)
        json_file.close()
        
if __name__ == '__main__':
    main("i_have_a_dream.txt")

