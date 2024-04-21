import os

import tkinter as tk
from tkinter import messagebox
from customtkinter import *
from ttkbootstrap.tableview import Tableview
from PIL import Image

WIDTH = 1200
HEIGHT = 675
curr_dir = os.path.dirname(os.path.abspath(__file__))

def show_message(title: str, mess: str):
        messagebox.showerror(title, mess)

class LoginView:
    def __init__(self,co_so: list):

        self.window = CTk()
        self.window.geometry(f"{WIDTH}x{HEIGHT}")
        self.window.title("Thi trắc nghiệm")

        self.co_so = co_so

        self.header_tab = CTkTabview(self.window, anchor="nw", corner_radius=0,
                              fg_color="white", segmented_button_selected_color	="white",
                              text_color="black", segmented_button_fg_color="#a3a3a3",
                              segmented_button_selected_hover_color="#d9d9d9")
        self.header_tab.pack(expand=True, fill="both")
        self.header_tab.add("Đăng nhập")
        self.header_tab.add("Đăng ký")

        # Phần Đăng nhập
        self.dn_main_frame = CTkFrame(self.header_tab.tab("Đăng nhập"), fg_color="white")
        self.dn_main_frame.pack(side="top", fill="both", expand=True)

        self.dn_main_tab = CTkTabview(self.dn_main_frame, segmented_button_fg_color="white",
                                   fg_color="white", corner_radius=0)
        self.dn_main_tab.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.dn_main_tab.add("GIẢNG VIÊN")
        self.dn_main_tab.add("SINH VIÊN")

        # Phần Đăng nhập - Giảng viên
        self.dn_gv_frame = CTkFrame(self.dn_main_tab.tab("GIẢNG VIÊN"), fg_color="white")
        self.dn_gv_frame.pack(side="top", fill="both", expand=True)

        self.dn_gv_cbbox = CTkComboBox(self.dn_gv_frame, values=self.co_so, corner_radius=1,
                             fg_color="#dff5ff", border_color="#dff5ff",
                             button_color="#dff5ff", button_hover_color="#cff5ff")
        self.dn_gv_cbbox.pack(fill="x", side="top", pady=10)
        self.dn_gv_cbbox.set(self.co_so[0])

        self.dn_gv_user_entr = CTkEntry(self.dn_gv_frame, placeholder_text="Tên đăng nhập",
                                   corner_radius=1, height=35)
        self.dn_gv_user_entr.pack(fill="x")

        self.dn_gv_pw_entr = CTkEntry(self.dn_gv_frame, placeholder_text="Mật khẩu", show="•",
                                 corner_radius=1, height=35)
        self.dn_gv_pw_entr.pack(fill="x", pady=10)

        self.dn_gv_btn = CTkButton(self.dn_gv_frame, text="Đăng nhập", width=100, text_color="white",
                             corner_radius=1)
        self.dn_gv_btn.pack()

        # Phần Đăng nhập - Sinh viên
        self.dn_sv_frame = CTkFrame(self.dn_main_tab.tab("SINH VIÊN"), fg_color="white")
        self.dn_sv_frame.pack(side="top", fill="both", expand=True)

        self.dn_sv_cbbox = CTkComboBox(self.dn_sv_frame, values=self.co_so, corner_radius=1,
                             fg_color="#dff5ff", border_color="#dff5ff",
                             button_color="#dff5ff", button_hover_color="#cff5ff")
        self.dn_sv_cbbox.pack(fill="x", side="top", pady=10)
        self.dn_sv_cbbox.set(self.co_so[0])

        self.dn_sv_user_entr = CTkEntry(self.dn_sv_frame, placeholder_text="Mã số sinh viên",
                                   corner_radius=1, height=35)
        self.dn_sv_user_entr.pack(fill="x")

        self.dn_sv_pw_entr = CTkEntry(self.dn_sv_frame, placeholder_text="Mật khẩu", show="•",
                                 corner_radius=1, height=35)
        self.dn_sv_pw_entr.pack(fill="x", pady=10)

        self.dn_sv_btn = CTkButton(self.dn_sv_frame, text="Đăng nhập", width=100, text_color="white",
                             corner_radius=1)
        self.dn_sv_btn.pack()


        # Phần Đăng ký
        self.dk_main_frame = CTkFrame(self.header_tab.tab("Đăng ký"), fg_color="white")
        self.dk_main_frame.pack(side="top", fill="both", expand=True)

        self.dk_main_tab = CTkTabview(self.dk_main_frame, segmented_button_fg_color="white",
                                   fg_color="white", corner_radius=0)
        self.dk_main_tab.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.dk_main_tab.add("GIẢNG VIÊN")
        self.dk_main_tab.add("SINH VIÊN")
        self.dk_main_tab.set("SINH VIÊN")

        # Phần Đăng ký - Giảng viên
        self.dk_gv_frame = CTkFrame(self.dk_main_tab.tab("GIẢNG VIÊN"), fg_color="white")
        self.dk_gv_frame.pack(side="top", fill="both", expand=True)

        self.dk_gv_cbbox = CTkComboBox(self.dk_gv_frame, values=self.co_so, corner_radius=1,
                             fg_color="#dff5ff", border_color="#dff5ff", button_color="#dff5ff",
                            button_hover_color="#cff5ff", state="disabled")
        self.dk_gv_cbbox.pack(fill="x", side="top", pady=10)
        self.dk_gv_cbbox.set(self.co_so[0])

        self.dk_gv_user_entr = CTkEntry(self.dk_gv_frame, placeholder_text="Tên đăng nhập",
                                   corner_radius=1, height=35, state="disabled")
        self.dk_gv_user_entr.pack(fill="x")

        self.dk_gv_pw_entr = CTkEntry(self.dk_gv_frame, placeholder_text="Mật khẩu", show="•",
                                 corner_radius=1, height=35, state="disabled")
        self.dk_gv_pw_entr.pack(fill="x", pady=10)

        self.dk_gv_btn = CTkButton(self.dk_gv_frame, text="Đăng ký", width=100, text_color="white",
                             corner_radius=1, state="disabled")
        self.dk_gv_btn.pack()

        # Phần Đăng ký - Sinh viên
        self.dk_sv_frame = CTkFrame(self.dk_main_tab.tab("SINH VIÊN"), fg_color="white")
        self.dk_sv_frame.pack(side="top", fill="both", expand=True)

        self.dk_sv_cbbox = CTkComboBox(self.dk_sv_frame, values=self.co_so, corner_radius=1,
                             fg_color="#dff5ff", border_color="#dff5ff",
                             button_color="#dff5ff", button_hover_color="#cff5ff")
        self.dk_sv_cbbox.pack(fill="x", side="top", pady=10)
        self.dk_sv_cbbox.set(self.co_so[0])

        self.dk_sv_user_entr = CTkEntry(self.dk_sv_frame, placeholder_text="Mã số sinh viên",
                                   corner_radius=1, height=35)
        self.dk_sv_user_entr.pack(fill="x")

        self.dk_sv_pw_entr = CTkEntry(self.dk_sv_frame, placeholder_text="Mật khẩu", show="•",
                                 corner_radius=1, height=35)
        self.dk_sv_pw_entr.pack(fill="x", pady=10)

        self.dk_sv_btn = CTkButton(self.dk_sv_frame, text="Đăng ký", width=100, text_color="white",
                             corner_radius=1)
        self.dk_sv_btn.pack()

    def show_message(self, title: str, mess: str):
        messagebox.showerror(title, mess)


