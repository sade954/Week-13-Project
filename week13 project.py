import random
import string

print("This is the random name generator")
print("")

depts = ['marketing', 'accounting', 'finops']
ec2list = []

def string_generator(size=6, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))
    
#Department input and check
department = input("Please state your department (Marketing, Accounting. FinOps): ").lower()

#If department unsuccessful print unauthorized message
if (department  not in depts):
    print("You are not authorized to use this EC2 name generator. ")
else #if department check successful take amount
    print("")
    amount = int(input("Enter the amount of EC2instances: "))
#Instance name creation. Created instance, randomnum, randomchar, ec2name variables
    for instance in range(0, amount):
    randomnum = random.randint(100, 999)
    randomchar = ''.join(random.choices(string.ascii_letters, k=5)) 
    ec2name = "{}_{}{}{}".format(department, randomnum, randomchar, instance)
    ec2list.append(ec2name)
#Print formatted list
    print("\n".join(ec2list))
    
    
    
    
    
    
