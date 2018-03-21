import os
import nltk
import tokenize
from nltk import ne_chunk
from nltk.parse import stanford
from nltk.parse.stanford import StanfordDependencyParser
from graphviz import Source
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize.moses import MosesDetokenizer 	
from dandelion import DataTXT

datatxt = DataTXT(app_id='78697915c52f48f5b3bd6c7bb603b2a2', app_key='78697915c52f48f5b3bd6c7bb603b2a2')
h,k = 100,100
#num = 0
l = 9
i = 0
j = 0   
main = []
trial = []
tagged = [[0 for x in range(h)] for y in range(k)]
named = [[0 for x in range(h)] for y in range(k)]
list1 = [[0 for x in range(h)] for y in range(k)]
detoken = [[0 for x in range(h)] for y in range(k)]
ini_path = 'C:\Stanford'
os.environ['STANFORD_PARSER'] = 'C:\Stanford\stanford-parser.jar'
os.environ['STANFORD_MODELS'] = 'C:\Stanford\stanford-parser-3.5.2-models.jar'   
os.environ['JAVAHOME'] = 'C:/Program Files/Java/jdk1.8.0_161/'
parser = stanford.StanfordParser('C:\Stanford\stanford-parser.jar','C:\Stanford\stanford-parser-3.5.2-models.jar')

def construct(hello):
    num = 0
    sdp = StanfordDependencyParser()
    result = list(sdp.raw_parse(hello))
    dep_tree_dot_repr = [parse for parse in result][0].to_dot()
    num = num + 1    
    source = Source(dep_tree_dot_repr, filename="dep_tree"+ str(main.index(hello)), format="png")
    source.view()

def extract(sent,ind):
    j = 0
    trial.append(sent)
    length = len(ind)
    summary = []
    #summary.append(detoken[0][0])
    for j in range(length):
        summary.append(sent[ind[j]])
        detokenizer = MosesDetokenizer()
        hello = detokenizer.detokenize(summary, return_str=True)
        #print(hello)
    main.append(hello)
    construct(hello)

def checksim(arr,sent):
    j = 0
    c = []
    length = len(arr)
    for j in range(length):
        if 0.6 < arr[j] < 0.99:
            #print(arr[j])
            c.append(arr.index(arr[j])) 
    if len(c) != 0:
         extract(sent,c)
    else:
        exit

def similarity(arr):
    b = []
    j = 0
    length = len(arr)
    #print(length)
    for j in range(length - 1):
        A = datatxt.sim(arr[j],arr[j+1])
        b.append(A.similarity)
    #print(b)
        print(A.similarity)
    checksim(b,arr)

def initialize(file):
    m = 0
    n = 0
    o = 0
    fo = open(file).read()
    #print(fo)
    #stopWords = set(stopwords.words('english'))
    sent_token = sent_tokenize(fo)
    filtered_sentences = []
    for s in sent_token:
     word_token = word_tokenize(s)
     for w in word_token:
      #if w not in stopWords:
       filtered_sentences.append(w)
       
     list1[m][0] = filtered_sentences
     m=m+1
     tagged[n][0] = nltk.tag.pos_tag(filtered_sentences)
     named[n][0] = ne_chunk(tagged[j][0])
     n = n+1
     filtered_sentences = []
    for count in range(m):
     print(tagged[count][0])
    #for count in range(m):
    # print(named[count][0])
    detokenizer = MosesDetokenizer()
    for a in range(m):
     detoken[o][0] = detokenizer.detokenize(list1[a][0], return_str=True)
     o = o+1
    for b in range(o):
     print(detoken[b][0]) 
    i = 0
    a = []
    for i in range(o):
        a.append(detoken[i][0])
    similarity(a)    

print("File One: ")
initialize("1.txt")
print("\nFile two: ")
initialize("2.txt")
print("\nFile three: ")
initialize("3.txt")
detokenizer = MosesDetokenizer()
hello = detokenizer.detokenize(main, return_str=True)
#print(hello)
f = open('summary.txt','w')
f.write(hello)
f = open('summary.txt','r')
rishi = f.read()
initialize('summary.txt')
#print(main[2])
#len = len(main)
len = len(main)
f = open('multidocsummary.txt','w')
f.write(main[len - 1])