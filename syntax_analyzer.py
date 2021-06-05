import sys
from slr_table import Grammar, terminals, nonterminals, parsing_table

if __name__=="__main__":
    # file_name=input()
    file_name = sys.argv[-1]
    in_f= open(file_name,'r')
    out_f= open('syntax.out.txt','w')

    str_f=in_f.read()+"$"
    in_f.close()
    input = str_f.split() # 여러개의 terminal들이 배열로 입력되어있다.

    #slr table을 스택과 함께 사용할 것이기때문에 임의로 0(첫번째 state)을 넣은 stack배열을 사용한다.
    stack = ['0']
    bar = 0 #shift의 기준이 되는 movebar를 의미한다.
    next_symbol = input[bar] #input이 배열에 들어가있으므로 bar는 input 배열의 인덱스로 사용된다.

    # 스택을 이용해 accept/reject인지 확인하는 while문
    while True:
        try:
            cur_state = int(stack[-1]) # 인덱스가 -1인 이유는 stack 배열의 마지막요소를 항상 확인해야하기 때문이다.
            ## shift-goto 인경우
            if parsing_table[cur_state][next_symbol][0] == "s":

                stack.append(next_symbol) # shift되어 reduce되지 못하는 symbol도 이동바가 움직이면서 handle이 될 수 있기때문에 스택에 넣어둔다고 가정한다.
                stack.append(parsing_table[cur_state][next_symbol][1:]) # table값이 sn이기때문에 (n은 state number) s라는 문자를 제외한 state number만 스택에 저장
                bar += 1 # 이동바는 한 칸 오른쪽으로 움직인다.
                next_symbol = input[bar] # 이동된 칸에 있는 input symbol을 next_symbol로 가정한다.

            ## reduce 인경우
            elif parsing_table[cur_state][next_symbol][0] == "r":
                grammar_order=int(parsing_table[cur_state][next_symbol][1:]) #CFG에서 r뒤의 숫자에 해당하는 문법을 가져온다.
                grammar = Grammar[grammar_order] # 해당하는 문법을 grammar 변수에 저장한다.
                
                #grammar의 길이가 1인경우(엡실론으로 production되는 경우)와 그렇지 않은 경우로 나눈다.
                if len(grammar)!=1:
                    stack = stack[:stack.index(grammar[1].split()[0])] 
                    # 인덱싱 기법을 활용하여 reduce되는 terminal/nonterminal의(특정 grammar의 화살표 뒤)첫번째 요소까지 제거한다.

                cur_state = int(stack[-1])
                new_symbol = grammar[0] # reduce된 새로운 symbol(특정 grammar의 화살표 앞)을 stack에 넣어준다.

                stack.append(new_symbol)
                stack.append(parsing_table[cur_state][new_symbol]) # 현재 state와 방금 넣은 새로운 symbol slrtable값도 넣어준다.
    

            # accept인경우
            elif parsing_table[cur_state][next_symbol] == "acc": # 해당 파싱 테이블의 값이 acc인 경우 input은 accept를 의미함
                # print("성공")
                message="INPUT '"+str_f+"' is ACCEPT!!"
                out_f.write(message)
                break # 바로 while문을 빠져나온다.


        except TypeError or IndexError:
            message='File "'+file_name+'" is REJECT!!\n'
            error = "Error : stack" + str(stack) + "is invalid stack(s)"
            out_f.write(message+error)
            break

    
    out_f.close()
