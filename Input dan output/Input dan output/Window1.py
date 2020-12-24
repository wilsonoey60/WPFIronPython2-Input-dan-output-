import wpf

from System.Windows import Application, Window

class Window1(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Window1.xaml')
        
    def button1_Click(self, sender, e):
        a = self.inputan.Text
        self.cetak.Content = a
        pass
        
if __name__ == '__main__':
    Application().Run(MyWindow())