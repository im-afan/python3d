from math import cos, sin
import numpy as np

def makeTransMatrix3D(trans):
    return np.array([
        [1, 0, 0, trans[0]],
        [0, 1, 0, trans[1]],
        [0, 0, 1, trans[2]],
        [0, 0, 0, 1]
    ])

def makeRotMatrix(rot):
    yaw = rot[0]
    pitch = rot[1]
    roll = rot[2]

    yawMat = np.array([
        [1, 0, 0, 0],
        [0, cos(yaw), sin(yaw), 0],
        [0, sin(yaw), cos(yaw), 0],
        [0, 0, 0, 1]
    ])

    pitchMat = np.array([
        [cos(pitch), 0, -sin(pitch), 0],
        [0, 1, 0, 0],
        [sin(pitch), 0, cos(pitch), 0],
        [0, 0, 0, 1]
    ])

    rollMat = np.array([
        [cos(roll), sin(roll), 0, 0],
        [-sin(roll), cos(roll), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    return yawMat.dot(pitchMat).dot(rollMat)

