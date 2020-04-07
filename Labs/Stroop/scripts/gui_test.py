from psychopy import gui

files = gui.fileOpenDlg(tryFilePath=".", allowed='*.csv')
if not files:#user pressed cancel
    core.quit()
    
print(files)