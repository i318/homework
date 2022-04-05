import random


wincounter = 0 

def play():
    user = input("Choose an option: r for rock, p for paper, s for scissors, sp for spock, l for lizard\n")
    computer = random.choice(['r', 'p', 's', 'sp', 'l'])
    if user == computer:
        return 'You have resulted in a tie, mi amigo'
    if is_win(user, computer):
        wincounter +=1
        return 'You won yippeeee!!!!' 
    return 'You lost, such a shame :((( '

def is_win(player, opponent):
    #r>s, s>p, p>r, l > sp, sp > s, p>sp, sp > r , l > p , s > l
    if (player == 'r'and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')\
        or (player == 'l' and opponent == 'sp') or (player == 'sp' and opponent == 's') or (player == 'p' and opponent == 'sp')\
            or (player == 'sp' and opponent == 'r') or (player == 'l' and opponent == 'p') or (player == 's' and opponent == 'l'):
            return True



print(play())
print(str(wincounter))
