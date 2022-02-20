class Directory:
    dir = []
    files = []
    atrib = ""
    name = ""
    cont = ""
    atrib = ""

    def __init__(self,n):
        self.name = n

    def dir_add(self, d):
        self.dir.append(d)

    def dir_remove(self, d):
        self.dir.remove(d)

    def in_dir(self,r):
        for d in self.dir:
            if d.get_name() == r:
                return r
            
        return ""
    
    def element(self):
        r = "_"
        for d in self.dir:
            r = r + d.get_name() + "\n "
            
        return r

    def file_add(self,f):
        self.files.append(f)

    def file_remove(self,f):
        self.files.remove(f)

    def writeFile(self,c):
        self.cont = c
    
    def readFile(self,f):
        return self.cont

    def set_atrib(self,r):
        self.atrib = r

    def get_atrib(self):
        return self.atrib

    def get_name(self):
        return self.name
