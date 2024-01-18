import random
movies=["Captain America","Captain Marvel","Iron Man","The Incredible Hulk","Thor","The Avengers","Spider-Man","Infinity War","Endgame","No Way Home"]

def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.attend(' ')
        else:
            temp.attend('*')
    qn=''.join(str(x) for x in temp)
    return qn
def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True
def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if ref[i]==' ' or ref[i]==letter:
            temp.append(ref[i])
        else:

def play():
    p1name=input('Player 1! please enter your name')
    p2name=input('player 2! please enter your name')
    pp1=0
    pp2=0
    turn=0
    willing=True
    while(willing):
        if turn%2==0:
            print(p1name,'your turn')
            picked_movie=random.choice(movies)
            qn=create_question(picked)
            print(qn)

            not_said=True
            while not_said:
                 letter=input('your letter:')
                 if(is_present(letter,picked_movie)):
                     modified_qn=unlock(modified_qn,picked_movie,ch)
                     print(modified_qn)
                     d=input('press 1 to guess the movie or 2 to unlock another letter')
                     if d==1:
                         ans=input('your answer:')
                         if ans==picked_movie:
                             pp1=pp1+1
                             print('çorrect')
                             not_said=False
                             print(p1name,'your score:',pp1)
                         else:
                             print("wrong ans . try again")
                 else:
                      print(letter,'not found')
        c=input('press 1 to continue or 0 to quit')
        if c==0:
            print(p1name,'your score:',pp1)
            print(p2name, 'your score:', pp2)
            print("thanks for playing")
            print("have a nice day")
            willing=False
        else:
            turn=turn+1

play()



