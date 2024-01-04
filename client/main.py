import wx
import requests

USER: dict | None = None 

class LoginPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        self.username_label = wx.StaticText(self, label="Username:")
        self.username_text = wx.TextCtrl(self)
        
        self.password_label = wx.StaticText(self, label="Password:")
        self.password_text = wx.TextCtrl(self, style=wx.TE_PASSWORD)
        
        self.login_button = wx.Button(self, label="Login")
        self.login_button.Bind(wx.EVT_BUTTON, self.on_login)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.username_label, 0, wx.ALL, 5)
        sizer.Add(self.username_text, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.password_label, 0, wx.ALL, 5)
        sizer.Add(self.password_text, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.login_button, 0, wx.ALL | wx.CENTER, 5)
        
        self.SetSizer(sizer)

    def on_login(self, event):
        username = self.username_text.GetValue()
        password = self.password_text.GetValue()

        # Replace this with your actual authentication logic
        authenticated, error = self.authenticate(username, password)

        if authenticated:
            self.GetParent().show_secret_panel()
        else:
            wx.MessageBox("Authentication failed. Please try again. error msg: "+str(error), "Error", wx.OK | wx.ICON_ERROR)

    def authenticate(self, username, password):
        global USER
        # Dummy authentication logic (replace with actual API call)
        # In a real-world scenario, you would make an API call to authenticate the user
        # and handle the response accordingly.
        req = requests.post("http://192.168.2.7:5000/login", json={"username": username, "password": password})
        if req.ok: 
            jsons = req.json()
            if jsons['error']: return (False, req.content )
            USER = jsons['user']
            return (True, True)

        return (False, False)
        # return True if username == "user" and password == "pass" else False


class SecretPanel(wx.Panel):
    def __init__(self, parent):
        global USER
        wx.Panel.__init__(self, parent)
        
        # if not USER:
        #     self.Hide()
        #     return; 
        
        self.secret_text = wx.StaticText(self, label="Secret information: ")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.secret_text, 0, wx.ALL, 20)
        self.SetSizer(sizer)

    def afterLogin(self):
        self.secret_text.SetLabel("Secret information: "+ requests.get("http://192.168.2.7:5000/protected", headers={
            "Authorization": USER.get('jwt')
        }).json()['secret'])


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        wx.Frame.__init__(self, *args, **kwds)

        self.login_panel = LoginPanel(self)
        self.secret_panel = SecretPanel(self)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.login_panel, 1, wx.EXPAND)
        self.sizer.Add(self.secret_panel, 1, wx.EXPAND)

        self.secret_panel.Hide()

        self.SetSizer(self.sizer)

    def show_secret_panel(self):
        self.login_panel.Hide()
        self.secret_panel.Show()
        self.Layout()
        self.secret_panel.afterLogin()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, title="Authentication App", size=(400, 300))
    frame.Show()
    app.MainLoop()