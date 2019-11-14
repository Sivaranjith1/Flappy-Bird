from bird import Bird
import numpy as np

class NN:
    def __init__(self):
        self.first_layer_weights = np.random.rand(3, 5)
        self.first_layer_bias = np.random.rand(3,1)/10

        self.final_layer_weights = np.random.rand(1, 3)
        self.final_layer_bias = np.random.rand(1,1)/10


        self.bird = Bird(50,250)

    def sigmoid(self, x):
        return 1/(1 + np.exp(-x))

    def predict(self,pipes):
        birdsX = self.bird.x
        birdsY = self.bird.y

        lastPipeX = 0
        lastPipeY = 0
        nextPipeX = 0
        nextPipeY = 0

        #getting the next pipe and the pipe that has passed
        for pipe in pipes:
            if pipe.x > birdsX:
                nextPipeX = pipe.x
                nextPipeY = pipe.y
                break
            else:
                lastPipeX = pipe.x
                lastPipeY = pipe.y

        nextPipeX -= birdsX

        #normalize data
        birdsY /= 500
        lastPipeX /= 500
        lastPipeY /= 500
        nextPipeX /= 500
        nextPipeY /= 500
        
        inputData = np.array([[birdsY, lastPipeY, lastPipeX, nextPipeY, nextPipeX]]).transpose()

        #run it in the modell
        firstlayer_before_sigmoid = np.matmul(self.first_layer_weights, inputData) + self.first_layer_bias
        firstlayer = self.sigmoid(firstlayer_before_sigmoid)


        lastlayer = self.sigmoid(self.final_layer_weights.dot(firstlayer) + self.final_layer_bias)
        

        output = 0
        if lastlayer[0][0] >= 0.5:
            output = 1
        return output

    

    @staticmethod
    def child(parent):
        first_layer_weights = parent.first_layer_weights.copy()
        first_layer_bias = parent.first_layer_bias.copy()
        final_layer_weights = parent.final_layer_weights.copy()
        final_layer_bias = parent.final_layer_bias.copy()

        newBird = NN()
        newBird.first_layer_weights = first_layer_weights + np.random.uniform(-1, 1, size=(3,5))
        newBird.first_layer_bias = first_layer_bias + np.random.uniform(-1, 1, size=(3,1))/100
        newBird.final_layer_weights = final_layer_weights + np.random.uniform(-1, 1, size=(1,3))
        newBird.final_layer_bias = final_layer_bias + np.random.uniform(-1, 1, size=(1,1))/100
        
        return newBird