import os

def search(dirname):
    try:
        print("검색하려는 폴더:",dirname)
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname,filename)

            ext =os.path.splitext(full_filename)[-1]
            if ext == ".txt":
                print(full_filename)
    except PermissionError:
        print("해당 폴더는 접근 할 수 없음")
    except Exception as e:
        print(e)
            
        

search('c:\\test_a')
