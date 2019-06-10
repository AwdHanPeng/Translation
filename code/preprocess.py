import pickle
from sklearn.model_selection import train_test_split
import nltk
import jieba

PAD_token = 0
BEG_token = 1
EOS_token = 2

class Voc:
    def __init__(self, lang):
        self.word2index = {'PAD': PAD_token, 'BEG': BEG_token, 'EOS': EOS_token}
        self.word2count = {}
        self.index2word = {PAD_token: "PAD", BEG_token: 'BEG', EOS_token: 'EOS'}
        self.num_words = 3
        self.lang = lang

    def add_word(self, word):
        if word not in self.word2index:
            self.word2index[word] = self.num_words
            self.word2count[word] = 1
            self.index2word[self.num_words] = word
            self.num_words += 1
        else:
            self.word2count[word] += 1

    def get_index(self, word):
        return self.word2index[word]

    def save_map(self):
        with open('../data/{}word2index.pkl'.format(self.lang), 'wb') as f:
            pickle.dump(self.word2index, f)
        print('complete to save {}word2index len = {}'.format(self.lang, self.num_words))
        with open('../data/{}index2word.pkl'.format(self.lang), 'wb') as f:
            pickle.dump(self.index2word, f)
        print('complete to save {}index2word len = {}'.format(self.lang, self.num_words))

def eng_token(str):
    return nltk.word_tokenize(str)

def chi_token(str):
    t = jieba.cut(str)
    t = ','.join(t)
    t = t.split(',')
    return t

def txt2list(path, save_path):
    source = []
    target = []

    with open(path, 'r', encoding='UTF-8') as f:
        count = 0
        lines = f.readlines()
        for line in lines:
            sentence = line.replace('\n', '').split('\t')
            eng = sentence[0]
            chi = sentence[1]
            eng = eng_token(eng)
            chi = chi_token(chi)
            count += 1
            if count % 100 == 0:
                print('{} sentence complete in raw train'.format(count))
            for i, word in enumerate(eng):
                eng_voc.add_word(word)
                eng[i] = eng_voc.get_index(word)
            for i, word in enumerate(chi):
                chi_voc.add_word(word)
                chi[i] = chi_voc.get_index(word)

            eng.insert(0, BEG_token)
            eng.append(EOS_token)
            source.append(eng)
            chi.insert(0, BEG_token)
            chi.append(EOS_token)
            target.append(chi)

    assert len(source) == len(target)
    print('prepare to save list')
    train_src_path, train_tgt_path, valid_src_path, valid_tgt_path, test_src_path, test_tgt_path = save_path
    train_src, test_src, train_tgt, test_tgt = train_test_split(source, target, test_size=0.01)
    train_src, valid_src, train_tgt, valid_tgt = train_test_split(train_src, train_tgt, test_size=0.01)
    assert len(train_src) == len(train_tgt)
    assert len(test_src) == len(test_tgt)
    assert len(valid_src) == len(valid_tgt)
    print('Train Dataset: Valid Dataset: Test Dataset = {:.2f}%： {:.2f}%： {:.2f}%'.format(
        100. * len(train_src) / len(source),
        100. * len(valid_src) / len(source),
        100. * len(test_src) / len(source)))

    with open(train_src_path, 'wb') as f:
        pickle.dump(train_src, f)
    with open(train_tgt_path, 'wb') as f:
        pickle.dump(train_tgt, f)
    print('complete to save train dataset')

    with open(valid_src_path, 'wb') as f:
        pickle.dump(valid_src, f)
    with open(valid_tgt_path, 'wb') as f:
        pickle.dump(valid_tgt, f)
    print('complete to save valid dataset')

    with open(test_src_path, 'wb') as f:
        pickle.dump(test_src, f)
    with open(test_tgt_path, 'wb') as f:
        pickle.dump(test_tgt, f)
    print('complete to save test dataset')

if __name__ == '__main__':
    eng_voc = Voc('ENG')
    chi_voc = Voc('CHI')
    '''
    src_path, tgt_path = path
    train_src_path, train_tgt_path, valid_src_path, valid_tgt_path, test_src_path, test_tgt_path = save_path
    '''
    print('come on')
    txt2list('../data/cmn.txt', [
        '../data/train/train_src.pkl', '../data/train/train_tgt.pkl',
        '../data/valid/valid_src.pkl', '../data/valid/valid_tgt.pkl',
        '../data/test/test_src.pkl', '../data/test/test_tgt.pkl'
    ])
    eng_voc.save_map()
    chi_voc.save_map()
