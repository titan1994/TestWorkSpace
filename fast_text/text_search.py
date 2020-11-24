import fasttext
import argparse
import numpy as np
import faiss
import math
import sqlite3


maxlen = 150
porog = 0.2

def func():

    conn = sqlite3.connect("/home/uadmin/Загрузки/fasttext1C/1c/nom1c.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    sql = "SELECT * FROM nomenclature"
    cursor.execute(sql)
    rows = cursor.fetchall()

    Nline = len(rows)

    dim = 32
    topn = 50

    nomen = []
    k = int(math.sqrt(Nline))
    quantiser = faiss.IndexFlatL2(dim)

    if opt.metric == '0':
        #     index = faiss.IndexIVFFlat(quantiser, dim, k, faiss.METRIC_L2)
        index = faiss.IndexFlat(dim, faiss.METRIC_L2)
    elif opt.metric == '1':
        index = faiss.IndexFlat(dim, faiss.METRIC_INNER_PRODUCT)
    elif opt.metric == '2':
        index = faiss.IndexFlat(dim, faiss.METRIC_L1)
    elif opt.metric == '3':
        index = faiss.IndexFlat(dim, faiss.METRIC_Linf)
    elif opt.metric == '4':
        index = faiss.IndexFlat(dim, faiss.METRIC_Lp)
    elif opt.metric == '5':
        index = faiss.IndexFlat(dim, faiss.METRIC_Canberra)
    elif opt.metric == '6':
        index = faiss.IndexFlat(dim, faiss.METRIC_BrayCurtis)
    elif opt.metric == '7':
        index = faiss.IndexFlat(dim, faiss.METRIC_JensenShannon)

    #if opt.metric == '0':
    #    index = faiss.IndexIVFFlat(quantiser, dim, k, faiss.METRIC_L2)
    #else:
    #    index = faiss.IndexIVFFlat(quantiser, dim, k, faiss.METRIC_INNER_PRODUCT)

    vectors = np.zeros((Nline, dim)).astype('float32')
    for i, row in enumerate(rows):
        vectors[i, :] = row[1:]
        nomen.append(row[0])
    # vectors = np.random.random((1000000, dim)).astype('float32')

    index.train(vectors)
    index.add(vectors)
    index.nprobe = 30

    model2 = fasttext.load_model("/home/uadmin/Загрузки/fasttext1C/1c/skipgram3.bin")
    query = model2.get_word_vector(opt.string)
    query = np.expand_dims(query, axis=1)
    query = query.transpose()

    D, I = index.search(query, topn)
    # print(query)
    # print(D)

    f = open('/home/uadmin/Загрузки/fasttext1C/vec.txt', 'w')
    #for i in I[0, :]:
    #    f.write(nomen[i] + '\n')
    itr = 0

    while itr < I.size:
        f.write('' + str(nomen[I.item(itr)]) + '|' + str(D.item(itr))+'\n')
        itr+=1
    f.close()

    #print(D.size)
    #print('re' + str(nomen[I.item(0)]) + str(D.item(0)))


    #f = open('/home/uadmin/Загрузки/fasttext1C/dec.txt', 'w')
    #for i in D[0, :]:
    #    f.write(str(i)+ '\n')
    #f.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--string', type=str, default='стол с-04-', help='')
    parser.add_argument('--metric', type=str, default='0', help='')

    opt = parser.parse_args()

    func()


