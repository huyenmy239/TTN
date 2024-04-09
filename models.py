import pyodbc

class DatabaseModel:
    def __init__(self, server, database, login, pw):
        self.server = server
        self.database = database
        self.co_so = []
        self.server_list = []
        self.login = login
        self.pw = pw

    def find_driver(self):
        for d in pyodbc.drivers():
            if "ODBC" in d:
                return d

    def connect_to_database(self):
        DRIVER = "{" + self.find_driver() + "}"
        try:
            con = pyodbc.connect(
                f"Driver={DRIVER};"
                f"Server={self.server};"
                f"Database={self.database};"
                # "Trusted_Connection=yes;"
                f"UID={self.login};"
                f"PWD={self.pw};"
            )
        except Exception:
            return 0
        else:
            return con

    def load_co_so(self):
        con = self.connect_to_database()
        cur = con.cursor()

        try:
            v_sql = "SELECT * FROM V_DSPHANMANH"
            cur.execute(v_sql)

            rows = cur.fetchall()
            for row in rows:
                self.co_so.append(row[0])
                self.server_list.append(row[1])

        except Exception as e:
            print("Error:", e)

        finally:
            cur.close()
            con.close()

        for c in self.co_so:
            if "Tra cuu" in c:
                self.co_so.remove(c)


class Khoa:

    def __init__(self):
        self.ma_khoa: str
        self.ten_khoa: str
        self.ma_coso: str

    def load_data(self, con):
        cur = con.cursor()

        cur.execute(f"SELECT * FROM KHOA")

        rows = cur.fetchall()

        for row in rows:
            print(row)