class CoSoView:
    def __init__(self, info: list, khoa_data: list, gv_data: list, lop_data: list, sv_data: list, mon_data: list, bode_data: list):
        self.info = info

        # Biến update
        self.update_var = False
        # Biến selected
        self.selected_var = ""

        self.window = CTk()
        self.window.geometry(f"{WIDTH}x{HEIGHT}")
        self.window.title("Thi trắc nghiệm")
        self.window.configure(fg_color="#ababab")

        self.infor_bar = CTkFrame(self.window, height=50, fg_color="#ababab")
        self.infor_bar.pack(fill="x")

        str_infor = f"Mã: {self.info[0][0]}   Tên: {self.info[0][1].title()}   Nhóm: {self.info[0][2]}"

        self.infor_label = CTkLabel(self.infor_bar, text=f"{str_infor}", font=("arial", 16), text_color="white")
        self.infor_label.place(relx=0.6, rely=0.19)

        self.header_tab = CTkTabview(self.window, anchor="nw", corner_radius=0,
                              fg_color="#dff5ff", segmented_button_selected_color="white",
                              text_color="black", segmented_button_fg_color="#a3a3a3",
                              segmented_button_selected_hover_color="#dff5ff",
                              segmented_button_unselected_color="#dff5ff")
        self.header_tab.place(relx=0.0, rely=0.05, relheight=1, relwidth=1)
        self.header_tab.add("Khoa")
        self.header_tab.add("Giảng viên")
        self.header_tab.add("Lớp")
        self.header_tab.add("Sinh viên")
        self.header_tab.add("Môn học")
        self.header_tab.add("Bộ đề")


        # Icon Image
        add_path = os.path.join(curr_dir, "icons", "add.png")
        add_img = CTkImage(light_image=Image.open(add_path))

        del_path = os.path.join(curr_dir, "icons", "bin.png")
        del_img = CTkImage(light_image=Image.open(del_path))

        rel_path = os.path.join(curr_dir, "icons", "reload.png")
        rel_img = CTkImage(light_image=Image.open(rel_path))

        save_path = os.path.join(curr_dir, "icons", "save.png")
        save_img = CTkImage(light_image=Image.open(save_path))

        undo_path = os.path.join(curr_dir, "icons", "undo.png")
        undo_img = CTkImage(light_image=Image.open(undo_path))


        # Phần Khoa
        self.khoa_main_frame = CTkFrame(self.header_tab.tab("Khoa"), fg_color="white", width=HEIGHT, height=HEIGHT/5*3)
        self.khoa_main_frame.place(relx = 1, rely = 0.95, relwidth = 1, relheight = 0.6, anchor="se")
        self.khoa_main_frame.grid_rowconfigure(0, weight=1)
        self.khoa_main_frame.grid_columnconfigure(0, weight=1)

        khoa_heading = [
            {"text": "Mã khoa", "stretch": True},
            {"text": "Tên khoa", "stretch": True},
            {"text": "Mã cơ sở", "stretch": True},
        ]

        khoa_row = []
        for row in khoa_data:
            khoa_row.append((row[0], row[1], row[2]))

        self.khoa_table = Tableview(
            master=self.khoa_main_frame,
            coldata=khoa_heading,
            rowdata=khoa_row,
            paginated=True,
            searchable=True,
            pagesize=15,
        )
        self.khoa_table.grid(row=0, column=0, sticky="nsew")


        # Phần Giảng viên
        self.gv_main_frame = CTkFrame(self.header_tab.tab("Giảng viên"), fg_color="white", width=HEIGHT, height=HEIGHT/5*3)
        self.gv_main_frame.place(relx = 1, rely = 0.95, relwidth = 1, relheight = 0.6, anchor="se")
        self.gv_main_frame.grid_rowconfigure(0, weight=1)
        self.gv_main_frame.grid_columnconfigure(0, weight=1)

        gv_heading = [
            {"text": "Mã giảng viên", "stretch": True},
            {"text": "Họ", "stretch": True},
            {"text": "Tên", "stretch": True},
            {"text": "Địa chỉ", "stretch": True},
            {"text": "Mã khoa", "stretch": True},
        ]

        gv_row = []
        for row in gv_data:
            gv_row.append((row[0], row[1], row[2], row[3], row[4]))

        self.gv_table = Tableview(
            master=self.gv_main_frame,
            coldata=gv_heading,
            rowdata=gv_row,
            paginated=True,
            searchable=True,
            pagesize=15,
        )
        self.gv_table.grid(row=0, column=0, sticky="nsew")


        # Phần Lớp
        self.lop_main_frame = CTkFrame(self.header_tab.tab("Lớp"), fg_color="white", width=HEIGHT, height=HEIGHT/5*3)
        self.lop_main_frame.place(relx = 1, rely = 0.95, relwidth = 1, relheight = 0.6, anchor="se")
        self.lop_main_frame.grid_rowconfigure(0, weight=1)
        self.lop_main_frame.grid_columnconfigure(0, weight=1)

        lop_heading = [
            {"text": "Mã lớp", "stretch": True},
            {"text": "Tên lớp", "stretch": True},
            {"text": "Mã khoa", "stretch": True},
        ]

        lop_row = []
        for row in lop_data:
            lop_row.append((row[0], row[1], row[2]))

        self.lop_table = Tableview(
            master=self.lop_main_frame,
            coldata=lop_heading,
            rowdata=lop_row,
            paginated=True,
            searchable=True,
            pagesize=15,
        )
        self.lop_table.grid(row=0, column=0, sticky="nsew")


        # Phần Sinh viên
        self.sv_main_frame = CTkFrame(self.header_tab.tab("Sinh viên"), fg_color="white", width=HEIGHT, height=HEIGHT/5*3)
        self.sv_main_frame.place(relx = 1, rely = 0.95, relwidth = 1, relheight = 0.6, anchor="se")
        self.sv_main_frame.grid_rowconfigure(0, weight=1)
        self.sv_main_frame.grid_columnconfigure(0, weight=1)

        sv_heading = [
            {"text": "Mã sinh viên", "stretch": True},
            {"text": "Họ", "stretch": True},
            {"text": "Tên", "stretch": True},
            {"text": "Ngày sinh", "stretch": True},
            {"text": "Địa chỉ", "stretch": True},
            {"text": "Mã lớp", "stretch": True},
        ]

        sv_row = []
        for row in sv_data:
            sv_row.append((row[0], row[1], row[2], row[3], row[4], row[5]))

        self.sv_table = Tableview(
            master=self.sv_main_frame,
            coldata=sv_heading,
            rowdata=sv_row,
            paginated=True,
            searchable=True,
            pagesize=15,
        )
        self.sv_table.grid(row=0, column=0, sticky="nsew")


        # Phần Môn học
        self.mon_feat_frame = CTkFrame(self.header_tab.tab("Môn học"))
        self.mon_feat_frame.place(relx=0, rely=0, relwidth=1, relheight=0.35)

        self.mon_button_frame = CTkFrame(self.mon_feat_frame, fg_color="#dff5ff")
        self.mon_entry_frame = CTkFrame(self.mon_feat_frame, fg_color="#dff5ff")
        self.mon_button_frame.pack(expand=True, fill="both")
        self.mon_entry_frame.pack(expand=True, fill="both")

        self.mon_add_button = CTkButton(self.mon_button_frame, text="Thêm", width=100, image=add_img)
        self.mon_del_button = CTkButton(self.mon_button_frame, text="Xóa", width=100, image=del_img)
        self.mon_save_button = CTkButton(self.mon_button_frame, text="Ghi", width=100, image=save_img)
        self.mon_reload_button = CTkButton(self.mon_button_frame, text="Tải lại", width=100, image=rel_img)
        self.mon_undo_button = CTkButton(self.mon_button_frame, text="Phục hồi", width=100,image=undo_img)

        self.mon_add_button.pack(side="left", expand=True, pady=10)
        self.mon_del_button.pack(side="left", expand=True, pady=10)
        self.mon_save_button.pack(side="left", expand=True, pady=10)
        self.mon_reload_button.pack(side="left", expand=True, pady=10)
        self.mon_undo_button.pack(side="left", expand=True, pady=10)

        self.mon_mamon_entry = CTkEntry(self.mon_entry_frame, placeholder_text="Mã môn", height=35)
        # self.mon_mamon_entry.configure(state="readonly")
        self.mon_tenmon_entry = CTkEntry(self.mon_entry_frame, placeholder_text="Tên môn", height=35, fg_color="white")

        self.mon_mamon_entry.pack(side="left", expand=True, fill="x", padx=30)
        self.mon_tenmon_entry.pack(side="left", expand=True, fill="x", padx=30)

        # l1 = CTkLabel(self.mon_feat_frame, text="label1", fg_color="blue")
        # l2 = CTkLabel(self.mon_feat_frame, text="label1", fg_color="yellow")
        # l1.pack(expand=True, fill="both")
        # l2.pack(expand=True, fill="both")

        self.mon_main_frame = CTkFrame(self.header_tab.tab("Môn học"), fg_color="white", width=HEIGHT, height=HEIGHT/5*3)
        self.mon_main_frame.place(relx = 1, rely = 0.95, relwidth = 1, relheight = 0.6, anchor="se")
        self.mon_main_frame.grid_rowconfigure(0, weight=1)
        self.mon_main_frame.grid_columnconfigure(0, weight=1)


        # Tạo bảng môn học
        self.mon_table = self.draw_mon_table(mon_data)

        self.mon_table.view.bind("<ButtonRelease-1>", self.set_mon_entry)


        # Phần Bộ đề
        self.bode_main_frame = CTkFrame(self.header_tab.tab("Bộ đề"), fg_color="white", width=HEIGHT, height=HEIGHT/5*3)
        self.bode_main_frame.place(relx = 1, rely = 0.95, relwidth = 1, relheight = 0.6, anchor="se")
        self.bode_main_frame.grid_rowconfigure(0, weight=1)
        self.bode_main_frame.grid_columnconfigure(0, weight=1)

        bode_heading = [
            {"text": "Câu hỏi", "stretch": True},
            {"text": "Mã môn học", "stretch": True},
            {"text": "Trình độ", "stretch": True},
            {"text": "Nội dung", "stretch": True},
            {"text": "A", "stretch": True},
            {"text": "B", "stretch": True},
            {"text": "C", "stretch": True},
            {"text": "D", "stretch": True},
            {"text": "Đáp án", "stretch": True},
            {"text": "Mã giáo viên", "stretch": True},
        ]

        bode_row = []
        for row in bode_data:
            bode_row.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

        self.bode_table = Tableview(
            master=self.bode_main_frame,
            coldata=bode_heading,
            rowdata=bode_row,
            paginated=True,
            searchable=True,
            pagesize=15,
        )
        self.bode_table.grid(row=0, column=0, sticky="nsew")

    def get_selected_row(self, event):
        # self.mon_mamon_entry.configure(state="normal")
        self.update_var = True
        row = self.mon_table.get_rows(selected=True)
        # self.mon_mamon_entry.configure(state="readonly")
        return row[0].values

    def set_mon_entry(self, event):
        values = self.get_selected_row(event)

        # Thay đổi biến selected
        self.selected_var = values[0]
        
        self.mon_mamon_entry.configure(state="normal")
        self.mon_mamon_entry.delete(0, END)
        self.mon_mamon_entry.insert(0, values[0])
        self.mon_tenmon_entry.delete(0, END)
        self.mon_tenmon_entry.insert(0, values[1])
        self.mon_mamon_entry.configure(state="readonly")

    def draw_mon_table(self, mon_data):
        mon_heading = [
            {"text": "Mã môn học", "stretch": True},
            {"text": "Tên môn học", "stretch": True},
        ]

        mon_row = []
        for row in mon_data:
            mon_row.append((row[0], row[1]))

        mon_table = Tableview(
            master=self.mon_main_frame,
            coldata=mon_heading,
            rowdata=mon_row,
            paginated=True,
            searchable=True,
            pagesize=15,
        )
        mon_table.grid(row=0, column=0, sticky="nsew")

        mon_table.view.bind("<ButtonRelease-1>", self.set_mon_entry)

        return mon_table


