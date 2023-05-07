import spacy 



def textSimilarity(text1,text2):
    # here check text similarity of a tweet and their retweet count
    nlp = spacy.load("en_core_web_sm")
    #nlp = spacy.load("en_core_web_md")

    doc1 = nlp(text1)
    doc2 = nlp(text2)
    return doc1.similarity(doc2)
    print('T1 and T2',doc1.similarity(doc2)) 

count=textSimilarity('protein12', 'allergic1')
if(count>=0.5):
    print("count is true")

print("count is false", count)

