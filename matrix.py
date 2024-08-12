import numpy as np
from imageutils import *
from cosine_similarity import *

class DigitMatrices:
    matrices = {}
    def __init__(self):
        None
      
    def add_object(self, DigitMatrix):
        self.matrices[DigitMatrix.digit] = DigitMatrix
    
    def printMatrix(self):
        print(f"Digit: {matrix.digit}")
        print(f"{matrix.cos_similarity}\n\n\n")
        

class DigitMatrix:
    size = ()
    digit = None
    path = ""
    img_dict = {}
    matrix = np.zeros(shape=(1,))
    embedding = np.zeros(shape=(1,))
    U = np.zeros(shape=(1,))
    S = np.zeros(shape=(1,))
    VT = np.zeros(shape=(1,))
    thresh_perc = 0

    def __init__(self, path, digit, size, threshold):
        self.path = path
        self.digit = digit
        self.size = size
        self.thresh_perc = threshold
        self.img_dict = load_images(path, size[0], size[1])
        self.matrix = combine_matrix(self.img_dict)
        self.principal_components()
        self.embedding = self.set_subspace()
        print(f"Class: {self.digit} has been initialized")

    def set_subspace(self):
        if len(self.U.shape) != 2:
            self.U = self.U.reshape(self.U.shape[0], -1)
        return create_sub(self.U)
    
    def setMatrix(self):
        self.matrix = combine_matrix(self.img_dict)
            
    def getDict(self):
        return self.img_dict
    
    def getMatrix(self):
        return self.matrix
    
    def getSubspace(self):
        return self.embedding
    
    def printMatrix(self):
        print(f"Digit: {self.digit}")
        print(f"Matrix: {self.embedding}\n")
        #print(f"Image Dictionary: {self.img_dict}\n")
    
    def principal_components(self):
        matrix_svd = np.linalg.svd(self.matrix)
        U = matrix_svd.U
        S = matrix_svd.S
        VT = matrix_svd.Vh
        
        #Get only principal compopents of U
        threshold = self.thresh_perc * np.max(S)
        indices = np.where(S > threshold)
        self.U = U[:, indices]
        self.S = S[indices]
        self.VT = VT[indices]
        self.embedding = self.U

#tests cos similarity of a test image across each subspace and chooses the subspace it projects in the most
def predict_class(classes, test_image):
    highest = 0
    predicted_class = None
    for i in range(len(classes)):
        projection_vector = project_image(test_image, classes[i].embedding) #classes[i].getSubspace().dot(test_image)
        cos_sim = abs(cosine_similarity(test_image, projection_vector))
        if cos_sim > highest:
            highest = cos_sim
            predicted_class = classes[i].digit
    return predicted_class