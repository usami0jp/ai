from multiprocessing import Process, Value
import socket,time
HOST='127.0.0.1'
PORT=50014   #######  HOST ===   13  13   13
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

def yahoo_read(run,run2,run3,run4):
    #https://flytech.work/blog/8818/
    #https://qiita.com/t0d4_/items/f9caa8621ca0c1fa3f98
    from transformers import AutoTokenizer, AutoModelForTokenClassification
    from transformers import pipeline
    import ner00, subprocess, nltk
    #nltk.download() #<- for punkt install ,  Executer nltk.d in python program , not unix shell
    import numpy as np
    #tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
    #model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
    #nlp = pipeline("ner", model=model, tokenizer=tokenizer)
    from diffusers import StableDiffusionPipeline
    import requests,re, wikipedia,warnings, torch, cv2
    from bs4 import BeautifulSoup
    #from google.cloud import translate_v2 as translate
    from transformers import pipeline, set_seed
    from PIL import Image, ImageDraw, ImageFont
    from newspaper import Article
    import re,random
    warnings.simplefilter('ignore')
    #generator = pipeline('text-generation', model='gpt2')
    set_seed(42)
    
    LLNo=1   #  Iteration of whole process  
    Nnews=3  #  No. of News  max 8
    iGenN=30 #   Text generation  100
    iRemove=25   #Remove leading words 10
    
    f2=open('yahoo/out2','a')
    a='LLNO= , '+str(LLNo)+' , '
    b='Nnews= , '+str(Nnews)+' , '
    c='iGen= , '+str(iGenN)+' , '
    d='iRemoves , '+str(iRemove)+'\n'
    all=a+b+c+d
    f2.write(all)
    f2.close
    
    # 0 Jap title  1 Eng title 2 summary 3 Named Entity 4 Text generation
    # dataA0  4 dimenstion
    dataA0=np.full((1,Nnews,iGenN+1,4),'',dtype=object)  #str -> one character
    data00=np.full((Nnews,4),'',dtype=object)    #str -> one character
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Sntence Similarity
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    from sentence_transformers import SentenceTransformer
    from sklearn.metrics.pairwise import cosine_similarity
    
    sentences = [
        "Three years later, the coffin was still full of Jello.",
        "The fish dreamed of escaping the fishbowl and into the toilet where he saw his friend go.",
        "The person box was packed with jelly many dozens of months later.",
        "He found a leprechaun in his walnut shell."
    ]
    
    s=' '
    print('\nScraping from Japanese Yahoo.  Yahoo.co.jp\n')
    URL = "https://www.yahoo.co.jp/"
    rest = requests.get(URL)
    soup = BeautifulSoup(rest.text, "html.parser")
    data_list = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
    info=[]
    dataN=[]
    #dataA00=[]  #  0日本語みだし 1英語みだし  2 日本語全文　３　英語全文
    
    #translate_client=translate.Client()
    
    f=open('yahoo/out.txt','a')
    print('==============================') 
#   print('  Yahoo News のみだしを',Nnews,'個取り出す ')
    print(' No. of News=', Nnews, ' from Yahoo News ')
    print('==============================') 
    
    
    for kk in range(Nnews):
        data=data_list[kk]
        g=data.span.string   #みだし
        g00=data.span.string #みだし
        print('g=',g)
    
        a00=ner00.trans('JE',g) #みだしの英語
        a=ner00.trans('JE',g)
    
        dat=data.attrs["href"]
        info.append(dat)
    
        url=info[kk]
        article = Article(url)
        article.download()
        article.parse()
    
        g=article.text
        example=ner00.trans('JE',g)
    
    
        dataA0[0,kk,0,0]=g00   #  みだし日本語
        dataA0[0,kk,0,1]=a00   #みだし英語
        dataA0[0,kk,0,2]=article.text  # 内容日本語               
        dataA0[0,kk,0,3]=example              #内容英語 
    
        kL0=str(dataA0[0,kk,0,3])         #何故かここだけ\n\nが入っているのでそれを排除
        kL1=kL0.split()
        kL2=' '.join(kL1)
        dataA0[0,kk,0,3]=kL2
    
        kL0=str(dataA0[0,kk,0,2])         #何故かここだけ\n\nが入っているのでそれを排除
        kL1=kL0.split()
        kL2=' '.join(kL1)
        dataA0[0,kk,0,2]=kL2
    
        print('i=0 ',dataA0[0,kk,0,0])
        print('i=1 ',dataA0[0,kk,0,1])
        print('i=2 ',dataA0[0,kk,0,2])
        print('i=3 ',dataA0[0,kk,0,3])
        print(' ')
    
    f2=open('yahoo/out2','a')
    for kk in range(Nnews):
        '''
        a=dataA0[0,kk,0,0]+' , '
        b=dataA0[0,kk,0,1]+' , '
        c=dataA0[0,kk,0,2]+' , '
        d=dataA0[0,kk,0,3]+'\n'
        '''
    
        a=dataA0[0,kk,0,0]+'\n'
        b=dataA0[0,kk,0,1]+'\n'
        c=dataA0[0,kk,0,2]+'\n'
        d=dataA0[0,kk,0,3]+'\n'
        all=a+b+c+d
        f2.write(all)
    f2.close

    f2=open('yahoo/out2_news','w')
