from time import sleep
from threading import Thread

class Hello(Thread):
    def run(self):
        for i in range(5):
                print("hello")
                sleep(1)
class Hi(Thread):
    def run(self):

        for i in range(5):
             print("Hi")

t1=Hello()
t2=Hi()

t1.start()          #this is a different thread t1
sleep(0.2)
t2.start()          #this is another thread t2

t1.join()
t2.join()
#main thread will not execute until both t1 and t2 will join
print("bye")



#this whole program is using a main thread
#but to run on different core or different threads not in Main thread
#we need Thread as a parent of the Hi and Hello class


# multi-threading
# threading is light-weight process and that process is divided into small parts

# that part is called thread
# can i execute 2 function on different cores at the same time

#zip() zips two list with each other
list=['anu','thakur','king]
num=['ab','cd','ef']
zipped=zip(list,num)
      for (a,b) in zipped:
            print(a,b)
