from collections import deque
from csp import *
from copy import deepcopy


class Vanilla:
  def __init__(self, soduko):
    self.soduko = soduko
    self.steps = 0

    self.neighbors = {}

    self.constraints = []

    #ROWS
    self.row_A = {'A1': [], 'A2': [], 'A3': [], 'A4': [], 'A5': [], 'A6': [], 'A7': [], 'A8': [], 'A9': []}
    self.row_B = {'B1': [], 'B2': [], 'B3': [], 'B4': [], 'B5': [], 'B6': [], 'B7': [], 'B8': [], 'B9': []}
    self.row_C = {'C1': [], 'C2': [], 'C3': [], 'C4': [], 'C5': [], 'C6': [], 'C7': [], 'C8': [], 'C9': []}
    self.row_D = {'D1': [], 'D2': [], 'D3': [], 'D4': [], 'D5': [], 'D6': [], 'D7': [], 'D8': [], 'D9': []}
    self.row_E = {'E1': [], 'E2': [], 'E3': [], 'E4': [], 'E5': [], 'E6': [], 'E7': [], 'E8': [], 'E9': []}
    self.row_F = {'F1': [], 'F2': [], 'F3': [], 'F4': [], 'F5': [], 'F6': [], 'F7': [], 'F8': [], 'F9': []}
    self.row_G = {'G1': [], 'G2': [], 'G3': [], 'G4': [], 'G5': [], 'G6': [], 'G7': [], 'G8': [], 'G9': []}
    self.row_H = {'H1': [], 'H2': [], 'H3': [], 'H4': [], 'H5': [], 'H6': [], 'H7': [], 'H8': [], 'H9': []}
    self.row_I = {'I1': [], 'I2': [], 'I3': [], 'I4': [], 'I5': [], 'I6': [], 'I7': [], 'I8': [], 'I9': []}

    #COLUMNS
    self.col_1 = {'A1': [], 'B1': [], 'C1': [], 'D1': [], 'E1': [], 'F1': [], 'G1': [], 'H1': [], 'I1': []}
    self.col_2 = {'A2': [], 'B2': [], 'C2': [], 'D2': [], 'E2': [], 'F2': [], 'G2': [], 'H2': [], 'I2': []}
    self.col_3 = {'A3': [], 'B3': [], 'C3': [], 'D3': [], 'E3': [], 'F3': [], 'G3': [], 'H3': [], 'I3': []}
    self.col_4 = {'A4': [], 'B4': [], 'C4': [], 'D4': [], 'E4': [], 'F4': [], 'G4': [], 'H4': [], 'I4': []}
    self.col_5 = {'A5': [], 'B5': [], 'C5': [], 'D5': [], 'E5': [], 'F5': [], 'G5': [], 'H5': [], 'I5': []}
    self.col_6 = {'A6': [], 'B6': [], 'C6': [], 'D6': [], 'E6': [], 'F6': [], 'G6': [], 'H6': [], 'I6': []}
    self.col_7 = {'A7': [], 'B7': [], 'C7': [], 'D7': [], 'E7': [], 'F7': [], 'G7': [], 'H7': [], 'I7': []}
    self.col_8 = {'A8': [], 'B8': [], 'C8': [], 'D8': [], 'E8': [], 'F8': [], 'G8': [], 'H8': [], 'I8': []}
    self.col_9 = {'A9': [], 'B9': [], 'C9': [], 'D9': [], 'E9': [], 'F9': [], 'G9': [], 'H9': [], 'I9': []}

    #BOXES
    self.box_1 = {'A1': [], 'A2': [], 'A3': [], 'B1': [], 'B2': [], 'B3': [], 'C1': [], 'C2': [], 'C3': []}
    self.box_2 = {'A4': [], 'A5': [], 'A6': [], 'B4': [], 'B5': [], 'B6': [], 'C4': [], 'C5': [], 'C6': []}
    self.box_3 = {'A7': [], 'A8': [], 'A9': [], 'B7': [], 'B8': [], 'B9': [], 'C7': [], 'C8': [], 'C9': []}
    self.box_4 = {'D1': [], 'D2': [], 'D3': [], 'E1': [], 'E2': [], 'E3': [], 'F1': [], 'F2': [], 'F3': []}
    self.box_5 = {'D4': [], 'D5': [], 'D6': [], 'E4': [], 'E5': [], 'E6': [], 'F4': [], 'F5': [], 'F6': []}
    self.box_6 = {'D7': [], 'D8': [], 'D9': [], 'E7': [], 'E8': [], 'E9': [], 'F7': [], 'F8': [], 'F9': []}
    self.box_7 = {'G1': [], 'G2': [], 'G3': [], 'H1': [], 'H2': [], 'H3': [], 'I1': [], 'I2': [], 'I3': []}
    self.box_8 = {'G4': [], 'G5': [], 'G6': [], 'H4': [], 'H5': [], 'H6': [], 'I4': [], 'I5': [], 'I6': []}
    self.box_9 = {'G7': [], 'G8': [], 'G9': [], 'H7': [], 'H8': [], 'H9': [], 'I7': [], 'I8': [], 'I9': []}

    self.container = [self.row_A, self.row_B, self.row_C, self.row_D, self.row_E, self.row_F, self.row_G, self.row_H, self.row_I, self.col_1, self.col_2, self.col_3, self.col_4, self.col_5, self.col_6, self.col_7, self.col_8, self.col_9, self.box_1, self.box_2, self.box_3, self.box_4, self.box_5, self.box_6, self.box_7, self.box_8, self.box_9]

  def initialize_compartments(self):

    for i in self.soduko:

      for j in self.container:
        if i in j:
          j[i] = self.soduko[i]

  
  def establish_neighbors_constraints(self):

    # establish each cell and have empty lists for it initially
    for i in self.container:
      for j in i:
        if j not in self.neighbors:
          self.neighbors[j] = []

    # add the neighbors for every cell
    for cell in self.neighbors:
      for compartment in self.container:
        if cell in compartment:
          for other_cell in compartment:
            if other_cell != cell:
              if other_cell not in self.neighbors[cell]:
                self.neighbors[cell].append(other_cell)

    
    
    for cell in self.neighbors:

      for other_cell in self.neighbors[cell]:
        t = (cell, other_cell)
        self.constraints.append(t)

  
  def AC3(self):

    q = deque()

    for reltionship in self.constraints:

      q.append(reltionship)

    
    while q:

      (Xi, Xj) = q.popleft()


      if self.revise(Xi, Xj):
        
        if len(self.soduko[Xi]) == 0:

          return False


        
        for Xk in self.neighbors[Xi]:
          if Xk != Xj:
            q.append((Xk,Xi))
      

    

    return True


  def revise(self, Xi , Xj):

    r = False

    for value in self.soduko[Xi]:




      if not self.consistent(value, Xi, Xj):



        arr = self.soduko[Xi]

        arr_updated = [v for v in arr if v != value]

        self.soduko[Xi] = []
        self.soduko[Xi] = arr_updated

   


        # self.soduko[Xi] = self.soduko[Xi].remove(value)
        r = True
    
    return r

  def consistent(self, value, Xi, Xj):



    for other_value in self.soduko[Xj]:


      if Xj in self.neighbors[Xi] and other_value!=value:
        return True
    
    return False

  # checking if a value can be assigned to a variable
  def ok(self,var, value, assignement):
    for neighbor in self.neighbors[var]:
      if neighbor in assignement and assignement[neighbor] == value:
        return False
    
    return True


  
  def backtrack_search(self):
    return self.backtrack({})

  def backtrack_search_FC(self):
    return self.backtrack_forward_check({})

  

  
  def backtrack(self,assignement):


    if self.complete(assignement):
      return assignement
    
    var = self.select_variable_order(assignement = assignement)
    domain = deepcopy(self.soduko)

    for val in self.soduko[var]:
      if self.ok(var, val, assignement=assignement):
        self.steps+=1
        assignement[var] = val





        result = self.backtrack(assignement)
        if result != "FAILURE":
          return result

        del assignement[var]
        self.soduko.update(domain)
    
    return "FAILURE"



  def backtrack_forward_check(self,assignement):


    if self.complete(assignement):
      return assignement
    
    var = self.select_variable_order(assignement = assignement)
    domain = deepcopy(self.soduko)

    for val in self.soduko[var]:
      if self.ok(var, val, assignement=assignement):
        assignement[var] = val

        inferences = {}
        inferences = self.infer(assignement, inferences, var, val)
        if inferences!="FAILURE":
          result = self.backtrack(assignement)
          if result != "FAILURE":
            return result
        
        del assignement[var]
        self.soduko.update(domain)
    
    return "FAILURE"


  def infer(self, assignement, inferences, var, val):

    inferences[var] = val

    for n in self.neighbors[var]:
      if n not in assignement and val in self.soduko[n]:
        if len(self.soduko[n]) == 1:
          return "FAILURE"

        arr = self.soduko[n]
        arr_updated = [v for v in arr if v != val]
        self.soduko[n] = []
        self.soduko[n] = arr_updated

        if len(arr_updated) == 1:
          flag = self.infer(assignement, inferences, n, arr_updated[0])
          if flag == "FAILURE":
            return "FAILURE"
    return inferences



  def complete(self, assignement):
    if set(assignement.keys()) == set(self.soduko.keys()):
      return True
    return False


  # uses MRV
  def select_variable_order(self, assignement):

    unassigned_vars = {}

    for i in self.soduko:
      if i not in assignement:
        unassigned_vars[i] = self.soduko[i]

    mrv = min(unassigned_vars, key=unassigned_vars.get)
    return mrv


   

  




  










    


    
 











    

    


    



  
  # def AC3(self):
    

  #   for compartment in self.container:

  #     for cell in compartment:


  #       if len(compartment[cell]) ==1:
  #         print("This is the number to be removed")
          
  #         number = compartment[cell][0]
  #         print(number)
  #         for cell2 in compartment:
  #           if cell2 != cell:
              
  #             if number in compartment[cell2]:
  #               print("remove from:")
  #               print(cell2)
  #               compartment[cell2].remove(number)
  #               print("after removing")
  #               print(compartment[cell2])
    

            

            

    
    
            





    
    

      
      
      
      
    