#   for kk in range(Nnews):
    for kk in range(1):
#       a=dataA0[0,kk,0,0]+'\n'
        a=dataA0[0,kk,0,0]+'。'
#       c=dataA0[0,kk,0,2]+'\n'
        all=a
        f2.write(all)
    f2.close

    # making -> dataA00,dataA dataAA dataJa data En
    # dataA00=[kk,i,' ']  #  i=0 Jap title 1 Eng title   2  Japanese whole sentence　３　 Eng. whole 
    
    dataA0=ner00.Remove(dataA0,data00,Nnews)
    
    #print('\n dataA0= \n',dataA0[0,kk,0,3],'\n')
    
    subprocess.run(["cat out.txt"],shell=True)
    
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    
    tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
    model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
    nlp = pipeline("ner", model=model, tokenizer=tokenizer)
    warnings.simplefilter('ignore')
    generator = pipeline('text-generation', model='gpt2')
    set_seed(42)
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    
    ijk=0
    #================================
    for LL in range(LLNo): # Repeating whole process, Default is just 1.
    #    print('==============================') 
    #    print(' Loop Start whole process LL= ',LL)
    #    print('==============================') 
     
         #rint('==============================') 
         #rint('　Loop of No. of News
         #rint('==============================') 
         for iNews in range(Nnews):  
    
             #-------------------------------
             #    for   Text Generation
             #-------------------------------
             for iGen in range(iGenN):
                 print(' Text Generation  ',run4.value)
                 print(' Text Generation  ',run4.value)
                 ts2=int(time.time()-run2.value)
                 ts3=int(time.time()-run3.value)
                 print('run =',run.value,' run 2=',run2.value,ts2,'  run 3=',run3.value,ts3,'  run 4=',run4.value)

                 if run4.value == 0:
                     print('In Text Generation ',run4.value)
                     print('In Text Generation ',run4.value)
        
                     print(' Text Gen. -> Summary -> text gen. iGen=',iGen )
                 
                 #================================
                     print('LL iNews iGen =',LL,iNews,iGen)
                     print('\nA0[iNews,iGen,3]',dataA0[LL,iNews,iGen,3],'\n')         # ner  
                     ner=nlp(dataA0[LL,iNews,iGen,3])         # ner  
                 #================================
                     ner2=[]
                     for i in range(len(ner)):
                        ner2.append(ner[i]['word'])
                     ner3=ner00.ner11(ner2)
                     ner4=', '.join(ner3)
        
        
                     nn=str(len(ner))
                     ner5a='LL= , '+str(LL+1)+' , iNews= ,'+str(iNews+1)+' , iGen= , '
                     ner5b=ner5a+str(iGen+1)+' , 固有名詞, '+nn+' ,'+ner4+'\n'
        
                     print('NER 固有名詞 = ',ner4)
                     f2=open('yahoo/out2','a')
                     f2.write(ner5b)
                     f2.close
        
        #            sumB=nltk.sent_tokenize(sum)
                     '''
        #            eeB=nltk.sent_tokenize(ee)
                     print('要約を分割 sumB=',sumB,'\n')
                     for j in range(len(sumB)):
                        print('sum[',j,']=',sumB[j],'')
                     sumC=sumB[1:]
                     print('')
                     for j in range(len(sumC)):
                        print('sum[',j,']=',sumC[j],'')
        
                     sumD=" ".join(sumC) 
                     print('sumD=',sumD)
                     '''
         
                     #========  Text Gen.  ======== 
                     c0=dataA0[LL,iNews,iGen,3]
                     c1=c0.split()
                     c2=' '.join(c1[iRemove:])
        
        
                     ner3t=c2
        
                     print('c2=',c2)
                     print('ner3=',ner3)
                     iGenT=divmod(int(iGen),3)
                     iGenT2=iGenT[1]
                     print('iGen=',iGen,'iGenT2=',iGenT2)
                     it='生成されたテキスト'
                     if iGen>1:
                         if len(ner3t)==0:
                             print('=======================================-- zero!!!!!!!==============')
                             ner3t=c2
                             print('=======================================-- zero!!!!!!!==============')
                             it=' Text len = 0'
                         else:
                             if iGenT2==0:
                                 if len(ner3) !=0:
                                     aa=random.randrange(len(ner3))
                                     ner3t=ner3[aa]
                                     print('\n aa=',aa, 'ner3t=',ner3t)
                                     it=' NER  is not 0'
                                 else:
                                     ner3t=c2
                                     it=' Text Gen. for NER=0'
        
        
                     print('\niGent=', iGenT,' it=',it)
        
                     print('\niGent=', iGenT)
                     print('ner3t=====',ner3t)
                     f4=open('out4','a')
                     b='Nnews= , '+str(Nnews)+' , '
                     c='iGen= , '+str(iGenN)+'\n' 
                     all2=b+c
                     f4.write(all2)
                     f4.write(str(ner3t))
                     f4.close
        
                     out=generator(ner3t, max_length=70,pad_token_id=50256, num_return_sequences=5)
                     #=============================== 
                     t0=dataA0[LL,iNews,iGen,3]
                     o1a=out[0]   # o1a is iGen+1 
                     #===============================
                     #   Sentence Similarity
                     #===============================
                     o1b=o1a['generated_text']
                     o1c=o1b.split()
                     o1e=" ".join(o1c)    # おー　わん　いー
                     sentence01=[t0,o1e]
        
                     print('\nsentence01=',sentence01)
        
                     a01=ner00.sim(sentence01)
                     print(a01)
                     a02=a01[0]
                     a03=a02[0]
                     print('===========================>',str(a03),'===============-str(a03')
        
                     dataA0[LL,iNews,iGen+1,3]=o1e       # <- Saving  iGen+1 
         
                        
                     f2=open('Coincidence ','a') 
                     o1f=o1e+'\n'+'sentence similarity= , '+str(a03) +'\n'
        
