import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

file = open('1974-Schmidt-SPD.nostop', 'r')
string = file.read()
final_list = list(string.split(" "))

top_terms = pd.DataFrame(columns=range(1, 6))
tfidf = TfidfVectorizer()
tfidf_vectors = tfidf.fit_transform(final_list)
term_doc_mat = pd.DataFrame(tfidf_vectors.todense(), columns=tfidf.vocabulary_)
for i in term_doc_mat.index:
    top_terms.loc[len(top_terms)] = term_doc_mat.loc[i].sort_values(ascending=False)[0:5].index
print(top_terms)