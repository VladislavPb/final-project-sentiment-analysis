import pickle


class Review(object):

  def __init__(self):
    with open('vectorizer.pickle', 'rb') as file1:
      self.vect = pickle.load(file1)
    with open('classifier.pickle', 'rb') as file2:
      self.clas = pickle.load(file2)
    self.tone = {'neg': 'negative', 'pos': 'positive'}
  
    
  def prediction(self, text):
    try:
      vectorized = self.vect.transform([text])
      pred = self.clas.predict(vectorized)[0]
      return self.tone[pred]
    except:
      return 'Error. Invalid input'
      