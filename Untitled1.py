#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
sentence="""At eight o'clock on Thursday morning Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
tokens


# In[5]:


import nltk
from sklearn.feature_extraction import CountVectorizer
sentence="""At eight o'clock on Thursday morning Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
vectorizer=CountVectorizer()
print(tokens.toarray())


# In[7]:


nltk.download()


# In[10]:


from nltk.stem import PorterStemmer
from nltk import word_tokenize,pos_tag
sentencex = """At eight o'clock on Thursday morning Arthur didn't feel very good. luckily"""
[word for word in word_tokenize(sentencex)]
porter=PorterStemmer()
[porter.stem(word) for word in word_tokenize(sentencex)]


# In[19]:


from nltk.stem import SnowballStemmer
from nltk import word_tokenize,pos_tag
sentencex = """At eight o'clock on Thursday morning Arthur didn't feel very good. luckily there is no ambiguity in this city capacity """
[word for word in word_tokenize(sentencex)]
trystem=SnowballStemmer('english')
[trystem.stem(word) for word in word_tokenize(sentencex)]


# In[ ]:





# In[ ]:


("")

