def q_rand():
    que="How many"
    q_type="2"
    options=['Ind',"Aus"]
    return que,q_type,options
def main():
            quiz={}
            #mid=i['match_id']
            quiz["match_id"]="222"
            quiz["curparticipation"]="1"
            quiz["minq"]="12"
            quiz["pfee"]="10"
            quiz["q_array"]={}
            for i in range(21):
                quiz["q_array"][str(i)]={}
                que,q_type,options=q_rand()
                quiz["q_array"][str(i)]["content"]=que
                quiz["q_array"][str(i)]["type"]=q_type
                print(options)
                if options!=-1:
                    quiz["q_array"][str(i)]["options"]={}
                    for j in range(len(options)):
                        quiz["q_array"][str(i)]["options"][str(j)]=options[j]
                else:
                    quiz["q_array"][str(i)]["options"]=""
                


                


            return quiz
print(main())