class TruongView:
    def __init__(self, info: list, khoa_data: list, gv_data: list, lop_data: list, sv_data: list, mon_data: list, bode_data: list):
        self.info = info

        self.window = CTk()
        self.window.geometry(f"{WIDTH}x{HEIGHT}")
        self.window.title("Thi trắc nghiệm")
        self.window.configure(fg_color="#ababab")

        self.infor_bar = CTkFrame(self.window, height=50, fg_color="#ababab")
        self.infor_bar.pack(fill="x")

        str_infor = f"Mã: {self.info[0][0]}   Tên: {self.info[0][1].title()}   Nhóm: {self.info[0][2]}"

        self.infor_label = CTkLabel(self.infor_bar, text=f"{str_infor}", font=("arial", 16), text_color="white")
        self.infor_label.place(relx=0.6, rely=0.19)

        self.header_tab = CTkTabview(self.window, anchor="nw", corner_radius=0,
                              fg_color="#dff5ff", segmented_button_selected_color="white",
                              text_color="black", segmented_button_fg_color="#a3a3a3",
                              segmented_button_selected_hover_color="#d9d9d9")
        self.header_tab.place(relx=0.0, rely=0.05, relheight=1, relwidth=1)
        self.header_tab.add("Khoa")
        self.header_tab.add("Giảng viên")
        self.header_tab.add("Lớp")
        self.header_tab.add("Sinh viên")
        self.header_tab.add("Môn học")
        self.header_tab.add("Bộ đề")


        # Phần Khoa
        self.khoa_main_frame = CTkFrame(self.header_tab.tab("Khoa"), fg_color="white", width=HEIGHT, height=HEIGHT/5*3)
        self.khoa_main_frame.place(relx = 1, rely = 0.95, relwidth = 1, relheight = 0.6, anchor="se")
        self.khoa_main_frame.grid_rowconfigure(0, weight=1)
        self.khoa_main_frame.grid_columnconfigure(0, weight=1)

        khoa_heading = [
            {"text": "Mã khoa", "stretch": True},
            {"text": "Tên khoa", "stretch": True},
            {"text": "Mã cơ sở", "stretch": True},
        ]

        khoa_row = []
        for row in khoa_data:
            khoa_row.append((row[0], row[1], row[2]))

        self.khoa_table = Tableview(
            master=self.khoa_main_frame,
            coldata=khoa_heading,
            rowdata=khoa_row,
            paginated=True,
            searchable=True,
            pagesize=15,
        )
        self.khoa_table.grid(row=0, column=0, sticky="nsew")


        # Phần Giảng viên
        self.gv_main_frame = CTkFrame(self.header_tab.tab("Giảng viên"), fg_color="white", width=HEIGHT, height=HEIGHT/5*3)
        self.gv_main_frame.place(relx = 1, rely = 0.95, relwidth = 1, relheight = 0.6, anchor="se")
        self.gv_main_frame.grid_rowconfigure(0, weight=1)
        self.gv_main_frame.grid_columnconfigure(0, weight=1)

        gv_heading = [
            {"text": "Mã giảng viên", "stretch": True},
            {"text": "Họ", "stretch": True},
            {"text": "Tên", "stretch": True},
            {"text": "Địa chỉ", "stretch": True},
            {"text": "Mã khoa", "stretch": True},
        ]

        gv_row = []
        for row in gv_data:
            gv_row.append((row[0], row[1], row[2], row[3], row[4]))

        self.gv_table = Tableview(
            master=self.gv_main_frame,
            coldata=gv_heading,
            rowdata=gv_row,
            paginated=True,
            searchable=True,
            pagesize=15,
        )
        self.gv_table.grid(row=0, column=0, sticky="nsew")


        # Phần Lớp
        self.lop_main_frame = CTkFrame(self.header_tab.tab("Lớp"), fg_color="white", width=HEIGHT, height=HEIGHT/5*3)
        self.lop_main_frame.place(relx = 1, rely = 0.95, relwidth = 1, relheight = 0.6, anchor="se")
        self.lop_main_frame.grid_rowconfigure(0, weight=1)
        self.lop_main_frame.grid_columnconfigure(0, weight=1)

        lop_heading = [
            {"text": "Mã lớp", "stretch": True},
            {"text": "Tên lớp", "stretch": True},
            {"text": "Mã khoa", "stretch": True},
        ]

        lop_row = []
        for row in lop_data:
            lop_row.append((row[0], row[1], row[2]))

        self.lop_table = Tableview(
            master=self.lop_main_frame,
            coldata=lop_heading,
            rowdata=lop_row,
            paginated=True,
            searchable=True,
            pagesize=15,
        )
        self.lop_table.grid(row=0, column=0, sticky="nsew")


        # Phần Sinh viên
        self.sv_main_frame = CTkFrame(self.header_tab.tab("Sinh viên"), fg_color="white", width=HEIGHT, height=HEIGHT/5*3)
        self.sv_main_frame.place(relx = 1, rely = 0.95, relwidth = 1, relheight = 0.6, anchor="se")
        self.sv_main_frame.grid_rowconfigure(0, weight=1)
        self.sv_main_frame.grid_columnconfigure(0, weight=1)

        sv_heading = [
            {"text": "Mã sinh viên", "stretch": True},
            {"text": "Họ", "stretch": True},
            {"text": "Tên", "stretch": True},
            {"text": "Ngày sinh", "stretch": True},
            {"text": "Địa chỉ", "stretch": True},
            {"text": "Mã lớp", "stretch": True},
        ]

        sv_row = []
        for row in sv_data:
            sv_row.append((row[0], row[1], row[2], row[3], row[4], row[5]))

        self.sv_table = Tableview(
            master=self.sv_main_frame,
            coldata=sv_heading,
            rowdata=sv_row,
            paginated=True,
            searchable=True,
            pagesize=15,
        )
        self.sv_table.grid(row=0, column=0, sticky="nsew")


        # Phần Môn học
        self.mon_main_frame = CTkFrame(self.header_tab.tab("Môn học"), fg_color="white", width=HEIGHT, height=HEIGHT/5*3)
        self.mon_main_frame.place(relx = 1, rely = 0.95, relwidth = 1, relheight = 0.6, anchor="se")
        self.mon_main_frame.grid_rowconfigure(0, weight=1)
        self.mon_main_frame.grid_columnconfigure(0, weight=1)

        mon_heading = [
            {"text": "Mã môn học", "stretch": True},
            {"text": "Tên môn học", "stretch": True},
        ]

        mon_row = []
        for row in mon_data:
            mon_row.append((row[0], row[1]))

        self.mon_table = Tableview(
            master=self.mon_main_frame,
            coldata=mon_heading,
            rowdata=mon_row,
            paginated=True,
            searchable=True,
            pagesize=15,
        )
        self.mon_table.grid(row=0, column=0, sticky="nsew")


        # Phần Bộ đề
        self.bode_main_frame = CTkFrame(self.header_tab.tab("Bộ đề"), fg_color="white", width=HEIGHT, height=HEIGHT/5*3)
        self.bode_main_frame.place(relx = 1, rely = 0.95, relwidth = 1, relheight = 0.6, anchor="se")
        self.bode_main_frame.grid_rowconfigure(0, weight=1)
        self.bode_main_frame.grid_columnconfigure(0, weight=1)

        bode_heading = [
            {"text": "Câu hỏi", "stretch": True},
            {"text": "Mã môn học", "stretch": True},
            {"text": "Trình độ", "stretch": True},
            {"text": "Nội dung", "stretch": True},
            {"text": "A", "stretch": True},
            {"text": "B", "stretch": True},
            {"text": "C", "stretch": True},
            {"text": "D", "stretch": True},
            {"text": "Đáp án", "stretch": True},
            {"text": "Mã giáo viên", "stretch": True},
        ]

        bode_row = []
        for row in bode_data:
            bode_row.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

        self.bode_table = Tableview(
            master=self.bode_main_frame,
            coldata=bode_heading,
            rowdata=bode_row,
            paginated=True,
            searchable=True,
            pagesize=15,
        )
        self.bode_table.grid(row=0, column=0, sticky="nsew")
        
        # Close window
        self.window.mainloop()


