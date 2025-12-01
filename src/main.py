# Import necessary libraries
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

if __name__ == '__main__':
    # Load the Wine dataset
    wine = load_wine()
    X, y = wine.data, wine.target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Logistic Regression model
    model = LogisticRegression(max_iter=10000, random_state=42)
    model.fit(X_train, y_train)

    # Save the model to a file
    joblib.dump(model, 'wine_model.pkl')
    
    print("The model training was successful")
