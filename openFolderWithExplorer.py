import subprocess
##Opens folder in which file path is in
file = "G:\DataAlgo\Textbook.pdf"
subprocess.Popen(r'explorer /select,{}'.format(file)) 