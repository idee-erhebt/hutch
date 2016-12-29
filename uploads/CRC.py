GRPY =[1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1]

def xordiv(x):
    while(len(x)>16):
        if(x[0]==1):
            for i in range(17):
                x[i]=x[i]^GRPY[i]

            while(len(x)!=0 and x[0]==0):
                x.pop(0)
    return x
            

print("Generotor polynomial is CRC-CCITT:",GRPY)

message=input("Enter message:").strip().split()
for i in range(len(message)):
    message[i]=int(message[i])

e_message=message+[0]*16
print("Message polynomial appended with zero's:",e_message)


ans=xordiv(e_message)

e_message=message+[0]*16

for i in range(len(e_message)-len(ans)):
    ans=[0]+ans

for i in range(len(e_message)):
    ans[i]=e_message[i]+ans[i]
print("Message with checksum appended:",ans)

message=input("Enter recieved polynomial:").strip().split()
for i in range(len(message)):
    message[i]=int(message[i])

message=xordiv(message)
if(len(message)==0):
    print("Correct")
else:
    print("Error")




