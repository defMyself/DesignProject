import easyocr
reader = easyocr.Reader()
result = reader.readtext('test01.gif')