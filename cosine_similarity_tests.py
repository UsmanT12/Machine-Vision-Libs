from cosine_similarity import *

#Normalized image for img_261.jpg (2)
loaded_images_2 = load_images('trainingSet/2')
image_261 = Image.open('trainingSet/2/img_261.jpg')
array_261 = loaded_images_2['img_261.jpg']
norm_261 = np.linalg.norm(array_261)
normalized_261 = array_261 / norm_261
flat_array_261 = normalized_261.flatten()
flat_normalized_261 = np.array(flat_array_261)
#print('Normalized image array: ', normalized_261)

#compute dot product of img_261.jpg vector with normalized image vector, restults with 1.0 
dot_261 = np.dot(flat_array_261, flat_normalized_261)
#print(dot_261)

#compute dot product of normalized image vector of img_261 and img_271
array_271 = loaded_images_2['img_271.jpg']
norm_271 = np.linalg.norm(array_271)
normalized_271 = array_271 / norm_271
flat_array_271 = normalized_271.flatten()
flat_normalized_271 = np.array(flat_array_271)
dot_271_261 = np.dot(flat_normalized_271, flat_normalized_261)
#print('Normal dot product w/ 261 and 271 = ', dot_271_261)


'''
#compute the dot product of img_261 with 10 images of 9 from the MNIST set
loaded_images_9 = load_images('trainingSet/9')
print('Dot products with 2 and 9 images:')
total_9 = 0
for i, (key, value) in enumerate(loaded_images_9.items()):
    if i == 10:
        break
    norm = np.linalg.norm(value)
    normalized_vector = value / norm
    flat_vector = normalized_vector.flatten()
    dot_product = np.dot(flat_normalized_261, flat_vector)
    #print('Normal dot product w/ img_261.jpg and ', key, ': ', dot_product)
    total_9 += abs(dot_product)
avg_9 = total_9 / 10
print('Average: ',avg_9 ,'\n')
'''


#print('Average dot product with 2: ', avg_2)
#print('Average dot product with 9: ', avg_9)

loaded_images1 = {}
loaded_images2 = {}
'''
#Tests for cosine_similarity_set
#cosine_similarity_set('img_101.jpg', 2, 9, 20, loaded_images1)
#cosine_similarity_set('img_101.jpg', 2, 5, 20, loaded_images1)

for i in range(10):
    cosine_similarity_set('img_101.jpg', 2, i, 20, loaded_images1) 
#In conclusion cosine similarity isn't very accurate for one image.
'''

#test for cosine_similarity_same_set
print('\n')
cosine_similarity_set('img_101.jpg', 2, 9, 20, loaded_images1)
cosine_similarity_same_set(2, 20, loaded_images2) 