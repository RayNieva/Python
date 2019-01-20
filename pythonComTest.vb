Sub PythonTest()
  'Dim response As String
  
  Set PythonUtils = CreateObject("PythonServer.Utilities")
  response = PythonUtils.SplitString("Hello From VB")
  
  
  MsgBox response
  'For Each Item In response
   ' MsgBox Item
  'Next
End Sub
