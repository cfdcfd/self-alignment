## 本仓库用于保存self-alignment方法的系列脚本
使用python2.7编写

#### 自比对数据库建立
- 运行sumcontig.sh，获得sumcontig.fa

- 构建blast数据库如下
```
formatdb -i sumcontig.fa -p F -o T
```
- 文件夹中所有contig转换为数据库的脚本见contig2db.sh

#### blast比对
示例脚本见blastvdb.sh


#### blast数据预处理
用于删除冗余，减小比对后结果的大小
```
python filter_0.py -i ./filter_0/SRR341581 -o ./filter/SRR341581
python filter.py -i ./filter_0/SRR341581 -o ./filter/SRR341581
```

#### 统计分类比对得分
```
time python statsLM.py -i ./blastnlm/SRR341626_NLM -o ./test_result2
```
主要程序见statsLM.py,statsLM_1.py，两者的统计策略有细微差别
判别reads有效的原则：

1. 比对长度>60
2. 双端比对
3. 计算权重

statsLM.py不考虑双端比对的问题

#### 统计contig的独立性得分
主要程序见contig_stats.py
利用统计结果可以优化数据库，可参考脚本simple.py

其余.sh文件为部分胶水代码，供参考。