import random
import string

def generate_unique_ec2_names(num_instances, department_name):
    ec2_names = []
    for i in range(num_instances):
        
        random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
       
        ec2_name = f"{department_name}-EC2-{random_suffix}"
        ec2_names.append(ec2_name)
    return ec2_names

def main():
    
    num_instances = int(input("Enter the number of EC2 instances you want names for: "))
    
    department_name = input("Enter your department name (e.g., IT, Finance, etc.): ")

   
    ec2_names = generate_unique_ec2_names(num_instances, department_name)

   
    print("\nGenerated EC2 Names:")
    for name in ec2_names:
        print(name)

if __name__ == "__main__":
    main()
