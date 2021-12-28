
d=0

class puzzle:
    def start(self):
        print("enter the start state of the puzzle")
        start_=[[0,0,0,],[0,0,0,],[0,0,0,]]
        for i in range(0,3):
            for j in range(0,3):
                print("enter the value of {} th row {} th column ".format(i,j))
                value=input()
                start_[i][j]=value
        goal_=[[0,0,0,],[0,0,0,],[0,0,0,]]
        print("enter the goal state of the puzzle")
        for i in range(0,3):
            for j in range(0,3):
                print("enter the value of {} th row {} th column ".format(i,j))
                value=input()
                goal_[i][j]=value
        print("start state :")
        for i in range(0,3):
            for j in range(0,3):
                print(start_[i][j],end=" ")
            print("")
        print("  ")
        print("--------------")
        print("goal state :")
        for i in range(0,3):
            for j in range(0,3):
                print(goal_[i][j],end=" ")
            print("")
        print("  ")
        print("--------------")
        start_=self.function(start_,goal_)
        #for i in range(0,3):
         #   for j in range(0,3):
          #      print(start_[i][j],end=" ")
           # print("")
        #print("  ")
        #print("--------------")
        
    def heuristic(self,start_,goal_):
        #finding heuristic value
        h=0
        for i in range(0,3):
            for j in range(0,3):
                if start_[i][j]!=goal_[i][j] and start_[i][j]!=0 :
                    h=h+1
        return h 
    
    def find(self,start_):
        #finding blank state
        for i in range(0,3):
            for j in range(0,3):
                if start_[i][j]==0:
                    l=[i,j]
                    return l

    def function(self,start_,goal_):
        global d
        d=d+1
        # finding bank state
        for i in range(0,3):
            for j in range(0,3):
                if start_[i][j]=='0':
                    m=i
                    n=j
 #making all the possible changes 
        if m==0 or m==2 :
            if n==0 or n==2:
                s1=[[0,0,0,],[0,0,0,],[0,0,0,]]
                s2=[[0,0,0,],[0,0,0,],[0,0,0,]]
                for i in range(0,3):
                    for j in range(0,3):
                        s1[i][j]=start_[i][j]
                        s2[i][j]=start_[i][j]
                if m==0 and n==0:
                    t=s1[0][0]
                    s1[0][0]=s1[0][1]
                    s1[0][1]=t
                    t=s2[0][0]
                    s2[0][0]=s2[1][0]
                    s2[1][0]=t
                if m==0 and n==2:
                    t=s1[0][2]
                    s1[0][2]=s1[0][1]
                    s1[0][1]=t
                    t=s2[0][2]
                    s2[0][2]=s2[1][2]
                    s2[1][2]=t
                if m==2 and n==2:
                    t=s1[2][2]
                    s1[2][2]=s1[2][1]
                    s1[2][1]=t
                    t=s2[2][2]
                    s2[2][2]=s2[1][2]
                    s2[1][2]=t
                if m==2 and n==0:
                    t=s1[2][0]
                    s1[2][0]=s1[2][1]
                    s1[2][1]=t
                    t=s2[2][0]
                    s2[2][0]=s2[1][0]
                    s2[1][0]=t
                #calculating f(n)
                h1=d+self.heuristic(s1,goal_)
                h2=d+self.heuristic(s2,goal_)
                if h1>h2:
                    test=0
                    for i in range(0,3):
                        for j in range(0,3):
                            print(s2[i][j],end=" ")
                            if goal_[i][j]!=s2[i][j]:
                                test=1
                        print("")
                    print("  ")
                    print("--------------")
                    if test==1:
                        #not a goal state calling the function again
                        return self.function(s2,goal_)
                    else :
                        #goal state reached returning the state 
                        return s2
                else :
                    test=0
                    for i in range(0,3):
                        for j in range(0,3):
                            print(s1[i][j],end=" ")
                            if goal_[i][j]!=s1[i][j]:
                                test=1
                        print("")
                    print("  ")
                    print("--------------")
                    if test==1:
                        #not a goal state calling the function again
                        return self.function(s1,goal_)
                    else :
                        #goal state reached returning the state 
                        return s1
            if n==1 :
                s1=[[0,0,0,],[0,0,0,],[0,0,0,]]
                s2=[[0,0,0,],[0,0,0,],[0,0,0,]]
                s3=[[0,0,0,],[0,0,0,],[0,0,0,]]
                for i in range(0,3):
                    for j in range(0,3):
                        s1[i][j]=start_[i][j]
                        s2[i][j]=start_[i][j]
                        s3[i][j]=start_[i][j]
                if m==0:
                    t=s1[0][1]
                    s1[0][1]=s1[0][0]
                    s1[0][0]=t
                    t=s2[0][1]
                    s2[0][1]=s2[0][2]
                    s2[0][2]=t
                    t=s3[0][1]
                    s3[0][1]=s2[1][1]
                    s3[1][1]=t
                if m==2:
                    t=s1[2][1]
                    s1[2][1]=s1[2][0]
                    s1[2][0]=t
                    t=s2[2][1]
                    s2[2][1]=s2[2][2]
                    s2[2][2]=t
                    t=s3[2][1]
                    s3[2][1]=s3[1][1]
                    s3[1][1]=t
                #calculating f(n)
                h1=d+self.heuristic(s1,goal_)
                h2=d+self.heuristic(s2,goal_)
                h3=d+self.heuristic(s3,goal_)
                if h1<h2:
                    if h1<h3 :
                        test=0
                        for i in range(0,3):
                            for j in range(0,3):
                                print(s1[i][j],end=" ")
                                if goal_[i][j]!=s1[i][j]:
                                    test=1
                            print("")
                        print("  ")
                        print("--------------")
                        if test==1:
                            #not a goal state calling the function again
                            return self.function(s1,goal_)
                        else :
                            #goal state reached returning the state 
                            return s1
                    else :
                        test=0
                        for i in range(0,3):
                            for j in range(0,3):
                                print(s3[i][j],end=" ")
                                if goal_[i][j]!=s3[i][j]:
                                    test=1
                            print("")
                        print("  ")
                        print("--------------")
                        if test==1:
                            #not a goal state calling the function again
                            return self.function(s3,goal_)
                        else :
                            #goal state reached returning the state 
                            return s3
                else :
                    if h2<h3 :
                        test=0
                        for i in range(0,3):
                            for j in range(0,3):
                                print(s2[i][j],end=" ")
                                if goal_[i][j]!=s2[i][j]:
                                    test=1
                            print("")
                        print("  ")
                        print("--------------")
                        if test==1:
                            #not a goal state calling the function again
                            return self.function(s2,goal_)
                        else :
                            #goal state reached returning the state 
                            return s2
                    else :
                        test=0
                        for i in range(0,3):
                            for j in range(0,3):
                                print(s3[i][j],end=" ")
                                if goal_[i][j]!=s3[i][j]:
                                    test=1
                            print("")
                        print("  ")
                        print("--------------")
                        if test==1:
                            #not a goal state calling the function again
                            return self.function(s3,goal_)
                        else :
                            #goal state reached returning the state 
                            return s3
        elif m==1 :
            s1=[[0,0,0,],[0,0,0,],[0,0,0,]]
            s2=[[0,0,0,],[0,0,0,],[0,0,0,]]
            s3=[[0,0,0,],[0,0,0,],[0,0,0,]]
            for i in range(0,3):
                    for j in range(0,3):
                        s1[i][j]=start_[i][j]
                        s2[i][j]=start_[i][j]
                        s3[i][j]=start_[i][j]
            if n!=1 :
                if n==0:
                    t=s1[1][0]
                    s1[1][0]=s1[1][1]
                    s1[1][1]=t
                    t=s2[1][0]
                    s2[1][0]=s2[0][0]
                    s2[0][0]=t
                    t=s3[1][0]
                    s3[1][0]=s3[2][0]
                    s3[2][0]=t
                if n==2:
                    t=s1[1][2]
                    s1[1][2]=s1[1][1]
                    s1[1][1]=t
                    t=s2[1][2]
                    s2[1][2]=s2[0][2]
                    s2[0][2]=t
                    t=s3[1][2]
                    s3[1][2]=s3[2][2]
                    s3[2][2]=t
                #calculating f(n)
                h1=d+self.heuristic(s1,goal_)
                h2=d+self.heuristic(s2,goal_)
                h3=d+self.heuristic(s3,goal_)
                if h1<h2:
                    if h1<h3 :
                        test=0
                        for i in range(0,3):
                            for j in range(0,3):
                                print(s1[i][j],end=" ")
                                if goal_[i][j]!=s1[i][j]:
                                    test=1
                            print("")
                        print("  ")
                        print("--------------")
                        if test==1:
                            #not a goal state calling the function again
                            return self.function(s1,goal_)
                        else :
                            #goal state reached returning the state 
                            return s1
                    else :
                        test=0
                        for i in range(0,3):
                            for j in range(0,3):
                                print(s3[i][j],end=" ")
                                if goal_[i][j]!=s3[i][j]:
                                    test=1
                            print("")
                        print("  ")
                        print("--------------")
                        if test==1:
                            #not a goal state calling the function again
                            return self.function(s3,goal_)
                        else :
                            #goal state reached returning the state 
                            return s3
                else :
                    if h2<h3 :
                        test=0
                        for i in range(0,3):
                            for j in range(0,3):
                                print(s2[i][j],end=" ")
                                if goal_[i][j]!=s2[i][j]:
                                    test=1
                            print("")
                        print("  ")
                        print("--------------")
                        if test==1:
                            #not a goal state calling the function again
                            return self.function(s2,goal_)
                        else :
                            #goal state reached returning the state 
                            return s2
                    else :
                        test=0
                        for i in range(0,3):
                            for j in range(0,3):
                                print(s3[i][j],end=" ")
                                if goal_[i][j]!=s3[i][j]:
                                    test=1
                            print("")
                        print("  ")
                        print("--------------")
                        if test==0:
                            #goal state reached returning the state 
                            return s3
                        else :
                            #not a goal state calling the function again
                            return self.function(s3,goal_)
                            
            else :
                s4=[[0,0,0,],[0,0,0,],[0,0,0,]]
                for i in range(0,3):
                    for j in range(0,3):
                        s4[i][j]=start_[i][j]
                t=s1[1][1]
                s1[1][1]=s1[0][1]
                s1[0][1]=t
                t=s2[1][1]
                s2[1][1]=s2[2][1]
                s2[2][1]=t
                t=s3[1][1]
                s3[1][1]=s3[1][0]
                s3[1][0]=t
                t=s4[1][1]
                s4[1][1]=s3[1][2]
                s4[1][2]=t
                #calculating f(n)
                h1=d+self.heuristic(s1,goal_)
                h2=d+self.heuristic(s2,goal_)
                h3=d+self.heuristic(s3,goal_)
                h4=d+self.heuristic(s4,goal_)
                if h1<h2:
                    if h4<h3 :
                        if h1<h4:
                            test=0
                            for i in range(0,3):
                                for j in range(0,3):
                                    print(s1[i][j],end=" ")
                                    if goal_[i][j]!=s1[i][j]:
                                        test=1
                                print("")
                            print("  ")
                            print("--------------")
                            if test==1:
                                #not a goal state calling the function again
                                return self.function(s1,goal_)
                            else :
                                #goal state reached returning the state 
                                return s1
                            
                        else :
                            test=0
                            for i in range(0,3):
                                for j in range(0,3):
                                    print(s4[i][j],end=" ")
                                    if goal_[i][j]!=s4[i][j]:
                                        test=1
                                print("")
                            print("  ")
                            print("--------------")
                            if test==1:
                                #not a goal state calling the function again
                                return self.function(s4,goal_)
                            else :
                                #goal state reached returning the state 
                                return s4
                    else :
                        if h1<h3:
                            test=0
                            for i in range(0,3):
                                for j in range(0,3):
                                    print(s1[i][j],end=" ")
                                    if goal_[i][j]!=s1[i][j]:
                                        test=1
                                print("")
                            print("  ")
                            print("--------------")
                            if test==1:
                                #not a goal state calling the function again
                                return self.function(s1,goal_)
                            else :
                                #goal state reached returning the state 
                                return s1
                        else :
                            test=0
                            for i in range(0,3):
                                for j in range(0,3):
                                    print(s3[i][j],end=" ")
                                    if goal_[i][j]!=s3[i][j]:
                                        test=1
                                print("")
                            print("  ")
                            print("--------------")
                            if test==1:
                                #not a goal state calling the function again
                                return self.function(s3,goal_)
                            else :
                                #goal state reached returning the state 
                                return s3

                else :
                    if h4<h3 :
                        if h2<h4:
                            test=0
                            for i in range(0,3):
                                for j in range(0,3):
                                    print(s2[i][j],end=" ")
                                    if goal_[i][j]!=s2[i][j]:
                                        test=1
                                print("")
                            print("  ")
                            print("--------------")
                            if test==1:
                                #not a goal state calling the function again
                                return self.function(s2,goal_)
                            else :
                                #goal state reached returning the state 
                                return s2
                        else :
                            test=0
                            for i in range(0,3):
                                for j in range(0,3):
                                    print(s4[i][j],end=" ")
                                    if goal_[i][j]!=s4[i][j]:
                                        test=1
                                print("")
                            print("  ")
                            print("--------------")
                            if test==1:
                                #not a goal state calling the function again
                                return self.function(s4,goal_)
                            else :
                                #goal state reached returning the state 
                                return s4
                    else :
                        if h2<h3:
                            test=0
                            for i in range(0,3):
                                for j in range(0,3):
                                    print(s2[i][j],end=" ")
                                    if goal_[i][j]!=s2[i][j]:
                                        test=1
                                print("")
                            print("  ")
                            print("--------------")
                            if test==1:
                                #not a goal state calling the function again
                                return self.function(s2,goal_)
                            else :
                                #goal state reached returning the state 
                                return s2
                        else :
                            test=0
                            for i in range(0,3):
                                for j in range(0,3):
                                    print(s3[i][j],end=" ")
                                    if goal_[i][j]!=s3[i][j]:
                                        test=1
                                print("")
                            print("  ")
                            print("--------------")
                            if test==1:
                                #not a goal state calling the function again
                                return self.function(s3,goal_)
                            else :
                                #goal state reached returning the state 
                                return s3
                

    


p=puzzle()
p.start()