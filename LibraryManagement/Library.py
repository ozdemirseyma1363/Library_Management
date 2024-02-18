class Library:
  def menu(self):
      print("\n**MENU**")
      print('1-List Books \n2-Add Book \n3-Delete Book \n')
      process = input("Select the action :")
      Library.lst(self, process)
  def  lst(self, lib):
    if lib == '1':
        Library.lstBook(self)
    elif lib == '2':
        Library.addBook(self)
    elif lib == '3':
        Library.removeBook(self)
    else:
        Library.menu(self)
  def open(self):
      name = input("User Name :")
      password = input("Password :")
      uName = "seyma"
      uPassword = "seyma"
      if password == uPassword and name == uName:
          while True:
              Library.menu(self)

      elif name == uName and password != uPassword:
          print("Incorrect password")
          Library.open(self)
      elif name != uName:
          print("User didn't find")
          Library.open(self)
  def lstBook(self):
      from prettytable import PrettyTable
      directory = open("kitaplar.txt", "r",encoding="utf-8")
      bName, bAuthor, bYear, bNumber = [], [], [], []
      files = list(directory.readlines())
      for file in files:
          data = file.split(',')
          bName.append(data[0].replace("'", '').replace('[', ''))
          bAuthor.append(data[1].replace("'", '').replace('[', ''))
          bYear.append(data[2].replace("'", ''))
          bNumber.append(data[3].replace("'", '').replace(']', ''))
      report = PrettyTable()
      column_names = ['Book Title', 'Author', 'Year', 'Number of Pages']
      report.add_column(column_names[0], bName)
      report.add_column(column_names[1], bAuthor)
      report.add_column(column_names[2], bYear)
      report.add_column(column_names[3], bNumber)
      print(report)

  def removeBook(self):
      def DeleteLine(index):
          try:
              with open("kitaplar.txt", "r", encoding="utf-8") as file:
                  lines = file.readlines()
                  del lines[index]
              with open("kitaplar.txt", "w", encoding="utf-8") as file:
                  for line in lines:
                      file.write(line)
          except Exception as e:
              print(e)

      name = input("Please enter the title of the book you want to delete : ")
      directory = open("kitaplar.txt", "r", encoding="utf-8")
      count = []
      sk = 0
      files = list(directory.readlines())
      for file in files:
          data = file.split(',')
          if data[0].replace("'", "").replace("[", "") == name:
              count.append((sk))
          sk = sk + 1
      for i in count:
          DeleteLine(i)
          print(name + " has been deleted.")
  def addBook(self):
      folder = open("kitaplar.txt", "a",encoding="utf-8")
      title = input("Book Title: ")
      author = input("Book Author :")
      firstYear = input("First Release Year :")
      page = input("Number of pages :")
      information = title + "\n" + author + "\n" + firstYear + "\n" + page
      folder.write(str((information).splitlines()) + "\n")
      folder.close()
      print("Save Successful.")
Library.open(self=Library)


