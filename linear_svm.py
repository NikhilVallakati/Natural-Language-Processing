from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from local_time import LocalTime

# Support Vector Machines (SVM)
class Linear_SVM:
    @staticmethod
    def get_best_hyperparameter(X_train, y_train, y_val, X_val):
        best_accuracy = 0.0
        best_c = 0.0
        for c in [0.01, 0.05, 0.25, 0.5, 1]:
            svm = LinearSVC(C=c)
            svm.fit(X_train, y_train)
            accuracy_ = accuracy_score(y_val, svm.predict(X_val))
            if accuracy_ > best_accuracy:
                best_accuracy = accuracy_
                best_c = c
            print ("---SVM Accuracy for C=%s: %s" % (c, accuracy_))

        print(LocalTime.get(), "best hyperparameter c = ", best_c)
        return best_c