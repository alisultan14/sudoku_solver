from FileReader import *
from Vanilla import *
from Triple import *
from csp import *
from Killer import *
import yaml
import os
import sys
import random
import logging
import time

logging.basicConfig(filename="Output.txt",  
					filemode='w')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG) 

def load_config(filename):

    import os
    with open(os.path.join(sys.path[0], filename), "r") as f:   
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data

def main():

  cfg = load_config("config.yaml")
  soduko = cfg["SODUKO"]
  version = int(cfg["VERSION"]) - 1
  bc_tk = cfg["FORWARD_CHECKING"]
  ac3 = cfg["AC_3"]

  st = time.time()
  
  if soduko == "Vanilla":
     s = Vanilla(readVanilla()[version])
     
     s.initialize_compartments()
     s.establish_neighbors_constraints()
     if ac3:
        s.AC3()
        print(s.soduko)
     if (bc_tk):
      logger.debug(s.backtrack_search_FC())
     else:
      logger.debug(s.backtrack_search())
     et = round((time.time() - st),2)
     logger.debug("Time taken in seconds to solve this soduko:")
     logger.debug(et)
     logger.debug("Number of steps taken to solve the puzzle:")
     logger.debug(s.steps)
     print(et)
     print(s.steps)


     
    

  
  if soduko == "Triple":
     s = Triple(readTriple()[version])
     s.initialize_compartments()
     s.establish_neighbors_constraints()
     if ac3:
         s.AC3()
     if (bc_tk):
      logger.debug(s.backtrack_search_FC())
     else:
      logger.debug(s.backtrack_search())
     et = round((time.time() - st),2)
     logger.debug("Time taken in seconds to solve this soduko:")
     logger.debug(et)
     logger.debug("Number of steps taken to solve the puzzle:")
     logger.debug(s.steps)
     print(et)
     print(s.steps)

  
  if soduko == "Killer":
     s = Killer(readKiller()[version])
     s.initialize_compartments()
     s.establish_neighbors_constraints()
     if ac3:
         s.AC3()
     if (bc_tk):
      logger.debug(s.backtrack_search_FC())
     else:
      logger.debug(s.backtrack_search())
     et = round((time.time() - st),2)
     logger.debug("Time taken in seconds to solve this soduko:")
     logger.debug(et)
     logger.debug("Number of steps taken to solve the puzzle:")
     logger.debug(s.steps)
     print(et)
     print(s.steps)

  

  
  
  






     






  





if __name__ == "__main__":
    main()
