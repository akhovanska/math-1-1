#getting number for each iterated line
def num_liner(fun):
    def _num(n):
        print(n + 1)
        fun(n)

    return _num

#reading from the file
@num_liner
def text_printer(n):
    with open("1716.txt", "r", encoding="utf-8") as file: #1716 create any text file
        k = file.readlines()
        line = k[n]
        print(line)

#reading by line from the file that we opened before
def file_reader_by_line(filename):
    with open(filename, "r", encoding="utf-8") as f:
        num = len(f.readlines())
        for i in range(num):
            text_printer(i)


file_reader_by_line("1716.txt") #1716 create any text file
