import threading 

def print_num():
    for i in range(0,5):
        print("Thread 1:",i)
        
def print_list():
    for i in  ['a','b','c']:
        print("T2 Thread:", i)
        
def main():
    t1 = threading.Thread(target=print_num)
    t2 = threading.Thread(target=print_list)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Done")


if __name__ == "__main__":
    main()