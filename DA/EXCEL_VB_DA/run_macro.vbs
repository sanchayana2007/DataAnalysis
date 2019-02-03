Function RenameSheet(sheetname, fullfilename)
	Dim sht
	Dim xlApp 
	Dim xlBook 
	Dim filename 
	filename = sheetname
	Set xlApp = CreateObject("Excel.Application")
	Set xlBook = xlApp.Workbooks.Open(fullfilename,0,True)
	Set sht = xlBook.Worksheets(filename)
	sht.name = "AgregateName"
	xlApp.Application.Visible= true
	path = xlBook.Path
	xlBook.SaveAs Path & "\" & sheetname ,51
	xlApp.Quit 
	Set Filename = Nothing 
	Set xlBook = Nothing 
	Set xlApp = Nothing 

End Function 

Function Runmacro(Outfile,Sheetname,macroname,wdArg):
	Dim sht
	Dim xlApp 
	Dim xlBook 
	Set xlApp = CreateObject("Excel.Application")
	Set xlBook = xlApp.Workboooks.Open(Sheetname,0,False)
	xlApp.Application.Visible = True
	if wdArg= None then
		xlApp.Run macroname
	else
		xlApp.Run macroname , wdarg
	end if 
	xlApp.Activeworkbook.Close SaveChanges = True

	xlApp.Quit
	Set xlBook = Nothing 
	Set xlApp = Nothing
	WScript.Echo "Finished"
	

End Function 

Function UserInput(myPrompt):
	Set objShell = CreateObject("WScript.Shell")
	Set objScriptExec = objShell.Exec("python excelmappint.py")
	strIPConfig = objScriptExec.StdOut.ReadAll
	WScript.Echo strIpConfig 


End Function 


dim fso: set fso = CreateObject("Scripting.FileSystemObject")
filename = fso.GetAbsolutePathName(".") & "\"

dim Currdir
Currdir = fso.GetAbsolutePathName(".")
strinput = UserInput("Make sure Excel Personal")


filename  = fso.GetAbsolutePathName(".") & "\"
renamesheet = "lastweekfailed", filename & "lastweekfailed.csv"
renamesheet = "thisweekfailed", filename & "thisweekfailed.csv"

Runmacro "Pivot",filename & "\lastweekfailed.xlsx", "'C:\Users\sanchez\AppdataRoaming\Microsoft\Excel\XLSTART\PERSONAL.XLSB'!Create_Pivot_New",None
Runmacro "Pivot",filename & "\lastweekfailed.xlsx", "'C:\Users\sanchez\AppdataRoaming\Microsoft\Excel\XLSTART\PERSONAL.XLSB'!Analyse_Pivot_New",Currdir

