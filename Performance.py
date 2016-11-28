
def calculate_accuracy(name_classifier,dict1):

    classified_as_1=dict1['classified_as_1']
    correctly_classified_as_1=dict1['correctly_classified_as_1']
    belongs_to_1=dict1['belongs_to_1']
    classified_as_2=dict1['classified_as_2']
    correctly_classified_as_2=dict1['correctly_classified_as_2']
    belongs_to_2=dict1['belongs_to_2']
    classified_as_3=dict1['classified_as_3']
    correctly_classified_as_3=dict1['correctly_classified_as_3']
    belongs_to_3=dict1['belongs_to_3']
    classified_as_4=dict1['classified_as_4']
    correctly_classified_as_4=dict1['correctly_classified_as_4']
    belongs_to_4=dict1['belongs_to_4']
    classified_as_5=dict1['classified_as_5']
    correctly_classified_as_5=dict1['correctly_classified_as_5']
    belongs_to_5=dict1['belongs_to_5']

    fo = open(name_classifier+'_output.txt','w')



#    fo.write("\n"+"Classified as Pos: "+str(classified_as_pos)+"\n")
#    fo.write("Correctly classified as Pos: "+str(correctly_classified_as_pos)+"\n")
#    fo.write("Belongs as Pos: "+str(belongs_to_pos)+"\n")

#    fo.write("Classified as Neg: "+str(classified_as_neg)+"\n")
#    fo.write("Correctly classified as Neg: "+str(correctly_classified_as_neg)+"\n")
#    fo.write("Belongs as Neg: "+str(belongs_to_neg)+"\n")
    precision_1=0
    if(classified_as_1!=0):
        precision_1=correctly_classified_as_1/classified_as_1
        print(precision_1)
        fo.write("1 Precision:"+str(round(precision_1,2))+'\n')
    else:
        fo.write("1 Precison:"+'N/A\n')

    recall_1=0
    if(belongs_to_1!=0):
        recall_1=correctly_classified_as_1/belongs_to_1
        print(recall_1)
        fo.write("1 Recall:"+str(round(recall_1,2))+'\n')
    else:
        fo.write("1 Recall:"+'N/A\n')

    if(recall_1==0 and precision_1==0):
        fo.write("1 F1 score:"+'N/A\n')
    else:
        fo.write("1 F1 score:"+str(round(2*recall_1*precision_1/(recall_1+precision_1),2))+'\n')

    precision_2=0
    if(classified_as_2!=0):
        precision_2=correctly_classified_as_2/classified_as_2
        print(precision_2)
        fo.write("2 Precision:"+str(round(precision_2,2))+'\n')
    else:
        fo.write("2 Precison:"+'N/A\n')

    recall_2=0
    if(belongs_to_2!=0):
        recall_2=correctly_classified_as_2/belongs_to_2
        print(recall_2)
        fo.write("2 Recall:"+str(round(recall_2,2))+'\n')
    else:
        fo.write("2 Recall:"+'N/A\n')

    if(recall_2==0 and precision_2==0):
        fo.write("2 F1 score:"+'N/A\n')
    else:
        fo.write("2 F1 score:"+str(round(2*recall_2*precision_2/(recall_2+precision_2),2))+'\n')
    
    precision_3=0
    if(classified_as_3!=0):
        precision_3=correctly_classified_as_3/classified_as_3
        print(precision_3)
        fo.write("3 Precision:"+str(round(precision_3,2))+'\n')
    else:
        fo.write("3 Precison:"+'N/A\n')

    recall_3=0
    if(belongs_to_3!=0):
        recall_3=correctly_classified_as_3/belongs_to_3
        print(recall_3)
        fo.write("3 Recall:"+str(round(recall_3,2))+'\n')
    else:
        fo.write("3 Recall:"+'N/A\n')

    if(recall_3==0 and precision_3==0):
        fo.write("3 F1 score:"+'N/A\n')
    else:
        fo.write("3 F1 score:"+str(round(2*recall_3*precision_3/(recall_3+precision_3),2))+'\n')
    
    precision_4=0
    if(classified_as_4!=0):
        precision_4=correctly_classified_as_4/classified_as_4
        print(precision_4)
        fo.write("4 Precision:"+str(round(precision_4,2))+'\n')
    else:
        fo.write("4 Precison:"+'N/A\n')

    recall_4=0
    if(belongs_to_4!=0):
        recall_4=correctly_classified_as_4/belongs_to_4
        print(recall_4)
        fo.write("4 Recall:"+str(round(recall_4,2))+'\n')
    else:
        fo.write("4 Recall:"+'N/A\n')

    if(recall_4==0 and precision_4==0):
        fo.write("4 F1 score:"+'N/A\n')
    else:
        fo.write("4 F1 score:"+str(round(2*recall_4*precision_4/(recall_4+precision_4),2))+'\n')

    precision_5=0
    if(classified_as_5!=0):
        precision_5=correctly_classified_as_5/classified_as_5
        print(precision_5)
        fo.write("5 Precision:"+str(round(precision_5,2))+'\n')
    else:
        fo.write("5 Precison:"+'N/A\n')

    recall_5=0
    if(belongs_to_5!=0):
        recall_5=correctly_classified_as_5/belongs_to_5
        print(recall_5)
        fo.write("5 Recall:"+str(round(recall_5,2))+'\n')
    else:
        fo.write("5 Recall:"+'N/A\n')

    if(recall_5==0 and precision_5==0):
        fo.write("5 F1 score:"+'N/A\n')
    else:
        fo.write("5 F1 score:"+str(round(2*recall_5*precision_5/(recall_5+precision_5),2))+'\n')

    fo.close()