import numpy as np
import rotation

class Camera:
    def __init__(self, near, far, right, left, top, bottom):
        self.camPos = np.array([0, 0, 0, 0], dtype="float64")
        self.camRot = np.array([0, 0, 0], dtype="float64")
        self.near = near
        self.far = far
        self.right = right
        self.left = left
        self.top = top
        self.bottom = bottom

    def project(self, point, width, height): #width, heigth = canvas width/height
        view = (rotation.makeRotMatrix(self.camRot)).dot(rotation.makeTransMatrix3D(self.camPos))
        relpoint = view.dot(point)
        #print(relpoint[2])
        if(relpoint[2] >= self.near):
            return [(self.near*relpoint[0]/relpoint[2]/self.right + 1) * width/2, (self.near*relpoint[1]/relpoint[2]/self.top + 1) * height/2]
        else:
            return None