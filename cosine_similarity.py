from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = ['London Paris London', 'Paris Paris London']
cv = CountVectorizer()
cv_fit=cv.fit_transform(text)

#print(cv.get_feature_names())
#print(cv_fit.toarray())

print(cosine_similarity(cv_fit))