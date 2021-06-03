from slr_table import Grammar, terminals, nonterminals, parsing_table

if __name__=="__main__":

    #file input(last term project output)
    file_pj1= open('lexical.out.txt','r')
    #hile ouput(if the grammar is accepted or not)
    fileout= open('syntax.out.txt','w')
    #file input uses as a string.
    output_of_project1=file_pj1.read()
    buffer = (output_of_project1).split()


    pointer = 0
    a = buffer[pointer]
    #create the stack.
    stack = ['0']

    step = 0

    #SLR Parser using First set and Follow set. See if the Grammar is accepted or not.
    while True:
        try:
            print(stack)
            
            s = int(stack[-1])
            step += 1

            #If there is no Symbols in parsing table, break
            if a not in parsing_table[s].keys():
                print("ERROR: Unrecognized Symbol", a)
                break

            #input the stack ,a
            elif parsing_table[s][a][0] == "s":

                stack.append(a)
                stack.append(parsing_table[s][a][1:])
                pointer += 1
                a = buffer[pointer]

            #parsing_ table grammar split and input the stack if that is head.
            elif parsing_table[s][a][0] == "r":
                print(1)
                grammar = Grammar[int(parsing_table[s][a][1:])].split()
                print(grammar,22)

                if grammar[-1] != '^':
                    if len(grammar)!=2:
                        stack = stack[:-(2 * len(grammar[grammar.index('->') + 1:]))]
                        # 윗 부분이 무얼 의미하는걸까 아 pop!!
                    s = int(stack[-1])
                    head = grammar[0]
                    stack.append(head)
                    stack.append(str(parsing_table[s][head]))

            #If all grammar accepted, break
            elif parsing_table[s][a] == "acc":
                a = "GRAMMAR : ACCEPTED"
                fileout.write(a)
                print(a)
                break

        #catch the TypeError and make some comment why the Error occured in output file.
        except TypeError:
            f = "GRAMMAR : REJECTED \n"
            g = "STACK: " + str(stack) + "<- Error occured from here."
            h = f + g
            print(f)
            print(g)
            print("\nType Error!!")
            fileout.write(h)
            fileout.write("\nType Error!!")
            break


        #catch the IndexError and make some comment why the Error occured in output file.
        except IndexError:
            f = "GRAMMAR : REJECTED \n"
            g = "STACK: " + str(stack) + "<- Error occured from here."
            h = f + g
            print(f)
            print(g)
            print("\nIndex Error!!")
            fileout.write(h)
            fileout.write("\nIndex Error!!")
            break

    #file close.
    file_pj1.close()
    fileout.close()