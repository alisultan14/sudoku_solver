from pathlib import Path


# returns the soduko with their domains
def readVanilla():
    p = Path(__file__).with_name('Vanilla_Soduko.txt')
    vanilla_sodukos = []
    original_domain = ['1','2','3','4','5','6','7','8','9']
    with p.open('r') as f:
      x = f.readlines()
      for i in range(0, len(x), 82):
        soduko = {}
        for j in range(i, i+81):
          key = x[j][0:2]
          value = x[j][5:6]
          if value == '0':
            soduko[key] = original_domain
          else:
            soduko[key] = [value]

          
        
        
        vanilla_sodukos.append(soduko)

    return vanilla_sodukos


  # returns the soduko with their domains
def readTriple():
    p = Path(__file__).with_name('Triple_Soduko.txt')
    vanilla_sodukos = []
    original_domain = ['1','2','3','4','5','6','7','8','9']
    with p.open('r') as f:
      x = f.readlines()
      for i in range(0, len(x), 172):
        soduko = {}
        for j in range(i, i+171):

          parts = x[j].split(" ")
  
          key = parts[0]
 
          value = parts[2][0]

       

          print(key)
          print(value)


          if value == '0':
            soduko[key] = original_domain
          else:
            soduko[key] = [value[0]]
        vanilla_sodukos.append(soduko) 
      
    
       
      print(vanilla_sodukos)
        
    

    return vanilla_sodukos

  # returns the soduko with their domains
def readKiller():
    p = Path(__file__).with_name('Killer_Soduko.txt')
    vanilla_sodukos = []
    original_domain = ['1','2','3','4','5','6','7','8','9']
    with p.open('r') as f:
      x = f.readlines()
      soduko = {}
      for i in x:
        print(i)

        if len(i)<5:
          print("Here")
          vanilla_sodukos.append(soduko)
          soduko = {}
        elif len(i) > 7:
          parts = i.split(" ")
          print(parts)
          key = parts[0]
          soduko[key] = []
          boxes = parts[2].split(",")
          for b in boxes:
            soduko[key].append(b)
          
          soduko[key].append(parts[5][:-1])
        else:
          key = i[0:2]
          value = i[5:6]
          if value == '0':
            soduko[key] = original_domain
          else:
            soduko[key] = [value]
        vanilla_sodukos.append(soduko)
    


    return vanilla_sodukos








      
      
      
      
    