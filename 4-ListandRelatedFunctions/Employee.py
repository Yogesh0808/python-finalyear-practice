class Employee:
    def _init__(self,id,name,gender):
        self.id = id 
        self.name = name
        self.gender = gender
    
    def display_info():
        print(self.id, self.name, self.gender)
        
def main():
    emp = Employee(101,"Sankar","Male")
    emp.display_info()
    
if __name__ == "__main__":
    main()