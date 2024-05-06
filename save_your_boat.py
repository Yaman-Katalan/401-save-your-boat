choice=input("""
    welcome to save your boat game :D

    Description: 

        1) You have a boat that has 5 lives. When boat lives end it will drown.
        2) You should guess the word by choosing a letter from the English alphabet
        3) If you got the letter wrong you will lose a life.
        4) When you guess the letter right you will be provided with the updated word
        5) If you guess everything right you will win
        6) If you finish your lives without guessing the word you will lose.
        7) To quit, you can type exit

wanna play? (y, n) 
""")

game=[
    {'word': 'apple'},
    {'hints': ['Red and Yummy', 'Good for Pies', 'Healthy Snack', 'Juicy and Crunchy', 'Round in shape']}
]

game_hints=game[1]['hints']
game_word= list(game[0]['word'])
letter=game_word.pop(0)

hint_count=2
lives=5

word=''

if choice == 'y':
    print(f"""
guess this
_ _ _ _ _
          
          {game_hints[0]}
          {game_hints[1]}
""")
    while True:
     answer=input("choose a letter ->")
     
     if answer==letter:
        print("yay, you got it right!")
        word+=letter
        if len(game_word):
         letter=game_word.pop(0)
        print(f"word after guess\n{word} {"_ "*(len(game_word)+1)}")
     else:
        print("you got it wrong")
        lives-=1
        print(f"boat lives: {lives}")
     
     if lives==1:
        print("More hints:")
        while len(game_hints):
           print(f"   -{game_hints.pop(0)}")
           

     if word == game[0]['word']:
        print("Congrats! You won!")
        break

     if answer == 'exit' or lives==0:
        print("Game Over")
        break

      



