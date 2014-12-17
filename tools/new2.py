#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import wx

class MyApp(wx.App):

    pass

class FileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
          wx.FileDropTarget.__init__(self)
          self.window = window

    def OnDropFiles(self,  x,  y, fileNames):
          self.window.SetValue(str(fileNames))

class MyFrame(wx.Frame):

    def __init__(self, parent, id):

        wx.Frame.__init__(self, parent, id, title = u'音乐流派检索-你是我的小呀小苹果', size = (778,494))
        panel=wx.Panel(self)
        
        
        
        wx.StaticText(panel, -1, u'请将待检索的文件拖拽到此', (50, 24))
                
        textBox=wx.TextCtrl(panel, pos = (50, 50),size =(350, 100))
        dropTarget = FileDropTarget(textBox)
        textBox.SetDropTarget( dropTarget )
        
        self.button = wx.Button(panel, -1, "Hello", pos=(450, 100)) 
        self.button.SetDefault() 
        self.button.SetLabel(u"搜索") 
        
        wx.StaticText(panel, -1, u'啊，原来你喜欢XX的音乐', (50, 170))
        wx.StaticText(panel, -1, u'与它相接近的歌还有X   X   X   X ......', (50, 200))

if __name__=='__main__':
    app=MyApp()
    frame=MyFrame(parent=None,id=-1)
    frame.Show(True)
    app.MainLoop()