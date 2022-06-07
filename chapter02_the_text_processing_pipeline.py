#%%
# ! python -m spacy download pt_core_news_lg

import chunk
import spacy

#%%
nlp = spacy.load('pt_core_news_lg')


# %%

# doc = nlp(u'Todo dia eu acordo para estudar, principalmente Python. Estudar Python é muito legal e empolgante. Gosto muito de fazê-lo, estou estudando neste exato momento.')

doc = nlp(u'gosria de comprar três sapatos na cor preta')

#%%

[(word.text, word.lemma_, word.tag_, word.dep_) for word in doc]
# %%
[(word.text, word.head.text) for word in doc]

# %%
[word.lemma_ for word in doc if word.dep_=='ROOT' or word.dep_=='obl']

# %%
list(doc.sents)
# %%
doc
# %%
dir(doc)
# %%
doc.sentiment
# %%
doc.to_json()
# %%
list(doc.noun_chunks)
# %%
for token in doc:
    if token.pos_ == 'NOUN':
        chunk = ' '
        for w in token.children:
            if w.pos_ == 'DET' or w.pos_ == 'ADJ':
                chunk += w.text + ' '
    chunk += token.text        
chunk
# %%
doc
# %%
for token in doc:
    print(token, token.pos_,  spacy.explain(token.tag_))
# %%
token = doc[0]
# %%
list(token.rights)
# %%
list(doc.noun_chunks)
# %%
doc = nlp(u'Marcos Reis Ferreira comprou uma casa no Jardim Paulista em presidente prudente')
# %%
list(doc)
# %%
doc.ents
# %%
