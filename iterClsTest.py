#modified form :https://stackoverflow.com/questions/10814535/can-i-iterate-over-a-class-in-python
import time

class it(type):
    def __iter__(self):
        # Wanna iterate over a class? Then ask that class for iterator.
        return self.classiter()

class Foo:
    __metaclass__ = it # We need that meta class...
    by_id = {} # Store the stuff here...

    def __init__(self, id): # new isntance of class
        print(id,'Foo constructor called')   
        self.id = id # do we need that?
        self.by_id[id] = self # register istance
        
    def __del__(self):
        print(self.id,'Foo destructor is called with some delay')  
        print(self.id,"elapsed_time[sec]",time.time() - self.start)
        if self.id in self.by_id:
            print(self.id,'exists!') 
            self.by_id.pop(self.id, None) # None(self.id)
        else:
            print(self.id,'not exist!') 
 
    def delete(self):
        print(self.id,'Foo delete called')    
        if self.id in self.by_id:
            print(self.id,'will be deleted!') 
            self.by_id.pop(self.id, None) # None(self.id)
            self.start = time.time()
        else:
            print(self.id,'does not exist!')            
        
        
    def getId(self):
        return self.id

    @classmethod
    def classiter(cls): # iterate over class by giving all instances which have been instantiated
        return iter(cls.by_id.values())

if __name__ == '__main__':
    a = Foo(123)
    b = Foo(456)
    print list(Foo)
    a.delete()
    #a.__del__()
    #del a
    #del a #does not work
    print list(Foo)
    for foo in Foo:
        print (foo.getId())
    c = Foo(789)   
    for foo in Foo:
        print (foo.getId())
    print list(Foo)    
    b.delete()
    c.delete()
    print('all deleted!')
    print list(Foo)
    for foo in Foo:
        print (foo.getId())    
        
        