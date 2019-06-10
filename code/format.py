'''
    cmn.txt->train_src.data, train_tgt.data
'''

def txt2str(path):
    Eng = []
    Chi = []
    with open(path, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            temp = line.replace('\n', '').split('\t')
            Eng.append(temp[0])
            Chi.append(temp[1])

if __name__ == '__main__':
    txt2str('./data/cmn.txt')
