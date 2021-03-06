
import pickle

#doc_new = ['obama is running for president in 2016']

#function to run for prediction
def detect_fake_news(var):    
    #retrieving the best model for prediction call
    load_model = pickle.load(open('model/final_model.sav', 'rb'))
    prediction = load_model.predict([var])
    prob = load_model.predict_proba([var])

    return (prediction[0],prob[0][1])


if __name__ == '__main__':
    
    var = input("Please enter the news text you want to verify: ")
    print("You entered: " + str(var))
    detect_fake_news(var)