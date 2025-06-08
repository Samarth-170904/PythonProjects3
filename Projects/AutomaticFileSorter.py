import os,shutil
path = r"D:/Certificates"
file_name = os.listdir(path)

folder_names = ['pdf files','image files']
for item in range(0,2):
    if not os.path.exists(path+'/'+folder_names[item]):
        os.makedirs(path+'/'+folder_names[item])
        
for file in file_name:
    if '.pdf' in file and not os.path.exists(path+'/'+folder_names[0]+'/'+file):
        shutil.move(path+'/'+file,path+'/'+folder_names[0]+'/'+file)
    elif '.png' in file and not os.path.exists(path+'/'+folder_names[1]+'/'+file):
        shutil.move(path+'/'+file,path+'/'+folder_names[1]+'/'+file)
