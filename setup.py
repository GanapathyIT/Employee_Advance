from cx_Freeze import setup, Executable

exe = Executable(script = 'menu.py',
                 base = "Win32GUI",
                 targetName='Advance'
                 )

setup(name = "Advance" , 
	version = "0.1" , 
	description = "VSA" ,
	executables = [exe]) 
