import numpy as np
import matplotlib.pyplot as plt

inputFile = open("input2.txt", 'r')
rawData = inputFile.read().split("\n")
inputFile.close()

print(rawData)