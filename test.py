import csv


with open('data2.csv','r') as f:
    c_reader=csv.reader(f)

    cc=0;
    c=0;
    
    f = open("test_final.csv", "a")
    for line in c_reader:
        c=c+1;
        
        if (line[10]) !=str(1) and (line[10]) !=str(0) :
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
