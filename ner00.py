def trans(JE,txt):
     import os, requests, uuid, json
     
#    subscription_key = '468d18563f224cb1b22486b011139bad'
     subscription_key = '8e12dce789bb43afbc74109f35de9d61'
     endpoint         = 'https://api.cognitive.microsofttranslator.com'
     
     if JE=='EJ':
         fromLang = 'en'
         toLang = 'ja'
     else:
         fromLang = 'ja'
         toLang = 'en'
#    txt = 'if America is to be a great nation, this must become true.'
     
     path = '/translate?api-version=3.0'
     params = '&from=' + fromLang + '&to=' + toLang
     constructed_url = endpoint + path + params
     
     headers = {
         'Ocp-Apim-Subscription-Key': subscription_key,
         'Ocp-Apim-Subscription-Region': 'japaneast',
         'Content-type': 'application/json',
         'X-ClientTraceId': str(uuid.uuid4())
     }
     
     body = [{'text' : txt}]
     request = requests.post(constructed_url, headers=headers, json=body)
     response = request.json()
#    print(response)
#    print('翻訳：⇒  ' + response[0]['translations'][0]['text'])
     a= response[0]['translations'][0]['text']
#    print('In sub 翻訳',a)
#    exit(0)
     return a
     
     





def Ner():
#   for iNews in range(Nnews):
    return



# 文章の類似度
#pip install sentence-transformers
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import nltk
def Remove(dataA0,data00,Nnews):
#   data00=np.full((Nnews,4),'',dtype=object)

    for iNews in range(Nnews):
        for i in range(4):
            data00[iNews,i]=dataA0[0,iNews,0,i]

        s2=data00[iNews,3].split()
        if s2[1]=='Comments':
#            print('\nif Comments')
             s3=s2[3:]
#            print('\ns3=',s3)

        elif s2[1]=='comments':
#            print('\nif comments')
             s3=s2[3:]
#            print('\ns3=',s3)
        else:
#            print('\nNot if comments')
             s3=s2[:]
#       print('\ns3=',s3)
        s4=' '.join(s3)
        s5=s4.replace('&#39;','') 
        dataA0[0,iNews,0,3]=s5
#       print('\ns5=',s5)
#       exit(0)



#       print(s3)
#       s4=' '.join(s3)
#       s5=nltk.sent_tokenize(s4)
#       print(s5)
    return dataA0
    




def sim(sentences):
    '''
    sentences00 = [
    "Three years later, the coffin was still full of Jello.",
    "The fish dreamed of escaping the fishbowl and into the toilet where he saw his friend go.",
    "The person box was packed with jelly many dozens of months later.",
    "He found a leprechaun in his walnut shell."]
    '''

    model = SentenceTransformer('bert-base-nli-mean-tokens')
    
    sentence_embeddings = model.encode(sentences)
    c=sentence_embeddings
    print(sentence_embeddings.shape)
    
    a01=cosine_similarity(  [sentence_embeddings[0]], [sentence_embeddings[1]] )
    #a=cosine_similarity(  [sentence_embeddings[0]], sentence_embeddings[1:] )
    print('In Module=',a01)
    
    
    a=cosine_similarity(
        [sentence_embeddings[0]],
        sentence_embeddings[1:]
    )
    return a01
    


#https://www.isc.meiji.ac.jp/~mizutani/python/intro3_python.html

#aa=['Usami','Yoshiyuki','B', '##iden', 'Poland', 'Russia', 'Ukraine','Ba','##rak','##Obama']

def ner11(aa):
    cc=[]
    counter=0
    nn=len(aa)
    for i in range(nn):
        bb=aa[i].find('##')
        dd=aa[i]
        if bb==0:
            cc.append('')
            counter=counter+1
            cc[i-counter]=(cc[i-counter]+aa[i][2:])
        else:
            cc.append(aa[i]) 
            counter=0
    
#   print(aa)
    ee = [i for i in cc if i not in  '']
#   print(ee)
    return ee

#ee=ner00(aa)
#print('hello',ee)
'''
cc=[]
counter=0
nn=len(aa)
for i in range(nn):
    bb=aa[i].find('##')
    dd=aa[i]
    if bb==0:
        cc.append('')
        counter=counter+1
        cc[i-counter]=(cc[i-counter]+aa[i][2:])
    else:
        cc.append(aa[i]) 
        counter=0

print(aa)
ee = [i for i in cc if i not in  '']
print(ee)
'''




