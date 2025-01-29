import pathlib

def get_cats_info(fileCats):
    path = pathlib.Path(fileCats)
    ListCats=[] 
    try:
        with path.open("r", encoding='utf-8') as fh:
            for line in fh:      
                cats={
                    'id' : line.split(',')[0],
                    'name' : line.split(',')[1],
                    'age' : line.strip().split(',')[2]}
                ListCats.append(cats)
            return ListCats            
    except:
      print('Не вдалося знайти файл') 
      return[]  

result=get_cats_info("Cats.txt")
print(result)