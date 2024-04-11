from models import *
from views import *

DATABASE = "TTN"
SERVER_LIST = ["MIE"]
temp = DatabaseModel(server=SERVER_LIST[0], database=DATABASE, login="sa", pw="239003")
temp.load_co_so()
SERVER_LIST = SERVER_LIST + temp.server_list
COSO = temp.co_so

class LoginController:
    def __init__(self):
        self.coso = DatabaseModel(server=SERVER_LIST[0], database=DATABASE, login="sa", pw="239003")
        self.coso.load_co_so()
        self.view = LoginView(COSO)
        self.view.dn_gv_btn.configure(command=self.gv_login)
        self.view.dn_sv_btn.configure(command=self.sv_login)
        self.thongtin = []
        self.view.window.mainloop()

    def gv_login(self):
        username = self.view.dn_gv_user_entr.get()
        pw = self.view.dn_gv_pw_entr.get()

        if username == "" or pw == "":
            self.view.show_message("Lỗi", "Không được để trống tên đăng nhập hoặc mật khẩu.")
            return

        sv = ""
        if self.view.dn_gv_cbbox.get() == COSO[0]:
            sv = SERVER_LIST[1]
        else:
            sv = SERVER_LIST[2]

        server_dn = DatabaseModel(server=sv, database=DATABASE, login=username, pw=pw)

        con = server_dn.connect_to_database()
        if not con:
            self.view.show_message("Lỗi", "Tên đăng nhập hoặc mật khẩu sai.")
        else:
            cur = con.cursor()

            try:
                v_sql = f"EXEC SP_LayThongTinGiangVien '{username}'"
                cur.execute(v_sql)

                row = cur.fetchall()
                self.thongtin = row     

            except Exception as e:
                print("Error :", e)

            finally:
                cur.close()
                con.close()
        if self.thongtin:
            connect_info = [sv, DATABASE, username, pw]
            if self.thongtin[0][2].lower() == "coso":
                # Đóng cửa sổ hiện tại
                self.view.window.destroy()
                CoSoController(self.thongtin, connect_info)
            elif self.thongtin[0][2].lower() == "truong":
                self.view.window.destroy()
                TruongController(self.thongtin, connect_info)
            elif self.thongtin[0][2].lower() == "giangvien":
                self.view.window.destroy()
                GiangVienController(self.thongtin, connect_info)

    def sv_login(self):
        username = self.view.dn_sv_user_entr.get()
        pw = self.view.dn_sv_pw_entr.get()

        if username == "" or pw == "":
            self.view.show_message("Lỗi", "Không được để trống tên đăng nhập hoặc mật khẩu.")
            return

        server_dn = DatabaseModel(server=SERVER_LIST[1], database=DATABASE, login="lvt", pw="239003")

        con = server_dn.connect_to_database()
        cur = con.cursor()

        try:
            v_sql = f"EXEC SP_LayThongTinSinhVien '{username}', '{pw}'"
            cur.execute(v_sql)

            row = cur.fetchall()
            self.thongtin = row
            self.thongtin.append("Sinhvien")
            self.view.show_message("Thành công", f"Đăng nhập thành công. [{row}]")

        except Exception as e:
            self.view.show_message("Lỗi", "Tên đăng nhập hoặc mật khẩu sai.")

        finally:
            cur.close()
            con.close()

        if self.thongtin:
                # Đóng cửa sổ hiện tại
                self.view.window.destroy()
                        
                # Chuyển sang cửa sổ CoSoView
                SinhVienView(self.thongtin)



