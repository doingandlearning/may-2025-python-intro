file = open("01-course-intro.pptx", "rb")

contents = file.read()

print(str(contents).find("Introduction"))



file.close()