#                    print('===================================================================')
#                    print('\n'+'   Coincedence　= , '+str(a03) +'\n')
#                    print('===================================================================')
                     a09=str(LL)+str(iNews)+str(iGen)+str(a01)
                     f2.write(a09)
                     f2.close
        
                     f3=open('yahoo/out3','a') 
                     ner6a='LL= , '+str(LL+1)+' , iNews= ,'+str(iNews+1)+' , iGen= , '
                     ner6b=ner6a+str(iGen+1)+' , 固有名詞, '+nn+' ,'+ner4
                     ner6c=ner6b+' , '+o1f+'\n'
                     f3.write(ner6c)
                     f3.close
        
                     f5=open('yahoo/out5','a')
                     ac1= str(LL)+','+str(iNews)+','+str(iGen)
                     ac2=ac1+', '+str(ijk)
                     ac3=ac2+', 固有名詞, '+str(len(ner3))+' ,'+ner4+','+str(a03)+'\n'
                     f5.write(ac3)
                     f5.close
        
                     f2=open('一致','a') 
                     f2.write(ac3)
                     f2.close
        
                     f6=open('一致２','a') 
                     a10=str(iRemove)+', '+str(LL)+', '+str(iNews)+', '+str(iGen)+', '+str(a03)+'\n'
                     f6.write(a10)
                     f6.close
                     #----------------------------------------
        
                     sum00=summarizer(dataA0[LL,iNews,iGen,3], max_length=54, min_length=35, do_sample=False)
                     cc=sum00[0]
                     sum=cc['summary_text']
                     ee00=sum.split()  #単語に分割
        
                     image=pipe(sum).images[0]
                     fname= f'yahoo/images/{LL}-{iNews}-{iGen}.jpg'
                     image.save(fname) #usami
                     im=Image.open(fname)
        
                     ijk=ijk+1
                     fname2= f'yahoo/images2/{ijk}.jpg'
                     image.save(fname2)
                     font = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf', 32)
                     fontJ= ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc', 26)
                     img = Image.open(fname2)
                     draw = ImageDraw.Draw(img)
        #            draw.text((5,20), ner4, '#000000', font=font)  # NER at Upper 
        #            draw.text((5, 470), sum, '#FFFF00', font=font)
        #            draw.text((5, 430), dataA0[0,iNews,0,0], '#FFFFFF', font=fontJ)

                     '''
                     draw.text((5, 390), str(a03) , '#FFFFFF', font=fontJ)
                     draw.text((5, 430), sum, '#FFFFFF', font=font)
                     draw.text((5, 470), dataA0[0,iNews,0,1], '#FFFFF0', font=fontJ)
                     '''
        
                     draw.text((5, 0), sum, '#FFFF00', font=font)  # Summary at Upper 
                     draw.text((5, 430), str(a03) , '#FFFFFF', font=fontJ)
                     draw.text((5, 460), dataA0[0,iNews,0,1], '#FFFFFF', font=fontJ) # Initial title
        
                     img.save(f'yahoo/images3/{ijk}.jpg')
                     img.save(f'yahoo/images5/{LL}-{iNews}-{iGen}.jpg') 
        
                     img3=Image.open(f'yahoo/images3/{ijk}.jpg')
                     fx, fy = 1.800, 1.800
                     size = (round(img3.width * fx), round(img3.height * fx))

                     img3=img3.resize(size)

                     img3.show()
                     print('============ im show ==============')
                     print('sum=',sum)
                     tt2=time.time()-run2.value
                     tt3=time.time()-run3.value
                     print('run =',run.value,' run 2=',run2.value,int(tt2),'  run 3=',run3.value,int(tt3),'  run 4=',run4.value)
                     print('============ im show ============== ')
                     time.sleep(15)
