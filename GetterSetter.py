class getterSetter:
    def __init__(self,courseName):
        self.courseName=courseName
    def setCourse_Name(self,courseName):
        self.courseName=courseName.upper()
    def getCourse_Name(self):
        return(self.courseName)

ob=getterSetter("Python")
print(ob.getCourse_Name())
ob.setCourse_Name("MachineLearning")
print(ob.getCourse_Name())

