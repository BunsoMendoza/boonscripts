  
# Python program to rename all file 
# names in your directory  
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path) 
print(os.getcwd()) 
desired_file_name_length = 15



for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)

    if len(f_name) > desired_file_name_length:       
        f_name =  f_name[0:desired_file_name_length]  
         
        new_name = '{}{}'.format(f_name, f_ext) 
        os.rename(f, new_name) 
      
    