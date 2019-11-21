from MainProgram import some_main
from MainProgram.SubProgram import submain

print('Calling the from the other Module')
some_main.main_report()
submain.sub_report()