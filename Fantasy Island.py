print("""" ,,
`""*$b..
     ""*$o.
         "$$o.
           "*$$o.
              "$$$o.
                "$$$$bo...       ..o:
                  "$$$$$$$$booocS$$$    ..    ,.
               ".    "*$$$$SP     V$o..o$$. .$$$b
                "$$o. .$$$$$o. ...A$$$$$$$$$$$$$$b
          ""bo.   "*$$$$$$$$$$$$$$$$$$$$P*$$$$$$$$:
             "$$.    V$$$$$$$$$P"**""*"'   VP  * "l
               "$$$o.4$$$$$$$$X
                "*$$$$$$$$$$$$$AoA$o..oooooo..           .b
                       .X$$$$$$$$$$$P""     ""*oo,,     ,$P
                      $$P""V$$$$$$$:    .        ""*****"
                    .*"    A$$$$$$$$o.4;      .
                         .oP""   "$$$$$$b.  .$;
                                  A$$$$$$$$$$P
                                  "  "$$$$$P"
                                      $$P*"
                                     """"")
print("Welcome to Fantasy Island!")

choice1 = input("Would you like to play? Y or N \n").lower()
if choice1 == "y":
  print("Your adventure starts right now!")
  
  choice2 = input("You are faced with a fork in the road, do you want to go left or right?\n ").lower()
  if choice2 == "left":
    choice3 = input("Oh no... a river blocks your next movement.. do you Swim or Wait? \n").lower()
    if choice3 == "wait":
      choice4 = input("The river drained into a mysterious hole, BLAM!. \n You were teleported to a white room with three doors. \n Red, Blue and Yellow. Which one do you choose? ").lower()
      if choice4 == "yellow":
        print("CONGRATS YOU FOUND THE DRAGONS GOLD!! YOU WIN!")
        print('''     
     8 8 8 8                     ,ooo.
     8a8 8a8                    oP   ?b
    d888a888zzzzzzzzzzzzzzzzzzzz8     8b
     `""^""'                    ?o___oP' ''')
      elif choice4 == "red":
        print("YOU WERE TAKEN BY THE ALL SEEING EYE!!!! GAME OVER")
        print("""             ..,,;;;;;;,,,,
       .,;'';;,..,;;;,,,,,.''';;,..
    ,,''                    '';;;;,;''
   ;'    ,;@@;'  ,@@;, @@, ';;;@@;,;';.
  ''  ,;@@@@@'  ;@@@@; ''    ;;@@@@@;;;;
     ;;@@@@@;    '''     .,,;;;@@@@@@@;;;
    ;;@@@@@@;           , ';;;@@@@@@@@;;;.
     '';@@@@@,.  ,   .   ',;;;@@@@@@;;;;;;
        .   '';;;;;;;;;,;;;;@@@@@;;' ,.:;'
          ''..,,     ''''    '  .,;'
               ''''''::''''''''""")
      elif choice4 == "blue":
        print("YOU WERE TAKEN BY ALL SEEING EYE!!!! GAME OVER")
        print("""             ..,,;;;;;;,,,,
       .,;'';;,..,;;;,,,,,.''';;,..
    ,,''                    '';;;;,;''
   ;'    ,;@@;'  ,@@;, @@, ';;;@@;,;';.
  ''  ,;@@@@@'  ;@@@@; ''    ;;@@@@@;;;;
     ;;@@@@@;    '''     .,,;;;@@@@@@@;;;
    ;;@@@@@@;           , ';;;@@@@@@@@;;;.
     '';@@@@@,.  ,   .   ',;;;@@@@@@;;;;;;
        .   '';;;;;;;;;,;;;;@@@@@;;' ,.:;'
          ''..,,     ''''    '  .,;'
               ''''''::''''''''""")
      else:
        print("That door does not exist. Game over turd.")
    else:
      print("You forgot you can't swim! You were attacked by a gross looking fish!")
      print("""   _.-=-._     .-, 
 .'       "-.,' / 
(          _.  <
 `=.____.="  `._\ """)
  else:
    print("You tripped and fell over knocking your self out. lol nerd. GG GAME OVER!")
else:
  print("You did not choose an answer correctly, you got pinched by a crap! Game over!")
  print("PINCH PINCH")
