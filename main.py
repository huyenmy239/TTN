from controllers import *
from views import CoSoView

if __name__ == "__main__":
    # controller = LoginController()
    controller = CoSoController([["TH123", "PHAN VAN HAI", "Coso"]], ["MIE\MSSQLSERVER01", "TTN", "pvh", "239003"])
    # controller.view.window.mainloop()
    # CoSoView([["TH101", "Tran Phan Hai", "Co so"]]).window.mainloop()
    # c = LoginController()
    # c.test()