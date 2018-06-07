from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.linalg import norm


def tfidf_similarity(s1, s2):
    def add_space(s):
        return ' '.join(list(s))
    
    # 将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)
    # 转化为TF矩阵
    cv = TfidfVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
    print(vectors)
    # 计算TFIDF系数
    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))


s1 = '你在干嘛呢'
s2 = '你在干什么呢'
print(tfidf_similarity(s1, s2))