#                    if tt2>30:
#                        run4.value=0
                 else:
                     time.sleep(0.1)
                     run2t=time.time()-run2.value
                     print('GEN  ...run t =',run2t,'run 4=',run4.value)
        
                 run2ss=time.time()-run2.value
                 print('GEN OUT  ...run t =',run2ss,'run 4=',run4.value)
                 if run2ss>30:
                     run4.value=0
#                time.sleep(30)  # Loop wait 
             print(' ')
             print('-----------------------------')
             print('Next Topic')
             print('-----------------------------')

             
    f.close()


def worker(run,run2,run3,run4):  # When ０　, this routine works 
    t11=time.time()-run2.value
    print('Out     run =',run.value,'run 2=',run2.value,'run 4=',run4.value)
    time.sleep(4)

def worker2(run,run2,run3,run4):  # When ０, this routine works 
    while True:
        conn, addr = s.accept()
        run4.value=1
        run2.value=int(time.time())
#       run3.value=int(time.time())
        print('IN 222 ...run =',run.value,'run 2=',run2.value,'run 4=',run4.value)
        print('===========================================================ボイス')
        print('===========================================================ボイス')
        print('===========================================================ボイス')
        print( 'Connected by', addr)
        data = conn.recv(1024)
        question=data.decode()
        print(question,'      ', question,'          ', question)
        print('===========================================================ボイス')
        print('===========================================================ボイス')
        print('===========================================================ボイス')
        time.sleep(1)
#       run4.value=0
        print('IN END ...run =',run.value,'run 2=',run2.value,'run 4=',run4.value)

t00=int(0)
t01=int(1)
t03=int(time.time())
run = Value("i", 1)  # At initial １ is out,  ０ is in #######################
run2= Value("i", t03)
run3= Value("i", t03)
run4= Value("i", 0)
p2= Process(target=worker2, args=(run,run2,run3,run4))
p2.start()

p = Process(target=yahoo_read, args=(run,run2,run3,run4))
p.start()


    
         
