Transformer：
英文词库6981个单词，中文词库13837个单词
单句话最大长度为20个单词
PAD_TOKEN=0,BEG_TOKEN=1,EOS_TOKEN=2
模型decoder和encoder层数均为6层，D_model为512维，D_ff为2048维
muti-head中多头h=8 dropout=0.1
参数初始化方法为xavier_uniform
使用Adam优化器优化，学习率调整算法为论文中原始算法。
对true label使用labelsmoothing平滑
bleu值为41.5184%（unigram）
