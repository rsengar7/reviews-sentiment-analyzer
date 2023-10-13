try:
    # MAKE ALL THE MODULES AVAILABLE
    import sys
    import gc  # Garbage Collector

    import mysql.connector as MySQLdb

    import pandas as pd

    from sklearn.svm import SVC

    from sklearn.model_selection import train_test_split
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics import accuracy_score, confusion_matrix

except Exception as e:
    # PLEASE IMPORT THE MODULES FIRST
    #print("Enable to import all the necessary Modules---", e)
    sys.exit()


class Classifier:
    def __init__(self) -> None:
        self.review_data = pd.read_csv("reviews.csv")
        self.tfidfvec = TfidfVectorizer(lowercase=True)

    def __str__(self):
        return self.__class__.__name__

    def cl_dump(self):
        ''' Classifier for the Polarity Check and Sentiment Analyzer '''

        from sklearn.svm import SVC

        self.review_data = self.review_data.fillna("")

        X = self.review_data['keyword']
        y = self.review_data['rating'].apply(lambda x: 1 if x == 'pos' else 0)

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

        # Vectorize the text data using TdIdf Vectorization
        X_train_vectorized = self.tfidfvec.fit_transform(X_train)
        X_test_vectorized = self.tfidfvec.transform(X_test)

        # Support Vector Machine Classifier
        clf = SVC(kernel='linear')
        clf.fit(X_train_vectorized, y_train)

        y_pred = clf.predict(X_test_vectorized)

        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        print(f'Accuracy: {accuracy:.2%}')
        print()

        # Generate a confusion matrix
        conf_matrix = confusion_matrix(y_test, y_pred)
        print('Confusion Matrix:')
        print(conf_matrix)
        print("*"*100)

        return clf

    def sentiment(self, review, clf=None):
        if not isinstance(review, list):
            review = [review]

        if clf is None:
            clf = self.cl_dump()

        # Convert the Review into vectorized form for machine learning model
        review_vectorized = self.tfidfvec.transform(review)

        review_pred = clf.predict(review_vectorized)

        return review_pred[0]
        # prob_dist = clf2.prob_classify(tokn)
        # return prob_dist.prob("pos") - prob_dist.prob("neg")

obj = Classifier()
# obj.cl_dump()
review = "I have done something cool"
print(obj.sentiment(review))