import numpy as np
from MakeDictionary import makeDictionary
from ExtractFeatures import extractFeatures
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.svm import SVC, NuSVC, LinearSVC
from sklearn.metrics import confusion_matrix

# Create a dictionary of words with its frequency
print("Creating Dictionary Please Wait...........")
train_dir = r'C:\Users\Admin\Documents\sayan debnath blog\spam\train-mails'
dictionary = makeDictionary(train_dir)

print("Dictionary Created..........Intializing Feature Extraction Process.... Please Wait")
# Prepare feature vectors per training mail and its labels

train_labels = np.zeros(702)
train_labels[351:701] = 1
train_matrix = extractFeatures(train_dir, dictionary)
print("Feature Extraction Completed...Initializing modules for testing..")
# Training SVM and Naive bayes classifier

model1 = MultinomialNB()
model2 = LinearSVC()
model1.fit(train_matrix,train_labels)
#plt.plot(train_matrix)
#plt.show()
print("Training MultinomialNB........ ")
model2.fit(train_matrix,train_labels)
print("Training LinearSVC........ ")
# Test the unseen mails for Spam
test_dir = 'test-mails'
test_matrix = extractFeatures(test_dir, dictionary)
test_labels = np.zeros(2)
test_labels[1] = 1
print("Starting Testing process.....")
result1 = model1.predict(test_matrix)
print("50% completed testing.....")
result2 = model2.predict(test_matrix)
print(result1)
print (confusion_matrix(test_labels,result1))



#print (test_labels,result2)