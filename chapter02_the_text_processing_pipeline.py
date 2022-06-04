#%%
# ! python -m spacy download pt_core_news_lg

import spacy

#%%
nlp = spacy.load('pt_core_news_lg')


# %%

# doc = nlp(u'Todo dia eu acordo para estudar, principalmente Python. Estudar Python é muito legal e empolgante. Gosto muito de fazê-lo, estou estudando neste exato momento.')

doc = nlp(u'sempre viajo para Minas')

#%%

[(word.text, word.lemma_, word.tag_, word.dep_) for word in doc]
# %%
[(word.text, word.head.text) for word in doc]

# %%
[word.lemma_ for word in doc if word.dep_=='ROOT' or word.dep_=='obl']

# %%
