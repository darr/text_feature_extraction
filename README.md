# text_feature_extraction

text feature extraction using algorithms including CHI, DF, IG, MI for the experiment of text classification based on sougou online news  
基于卡方检验CHI，文档频率DF, 信息增益IG，互信息MI的文本特征提取与实现  

# How to run?

```shell
bash run.sh
```

This command will create the environment that needed by the models.  
This project is created on the purposes of easy-on-run.  
If you want to know the details about the models, just read code.  

note: data.txt is too big, I delete something.

data/data.txt: 搜狗文本分类语料库，共10个类别：  
'0': '汽车',  
'1': '财经',  
'2': 'IT',  
'3': '健康',  
'4': '体育',  
 '5': '旅游',  
'6': '教育',  
'7': '招聘',  
'9': '军事',  
 data.txt格式: category_id, word1 word2 word3 ...... wordn    
