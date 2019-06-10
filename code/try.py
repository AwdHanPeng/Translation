import pickle

def explore(file):
    with open(file, 'rb') as f:
        lines = pickle.load(f)
        sum_sentence = len(lines)
        print(sum_sentence)
        max_len = 0
        sum_sentence_len = 0
        for line in lines:
            sum_sentence_len += len(line)
            if len(line) > max_len:
                max_len = len(line)
        print('平均每句话几个单词{}'.format(sum_sentence_len / sum_sentence))
        print('max is {}'.format(max_len))

if __name__ == '__main__':
    explore('../data/test/test_src.pkl')  # 20588 平均每句话几个单词9.539731882650088 max is 38
    explore('../data/test/test_tgt.pkl')  # 20588 平均每句话几个单词8.733242665630465 max is 32
