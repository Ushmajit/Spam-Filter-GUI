import numpy as np
from MakeDictionary import makeDictionary
from ExtractFeatures import extractFeatures
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.svm import SVC, NuSVC, LinearSVC
from sklearn.metrics import confusion_matrix

from tkinter import *
from tkinter.filedialog import askdirectory

window = Tk()


window.geometry("500x500")


model2 = LinearSVC()
def askdTrainDirectory():
    trainDir = askdirectory()

    t1.insert(END, "Training Directory Selected\n ")
    t1.insert(END, "Creating Dictionary Please Wait...\n")
    # Create a dictionary of words with its frequency
    global dictionary
    dictionary = makeDictionary(trainDir)
    t1.insert(END, "Dictionary Created\nIntializing Feature Extraction Process\nPlease Wait\n")
    print("Dictionary")
    # Prepare feature vectors per training mail and its labels
    train_labels = np.zeros(702)
    train_labels[351:701] = 1
    train_matrix = extractFeatures(trainDir, dictionary)
    t1.insert(END, "Feature Extraction Completed...\nInitializing modules for testing..\n")
    print("Complete")
    t1.insert(END, "Training Multinomial NB\n")
    global model1
    model1 = MultinomialNB()
    model1.fit(train_matrix, train_labels)
    t1.insert(END, "Multinomial NB Training Complete")
    print(trainDir)


l1 = Label(window,text='Select the training directory')
l1.config(font=("Courier", 12))
l1.pack()

b1 = Button(window,text='Train', command=askdTrainDirectory)
b1.config(height = 1, width = 13)
b1.pack()


def askTestDirectory():
    t1.insert(END, "Test Directory Selected\n")
    t1.insert(END, "Initializing testing process\n")
    testDir = askdirectory()
    print(dictionary)
    test_matrix = extractFeatures(testDir, dictionary)
    test_labels = np.zeros(2)
    test_labels[1] = 1
    t1.insert(END, "Starting Predicting\n")
    result1 = model1.predict(test_matrix)
    t1.insert(END,result1)
    for i in np.nditer (result1, op_flags=['readwrite']):
        if(np.equal(0,i)):
            t1.insert(END, "Not a Spam\n")
        else:
            t1.insert(END, "Spam\n")
    print(testDir)

l2 = Label(window,text='Select the testing directory')
l2.config(font=("Courier", 12))
l2.pack()

b2 = Button(window,text='Test', command = askTestDirectory)
b2.config(height = 1, width = 13)
b2.pack()

l4 = Label(window,text='Status')
l4.config(font=("Courier", 12))
l4.pack()

t1 = Text(window, height = 100 , width = 200)
t1.pack()

window.mainloop()
