from random import randint 


user_name = input('What is your name ? ') 

greetings : str = f"""
    Hello {user_name}, Happy to see you here !  

    You can find a short explanation of the game here :

    We both geuss a number from 1 to 100.
    
    First one to guess it correctly with fewer atttempts, wins!
    
    Easy right ? You start. Let's go !

"""
print(greetings)

class NumberGuessingGame :

    def __init__(self, username ): 
        self.username = user_name
        self.user_score = 0
        self.computer_score = 0 
        self.max_attempts = 5
        self.total_rounds = 3

    def users_guess (self, computer_answer) :
        user_attempts = 0

        while user_attempts < self.max_attempts : 
            try : 

                user_guess = int(input('What number would you like to choose ? ')) 
                user_attempts += 1 

                if user_guess == computer_answer : 
                    print(f'Congratulations! the corroct answer was {computer_answer}. Which means you won this round') 
                    return True, user_attempts  
        
                elif user_guess < computer_answer : 
                     print(f'Incorroct! the correct answer is greater than {user_guess}')

                else : 
                    print(f'Incorrect! the number is less than {user_guess}') 

            except ValueError : 
                 print('Thats not a number, try to write a number ')
        

        print(f"""

        OH, It seems like i forgot to tell you :D 
              
        The correct answer was {computer_answer}

        You only had {self.max_attempts} attempts to guess it. 

        But don't worry {user_name}! Maybe next round ;>     
""")
        return False, user_attempts

    def computer_guess (self, user_answer) : 
    
        print('\nNow its my turn to guess yours')

        low = 1 
        high = 100 

        computer_attempts = 0 

        while computer_attempts < self.max_attempts :
            computer_guess = (low + high ) // 2 
            print(f'My guess is {computer_guess} ') 

            user_response = input('Tell me if its greater (+), lower (-) or correct (c) ').strip().lower() 
        

            if user_response not in ['+', '-', 'c'] : 
             print('Your respone have to be +, - or c ') 
             continue

            computer_attempts += 1 

            if user_response == '-' :
                 high = computer_guess - 1 
            elif user_response == '+' :
                low = computer_guess + 1 
            elif user_response == 'c' :
                 print (f'Yay! I guessed it right. :D') 
                 return True, computer_attempts
        
        print('It seems like i couldnt make it :<')
        return False, computer_attempts 
    
    def rounds(self):
        for round in range(1, self.total_rounds + 1): 
            print(f'___Round {round}___') 
           
            # for each round (random number)
            computer_answer = randint(1, 100) 

            #UsersRound
            print('\nIts your turn') 
            user_wins, user_attempts = self.users_guess(computer_answer) 

            #If user loses 
            if not user_wins : 
                print('\nIts my turn now!')
                computer_wins, computer_attempts = self.computer_guess(computer_answer)
            else:
                computer_wins = False 

            if user_wins:
                self.user_score += 1
            elif computer_wins:
                self.computer_score += 1
            else:
                
                print('Its a tie!') 
        if self.user_score == self.computer_score :
            final_round = input('Do you want to play an extra round to break the tie ? answer me with yes or no ').strip().lower()
            if final_round == 'yes':
                print('\n___Final___')
                computer_answer = randint(1, 100)
                
                print('\nYour turn!')
                user_wins, user_attempts = self.users_guess(computer_answer)
                    
                if not user_wins:
                    print('\nMy turn again')
                    computer_wins, computer_attempts = self.computer_guess(computer_answer)
                else:
                    computer_wins = False 

                if user_wins:
                        self.user_score += 1
                elif computer_wins:
                    self.computer_score += 1
                else:
                    print('Same scores again. I think we have to agree that we are both WINERS !')
            else: 
                print('OK,This game ended with a tie.') 

        print(f'''
            
            Game over.
            Final scores : 
            {user_name} : {self.user_score} 
            Computer : {self.computer_score}
             
         ''') 
        
        if self.user_score > self.computer_score :
            print(f'Congratulations {user_name}. You are a champion !') 
        elif self.computer_score > self.user_score :
            print(f'Hehe, I am the champion! Good luck next time {user_name}') 
        else :
            print('Well played! we are both champions, arent we ? :D') 

game = NumberGuessingGame(user_name)
game.rounds() 