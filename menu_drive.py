import os

while True:
	print("chat with me with your requirements : "  , end='')
	p = input()
    
      if(("run" in p) or ("execute" in p) or ("open" in p) or ("go to" in p))  and ("chrome" in p):
        os.system("chrome")
      
      elif (("run" in p) or  ("execute" in p ) or ("open" in p) or ("go to" in p)) and  (("notepad" in p) or ("editor" in p) ) :
          os.system("notepad")
      
      elif (("run" in p) or  ("execute" in p ) or ("open" in p) or ("go to" in p))  and ("player" in p) and ("media" in p):
          os.system("wmplayer")
      elif (("run" in p) or ("execute" in p) or ("open" in p) or ("go to" in p)) and (("internet" in p) and ("explorer" in p) or ("browser" in p)):
          os.system("iexplore")
          elif  ("exit" in p)  or ("quit" in p):
              break

else:
    print("dont support")