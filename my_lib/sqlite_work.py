import sqlite3

# Осталось сделать - удаление, поиск таблиц, расширение таблиц, обновление таблиц


class SqlDataConn:

    def __init__(self, db_name):
        """Конструктор"""
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        """
        Открываем подключение с базой данных.
        """
        self.conn = sqlite3.connect(self.db_name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Закрываем подключение.
        """
        self.conn.close()
        if exc_val:
            raise

    def check_table(self, table_name):
        """
        Проверка наличия таблицы
        :param table_name: Имя таблицы
        :return: Истина/Ложь
        """
        text_requests = 'SELECT name from sqlite_master WHERE type = "table" AND name = "{}"'.format(table_name)

        cursor_obj = self.conn.cursor()
        cursor_obj.execute(text_requests)

        if len(cursor_obj.fetchall()):

            return True
        else:
            return False

    def create_table(self, table_name, **columns):
        """
        создание произвольной таблицы
        :param table_name: имя таблицы
        :param columns: колонки таблицы
        :return: нет
        """

        if self.conn is None:
            # Если база данных ещё не инициализирована - инициализировать
            self.__enter__()

        is_table = self.check_table(table_name)
        if is_table:
            # Таблица уже создана - проверить колонки, на будущее
            return

        text_request_create = "create table if not exists {}(".format(table_name)
        for key, value in columns.items():
            text_add = "{} {}".format(key, value)
            text_request_create += text_add + ","

        text_request_create = text_request_create[:-1] + ")"

        # noinspection PyBroadException
        try:
            cursor_obj = self.conn.cursor()
            cursor_obj.execute(text_request_create)
            self.conn.commit()

        except Exception:
            print('create table error\n {}'.format(text_request_create))

    def insert_into(self, table_name, **values):
        """
        Добавление данных в таблицу
        :param table_name: имя таблицы
        :param values: значения колонок
        :return:
        """

        is_table = self.check_table(table_name)
        if not is_table:
            # Если таблицы нет - создать
            self.create_table(table_name, values)

        text_request_insert = "insert into {}(".format(table_name)
        for key in values:
            text_add = "{}".format(key)
            text_request_insert += text_add + ","
        text_request_insert = text_request_insert[:-1] + ")"

        text_values = "?,"*len(values)
        text_values = text_values[:-1]

        text_request_insert += " values(" + text_values + ")"

        # noinspection PyBroadException
        try:
            cursor_obj = self.conn.cursor()
            cursor_obj.execute(text_request_insert, tuple(values.values()))
            self.conn.commit()
        except Exception:
            print('insert table error\n {}'.format(text_values))

    def select_from(self, table_name, global_criteria='AND', **columns):
        """
        Получает данные из базы
        :param global_criteria: глобальное условие отбора
        :param table_name: имя таблицы
        :param columns: колонки. если задано значение колонки - то отбор
        :return: список
        """
        is_table = self.check_table(table_name)
        if not is_table:
            return None

        text_request_select = ''
        text_find = ''

        for key, val in columns.items():
            text_request_select += key+','
            string_value = str(val)
            if len(string_value) > 0:
                text_find += key + ' ' + string_value + ' {} '.format(global_criteria)

        if len(text_request_select) == 0:
            text_request_select = '*'
        else:
            text_request_select = text_request_select[:-1]

        if len(text_find) != 0:
            text_find = 'WHERE ' + text_find
            text_find = text_find[:-len(' {} '.format(global_criteria))]

        text_request_select = 'SELECT {} FROM {} {}'.format(text_request_select, table_name, text_find)

        # noinspection PyBroadException
        try:
            cursor_obj = data_base.conn.cursor()
            cursor_obj.execute(text_request_select)
            return cursor_obj.fetchall()

        except Exception:
            print('insert table error\n {}'.format(text_request_select))
            return []


if __name__ == '__main__':

    data_base_name = 'test.db'

    with SqlDataConn(data_base_name) as data_base:

        data_base.create_table('album', name='TEXT', count='INTEGER')
        data_base.insert_into('album', name='vamia3', count=20)

        # rows = data_base.select_from('album', global_criteria='or', name='="vamia"', count='=202')
        rows = data_base.select_from('album', name='="vamia3"')
        print(rows)


