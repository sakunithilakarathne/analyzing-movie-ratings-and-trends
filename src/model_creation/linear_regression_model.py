import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.metrics import classification_report, roc_auc_score, accuracy_score



def linear_regression_model(x_test,x_train,y_test,y_train):
    """
    Linear Regression Model
    """
    # Initialize and train the Linear Regression model
    model = LinearRegression()
    model.fit(x_train, y_train)

    # Make predictions
    y_prediction = model.predict(x_test)

    model_filename = "Models/linear_regression_model.pkl"
    pickle.dump(model, open(model_filename, 'wb'))
    print(f"Model saved to {model_filename}")

    # Evaluate the model
    mae = mean_absolute_error(y_test, y_prediction)
    mse = mean_squared_error(y_test, y_prediction)
    r2 = r2_score(y_test, y_prediction)

    # Print evaluation metrics
    print("\n\n\n\nLinear Regression Model Evaluation:")
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"R-squared (R²): {r2}")


