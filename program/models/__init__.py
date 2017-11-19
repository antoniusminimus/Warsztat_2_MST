#importy
from mysql.connector import connect


from clcrypto import password_hash

#klasy
class User:

    def __init__(self):
        self.__id = -1
        self.username = ""
        self.email = ""
        self.__hashed_password = ""

    @property
    def id(self):
        return self.__id

    @property
    def hashed_password(self):
        return self.__hashed_password

    def set_password(self, password):
        self.__hashed_password = password_hash(password)

    def save_to_db(self, cursor):
        if self.__id == -1:
            # saving new instance using prepared statements
            sql = """INSERT INTO Users(username, email, hashed_password) VALUES(%s, %s, %s)"""
            values = (self.username, self.email, self.hashed_password)
            cursor.execute(sql, values)
            self.__id = cursor.lastrowid
            return True
        else:
            sql = """UPDATE Users SET username=%s, email=%s, hashed_password=%s WHERE id=%s"""
            values = (self.username, self.email, self.hashed_password, self.id)
            cursor.execute(sql, values)
            return True

    @staticmethod
    def load_user_by_id(cursor, id):
        sql = "SELECT id, username, email, hashed_password FROM USERS WHERE id=%(id)s"
        cursor.execute(sql, {'id': id})
        data = cursor.fetchone()
        if data is not None:
            loaded_user = User()
            loaded_user.__id = data[0]
            loaded_user.username = data[1]
            loaded_user.email = data[2]
            loaded_user.__hashed_password = data[3]
            return loaded_user
        else:
            return None

    @staticmethod
    def load_all_users(cursor):
        sql = "SELECT id, username, email, hashed_password FROM Users"
        ret = []
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            loaded_user = User()
            loaded_user.__id = row[0]
            loaded_user.username = row[1]
            loaded_user.email = row[2]
            loaded_user.__hashed_password = row[3]
            ret.append(loaded_user)
        return ret

    def delete(self, cursor):
        sql = "DELETE FROM Users WHERE id=%s"
        cursor.execute(sql, (self.__id,))
        self.__id = -1
        return True

if __name__ == '__main__':
    # a = User()
    # a.username = 'a'
    # a.email = 'a@mail.com'
    # print(a.set_password('aaa'))
    # print(a.hashed_password)
    cnx = connect(user="root", password="coderslab", host="127.0.0.1", database="warsztat")
    cursor = cnx.cursor()
    #a.save_to_db(cursor)
    a = User.load_user_by_id(cursor, 2)
    # for user in User.load_all_users(cursor):
    #     print(user.username)
    # a.username = 'ccc'
    # a.save_to_db(cursor)
    a.delete(cursor)
    cnx.commit()
    cursor.close()
    cnx.close()
