import toolbox
from toolbox import report

message = toolbox.functions.weirdCase("The toolbox package is ready for use")
report(message)

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for chunk in toolbox.functions.listChunker(lst=list_of_numbers, csize=3):
    print(chunk)
