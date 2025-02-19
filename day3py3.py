print('''
      *******************************************************************************
          |                   |                  |                     |
 ________|.="";=.||______
|                   |  ,-"_,=""     `"=.|                  |
||"=._o`"-.        `"=.|___________________
          |                "=._o"=._      `"=.                     |
 ________|:=.o "=..".-="'"=.|______
|                   |    _.--" , ; `"=._o." ,-"""-. ".   |
||."  ,. .` ` `` ,  `"-."-._   ". '|___________________
          |           |o`"=.` , "` `; .". ,  "-."-._; ;              |
 ________|| ;-.o"=._; ." ` '."\ . "-._ /|______
|                   | |o;    "-.o"=.``  '` " ,_.--o;   |
||| ;     (#) `-.o `"=.`_.--"o.-; ;|___________________
___///|o;._    "      `".o|o_.--"    ;o;///____
////"=._o--.        ; | ;        ; ;////_
___////"=._o--.   ;o|o;     .;o;///____
/////"=.o.; | ;.--"o.--"////_
___/////"=.o|o_.--""////___
///////////[TomekK]
******************************************************************************* ''')
print("welcome to treasure Island.")
print("your mission is to find the treasure.")
cross_road =  input('you are at a cross road. where do you want to go? type "left" or "right".')
if cross_road == "left":
    print("the game will continue.....")
    cross_lake = input('you have come to a lake. there is an island in the middle of lake. type"wait" to wait for a boat. type "swim" to swim acoss')
    if cross_lake == "wait":
        print("the game will continue....")
        choose_door = input('you come to lake without any bruise. there is 3 room."one red" one blue" one yellow".' )
        if choose_door == "red":
            print("room full of electric leser light")
        elif choose_door == "blue":
            print("room full on thrones")
        elif choose_door == "yellow":
            print("you find the teasure. game over")
    else:
        print(" you got biten by snake.game over.")

else: 
    print("you fell in the hole.game over.")