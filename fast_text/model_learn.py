import fasttext
import argparse
import sqlite3

def func():
    conn = sqlite3.connect("/home/uadmin/Загрузки/fasttext1C/1c/nom1c.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()

    vector_dim = 32

    sql = "DELETE FROM nomenclature"
    cursor.execute(sql)
    conn.commit()

    if opt.string == 'refresh':

        model = fasttext.train_unsupervised('/home/uadmin/Загрузки/fasttext1C/1c/data/os_pochta.txt', model='skipgram', dim=vector_dim, epoch=200, minn=2, maxn=6)
        model.save_model("skipgram3.bin")

    model = fasttext.load_model("/home/uadmin/Загрузки/fasttext1C/1c/skipgram3.bin")

    num = []
    with open('/home/uadmin/Загрузки/fasttext1C/1c/data/os_pochta.txt', 'r') as r:
        for line in r.readlines():
            parts = line.split(';')
            s = parts[1].replace('\n', '')
            b = [str(x) for x in model.get_word_vector(s)]
            num.append((parts[0], ) + tuple(b))


    cursor.executemany("INSERT INTO nomenclature VALUES (" + ','.join(['?'] * (vector_dim+1)) + ")", num)
    #cursor.executemany("INSERT INTO nomenclature VALUES (?,\
    #                                               ?,?,?,?,?,?,?,?,?,?,\
    #                                               ?,?,?,?,?,?,?,?,?,?,\
    #                                               ?,?,?,?,?,?,?,?,?,?,\
    #                                               ?,?)", num)
    conn.commit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--string', type=str, default='', help='')

    opt = parser.parse_args()

    func()


