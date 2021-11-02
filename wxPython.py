import wx


class MyFrame(wx.Frame):
    def __init__(self, title="My Frame", size=(500, 500)):
        super().__init__(parent=None, title=title, size=size)
        # create panel of frame
        panel = wx.Panel(parent=self)
        # create sizer
        sizer = wx.BoxSizer(wx.VERTICAL)

        # create text input
        self.text_ctrl = wx.TextCtrl(panel)
        #add to sizer
        sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        # create btn
        myBtn = wx.Button(panel, label="Press me")
        # add event
        myBtn.Bind(wx.EVT_BUTTON, self.on_click)
        # add btn to sizer
        sizer.Add(myBtn, 0, wx.ALL | wx.CENTER, 5)

        #add sizer to panel
        panel.SetSizer(sizer)

        #display frame
        self.Show()

    #on_click handler
    def on_click(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You did'nenter anything!")
        else:
            print(f'You typed: "{value}"')


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame("Hello world")
    app.MainLoop()
