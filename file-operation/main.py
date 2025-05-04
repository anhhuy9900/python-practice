
class FileOperation:
    myFile = None

    def __init__(self):
        # Files - opening and reading a file in the same directory/folder
        self.myFile = open("./routers.txt", "r")  # "r" is the file access mode for reading and it is the default mode when opening a file

    def example(self):
        # Files - opening and reading a file in another directory/folder on Windows
        self.myFile = open("./routers.txt", "r")  #"r" is the file access mode for reading and it is the default mode when opening a file
        print("mode : ", self.myFile.mode)  # checking the mode in which a file has been opened
        print("read : ", self.myFile.read())  # method that returns the entire content of a file in the form of a string
        print("returning only the first 5 characters : ", self.myFile.read(5))  # returning only the first 5 characters (bytes) in the file
        print("seek : ", self.myFile.seek(0))  # moving the cursor at the beginning of the file
        print("tell : ", self.myFile.tell())  # checking the current position of the cursor inside the file
        print("readline : ", self.myFile.readline())  # returns the file content one line a ta time, each time you use the method
        print("readlines : ", self.myFile.readlines())  # returns a list where each element is a line in the file

    @staticmethod
    def create_new_file(self, filename='test.txt'):
        # opens/creates a new file for writing; the "w" method also creates the file for writing if the file doesn’t exist
        # and overrides the file if the file already exists; remember to close the file after writing to it to save the changes!
        newFile = open(filename, "w")
        # this method takes a sequence of strings as an argument and writes those strings to the file
        newFile.writelines(["Cisco", "Juniper", "HP", "\n"])

    @staticmethod
    def open_file(filename='newfile.txt'):
        newfile = open(filename, "a")  # opening a file for appending
        return newfile

    @staticmethod
    def write_file(filename='newfile.txt'):
        newfile = open(filename, "a")  # opening a file
        newfile.write('This is new line \n')
        newfile.writelines(['Line 1 \n', 'Line 2 \n', 'Line 3 \n'])
        newfile.close()  # closing a file

    @staticmethod
    def read_file(filename='newfile.txt'):
        newfile = open(filename, "r")  # opening a file
        print(newfile.read())

    @staticmethod
    def read_lines_file(filename='newfile.txt'):
        newfile = open(filename, "r")  # opening a file
        print(newfile.readlines())

    @staticmethod
    def close_file(newfile):
        # Files - closing a file
        newfile.close()  # closing a file
        print(newfile.closed)  # checking if a file is closed


file = FileOperation()
# file.example()
# file.create_new_file()
# newFile = file.open_file()
# file.close_file(newFile)
# file.write_file()
# file.read_file()
file.read_lines_file()