class GiangVienView:
    def __init__(self, info: list, bode_data: list):
        self.info = info

        self.window = CTk()
        self.window.geometry(f"{WIDTH}x{HEIGHT}")
        self.window.title("Thi trắc nghiệm")
        self.window.configure(fg_color="#ababab")

        self.infor_bar = CTkFrame(self.window, height=50, fg_color="#ababab")
        self.infor_bar.pack(fill="x")

        str_infor = f"Mã: {self.info[0][0]}   Tên: {self.info[0][1].title()}   Lớp: {self.info[0][2]}"

        self.infor_label = CTkLabel(self.infor_bar, text=f"{str_infor}", font=("arial", 16), text_color="white")
        self.infor_label.place(relx=0.6, rely=0.19)

        self.header_tab = CTkTabview(self.window, anchor="nw", corner_radius=0,
                              fg_color="#dff5ff", segmented_button_selected_color	="white",
                              text_color="black", segmented_button_fg_color="#a3a3a3",
                              segmented_button_selected_hover_color="#d9d9d9")
        self.header_tab.place(relx=0.0, rely=0.05, relheight=1, relwidth=1)
        self.header_tab.add("Bộ đề")

        # Phần Bộ đề
        self.bode_main_frame = CTkFrame(self.header_tab.tab("Bộ đề"), fg_color="white", width=HEIGHT, height=HEIGHT/5*3)
        self.bode_main_frame.place(relx = 1, rely = 0.95, relwidth = 1, relheight = 0.6, anchor="se")
        self.bode_main_frame.grid_rowconfigure(0, weight=1)
        self.bode_main_frame.grid_columnconfigure(0, weight=1)

        bode_heading = [
            {"text": "Câu hỏi", "stretch": True},
            {"text": "Mã môn học", "stretch": True},
            {"text": "Trình độ", "stretch": True},
            {"text": "Nội dung", "stretch": True},
            {"text": "A", "stretch": True},
            {"text": "B", "stretch": True},
            {"text": "C", "stretch": True},
            {"text": "D", "stretch": True},
            {"text": "Đáp án", "stretch": True},
            {"text": "Mã giáo viên", "stretch": True},
        ]

        bode_row = []
        for row in bode_data:
            bode_row.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

        self.bode_table = Tableview(
            master=self.bode_main_frame,
            coldata=bode_heading,
            rowdata=bode_row,
            paginated=True,
            searchable=True,
            pagesize=15,
        )
        self.bode_table.grid(row=0, column=0, sticky="nsew")


        # Close window
        self.window.mainloop()


