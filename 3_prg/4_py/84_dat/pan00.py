import pandas 

print("beg")
sFN='./7_ifc/py/x_dat/src00.xlsx'
oSrc=pandas.read_excel(sFN,'Cfg')
print('shape',oSrc.shape)
print('end')