class CoSoController:
    def __init__(self, info: list, connect_info: list):
        self.info = info
        self.connect_info = connect_info
        self.server = DatabaseModel(server=self.connect_info[0], database=self.connect_info[1], login=self.connect_info[2], pw=self.connect_info[3])
        self.con = self.server.connect_to_database()
        self.cur = self.con.cursor()
        self.view = CoSoView(self.info, self.load_khoa(), self.load_giangvien(), self.load_lop(), self.load_sv(), self.load_mon(), self.load_bode())

        self.view.mon_add_button.configure(command=self.add_monhoc)
        self.view.mon_save_button.configure(command=self.save_monhoc)

        self.view.window.mainloop()

    def add_monhoc(self):
        self.view.mon_mamon_entry.delete(0, END)
        self.view.mon_tenmon_entry.delete(0, END)

    def save_monhoc(self):
        mamon = self.view.mon_mamon_entry.get().upper()
        tenmon = self.view.mon_tenmon_entry.get().upper()
        sp = f"SP_ThemMonHoc '{mamon}', N'{tenmon}'"
        try:
            self.cur.execute(sp)
            self.con.commit()
        except pyodbc.Error as e:
            show_message("Lỗi", e.args[1])

        self.view.draw_mon_table(self.load_mon())
        

    def load_khoa(self):
        v_sql = f"SELECT * FROM KHOA"
        self.cur.execute(v_sql)
        rows = self.cur.fetchall()
        return rows
    
    def load_giangvien(self):
        v_sql = f"SELECT * FROM GIAOVIEN"
        self.cur.execute(v_sql)
        rows = self.cur.fetchall()
        return rows
    
    def load_lop(self):
        v_sql = f"SELECT * FROM LOP"
        self.cur.execute(v_sql)
        rows = self.cur.fetchall()
        return rows
    
    def load_sv(self):
        v_sql = f"SELECT * FROM SINHVIEN"
        self.cur.execute(v_sql)
        rows = self.cur.fetchall()
        return rows
    
    def load_mon(self):
        v_sql = f"SELECT * FROM MONHOC"
        self.cur.execute(v_sql)
        rows = self.cur.fetchall()
        return rows
    
    def load_bode(self):
        v_sql = f"SELECT * FROM BODE"
        self.cur.execute(v_sql)
        rows = self.cur.fetchall()
        return rows


class TruongController:
    def __init__(self, info: list, connect_info: list):
        self.info = info
        self.connect_info = connect_info
        self.server = DatabaseModel(server=self.connect_info[0], database=self.connect_info[1], login=self.connect_info[2], pw=self.connect_info[3])
        con = self.server.connect_to_database()
        self.cur = con.cursor()
        self.view = TruongView(self.info, self.load_khoa(), self.load_giangvien(), self.load_lop(), self.load_sv(), self.load_mon(), self.load_bode())

    def load_khoa(self):
        v_sql = f"SELECT * FROM KHOA"
        self.cur.execute(v_sql)
        rows = self.cur.fetchall()
        return rows
    
    def load_giangvien(self):
        v_sql = f"SELECT * FROM GIAOVIEN"
        self.cur.execute(v_sql)
        rows = self.cur.fetchall()
        return rows
    
    def load_lop(self):
        v_sql = f"SELECT * FROM LOP"
        self.cur.execute(v_sql)
        rows = self.cur.fetchall()
        return rows
    
    def load_sv(self):
        v_sql = f"SELECT * FROM SINHVIEN"
        self.cur.execute(v_sql)
        rows = self.cur.fetchall()
        return rows
    
    def load_mon(self):
        v_sql = f"SELECT * FROM MONHOC"
        self.cur.execute(v_sql)
        rows = self.cur.fetchall()
        return rows
    
    def load_bode(self):
        v_sql = f"SELECT * FROM BODE"
        self.cur.execute(v_sql)
        rows = self.cur.fetchall()
        return rows


class GiangVienController:
    def __init__(self, info: list, connect_info: list):
        self.info = info
        self.connect_info = connect_info
        self.server = DatabaseModel(server=self.connect_info[0], database=self.connect_info[1], login=self.connect_info[2], pw=self.connect_info[3])
        con = self.server.connect_to_database()
        self.cur = con.cursor()
        self.view = GiangVienView(self.info, self.load_bode())

    def load_bode(self):
        v_sql = f"EXEC SP_LayCauHoiTheoMAGV '{self.info[0]}'"
        self.cur.execute(v_sql)
        rows = self.cur.fetchall()
        return rows


class SinhVienController:
    def __init__(self, info: list, connect_info: list):
        self.info = info
        self.connect_info = connect_info
        self.server = DatabaseModel(server=self.connect_info[0], database=self.connect_info[1], login=self.connect_info[2], pw=self.connect_info[3])
        con = self.server.connect_to_database()
        self.cur = con.cursor()
        self.view = SinhVienView(self.info, self.load_baithi(), self.load_chitiet())

    def load_baithi(self):
        v_sql = f"SELECT * FROM BAITHI"
        self.cur.execute(v_sql)
        rows = self.cur.fetchall()
        return rows
    
    def load_chitiet(self):
        v_sql = f"SELECT * FROM CT_BAITHI"
        self.cur.execute(v_sql)
        rows = self.cur.fetchall()
        return rows
    