import os
import numpy as np

def extractFeatures(mailDir, dictionary):
    files = [os.path.join(mailDir,fi) for fi in os.listdir(mailDir)]

    featuresMatrix = np.zeros((len(files),3000))
    documentID = 0;

    for singleFile in files:
        #start reading all the files
      with open(singleFile) as oneFile:
        for i,line in enumerate(oneFile):
          if i == 2:
            wordsInALine = line.split()
            for word in wordsInALine:
              wordID = 0 #get the wordID
              for i,d in enumerate(dictionary):
                if d[0] == word:
                  wordID = i
                  featuresMatrix[documentID,wordID] = wordsInALine.count(word)
        documentID = documentID + 1
    return featuresMatrix