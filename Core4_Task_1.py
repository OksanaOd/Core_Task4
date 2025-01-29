import pathlib

def total_salary(fileSal):
    try:
        path = pathlib.Path(fileSal)
        emp=0
        total=0
        Salaries=[]
        with path.open("r", encoding='utf-8') as fh:
            for line in fh: #lines:
                line = line.strip()                                     
                total+=float(line.split(',')[1]) 
                emp+=1     
        if emp != 0:  
            Salaries.append(total)
            Salaries.append(total/emp) #average            
        else:
            return []
        return Salaries              
    except:
        print('Не вдалося знайти файл')
        return []   
  
result=total_salary("salary_file.txt")
try:
    print(f"Загальна сума заробітної плати: {result[0]}, Середня заробітна плата: {result[1]}") 
except IndexError:
   print("у списку відсутні дані по співробітникам!") 