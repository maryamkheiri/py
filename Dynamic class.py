def constractor(self,val):
    self.val=val
    print("hello world!")
def miyo(self):
    print("miyooooo"+self.val)
cat=type("just practicing",(),{"__init__":constractor,"sound":miyo})
tom=cat("tommy")
tom.sound()
tom.__dict__