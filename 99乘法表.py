import numpy as np
letters=np.array(list("qwertyuiopasdfghjklzxcvbnm"))
data=letters[np.random.randint(0,26,10000)]
features=set(data)
feat_dict={c:i for i,c in enumerate(sorted(features))}
print(feat_dict)
def transform(data, feat_dict):
    return [feat_dict[c] for c in data]
print(feat_dict.keys())
new_data=['n','b','a']
print(transform(new_data, feat_dict))