class SinhVienView:
    def __init__(self, info: list, baithi_data: list, chitiet_data: list):
        self.info = info

        self.window = CTk()
        self.window.geometry(f"{WIDTH}x{HEIGHT}")
        self.window.title("Thi trắc nghiệm")
        self.window.configure(fg_color="#ababab")

        self.infor_bar = CTkFrame(self.window, height=50, fg_color="#ababab")
        self.infor_bar.pack(fill="x")

        str_infor = f"Mã: {self.info[0][0]}   Tên: {self.info[0][1].title()}   Lớp: {self.info[0][2]}"

        self.infor_label = CTkLabel(self.infor_bar, text=f"{str_infor}", font=("arial", 16), text_color="white")
        self.infor_label.place(relx=0.6, rely=0.19)

        self.header_tab = CTkTabview(self.window, anchor="nw", corner_radius=0,
                              fg_color="#dff5ff", segmented_button_selected_color	="white",
                              text_color="black", segmented_button_fg_color="#a3a3a3",
                              segmented_button_selected_hover_color="#d9d9d9")
        self.header_tab.place(relx=0.0, rely=0.05, relheight=1, relwidth=1)
        self.header_tab.add(" Bài thi ")
        self.header_tab.add(" Thi ")

        # Phần Bài thi
        self.baithi_main_frame = CTkFrame(self.header_tab.tab(" Bài thi "), fg_color="white", width=HEIGHT, height=HEIGHT/5*3)
        self.baithi_main_frame.place(relx = 1, rely = 0.95, relwidth = 1, relheight = 0.6, anchor="se")
        self.baithi_main_frame.grid_rowconfigure(0, weight=1)
        self.baithi_main_frame.grid_columnconfigure(0, weight=1)

        baithi_heading = [
            {"text": "Mã bài thi", "stretch": True},
            {"text": "Mã sinh viên", "stretch": True},
            {"text": "Mã môn học", "stretch": True},
            {"text": "Lần thi", "stretch": True},
            {"text": "Ngày thi", "stretch": True},
            {"text": "Điểm", "stretch": True},
        ]

        baithi_row = []
        for row in baithi_data:
            baithi_row.append((row[0], row[1], row[2], row[3], row[4], row[5]))

        self.baithi_table = Tableview(
            master=self.baithi_main_frame,
            coldata=baithi_heading,
            rowdata=baithi_row,
            paginated=True,
            searchable=True,
            pagesize=15,
        )
        self.baithi_table.grid(row=0, column=0, sticky="nsew")

        # Close window
        self.window.mainloop()