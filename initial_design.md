# Initial Design Document
#### PLEASE! PLEASE! PLEASE! READ the [README.md](README.md) File carefully

1. Output an introduction of the game to user.
2. Set Player 1, Player 2, and Computer Losses as 0 
3. Set Play Choice as "yes"
4. Prompt user to input number of sticks they want to play with. (10-100)
5. While total sticks > 100 or total sticks < 10:
      1. Re-prompt user to enter the number of total sticks
6. While Play Choice = "yes":
   1. While total sticks does not equal 0:
      1. Set turn to equal 1
      2. Check if turn equals 1:
         1. Prompt player 1 to enter the number of sticks they would like to remove. (1-3)
         2. While sticks removed < 1 or sticks removed > 3:
            1. Re prompt user to enter the # of sticks they would like to remove.
         3. Subtract sticks removed from total sticks
         4. Set Loser to Player 1
         5. Set turn to 2
      3. Otherwise, Check if turn = 2
         1. Prompt player 2 to enter the number of sticks they would like to remove. (1-3)
         2. While sticks removed < 1 or sticks removed > 3:
            1. Re prompt user to enter the # of sticks they would like to remove.
         3. Subtract sticks removed from total sticks
         4. Set Loser as Player 2
         5. Set turn to 3
      4. Otherwise, Check if turn = 3
         1. Generate a random integer between (1-3)
         2. Subtract random integer from total sticks
         3. Set Loser as computer 
         4. Set turn to 1
   2. Output Loser to user
   3. Check if Loser = player 1:
      1. Add 1 to player 1 loss count
   4. Otherwise, Check if loser = player 2:
      1. Add 1 to player 2 loss count
   5. Otherwise:
      1. Add 1 to computer loss count
   6. Prompt user to input if they would like to keep playing (yes or no)
   7. Case correct play choice
   8. While play choice does not equal "yes" or "no":
      1. Prompt user to re-enter whether they would like to keep playing
      2. Case correct play choice
7. Output Player 1, Player 2, and Computer losses
8. Output Ending Message to User.
   


