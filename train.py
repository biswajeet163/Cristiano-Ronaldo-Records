import csv


with open('data2.csv','r') as ff:
    c_reader=csv.reader(ff)

    cc=0;
    c=0;
    
    f = open("train2.csv", "a")

###########  writing header.............
    count=0;
    for line in c_reader:
        count=count+1;
        for i in line:
            f.write(str(i) + " , ");
            #print(str(i) + " , ");
        f.write("\n");


        if(count==1):
            break;

################### writing data.............
     
    for line in c_reader:
        c=c+1;
        
        if (line[10]) ==str(1) or (line[10]) ==str(0) :
            cc=cc+1;
            for i in line:
                f.write(str(i) + " , ");
                #print(str(i) + " , ");
            f.write("\n");
            #print("\n");

        
    f.close()
        
 




        
       
       
        



print ("\n\n\nHello Lord")
print(c);
print(cc);
