from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle

def random_forest_model(x_test,x_train,y_test,y_train):
    """
    Random Forest Regressor model
    """
    # Initialize and train the Random Forest model
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(x_train, y_train)

    # Make predictions
    y_pred_rf = rf_model.predict(x_test)

    model_filename = "Models/random_forest_model.pkl"
    pickle.dump(rf_model, open(model_filename, 'wb'))
    print(f"Model saved to {model_filename}")

    # Evaluate the model
    mae_rf = mean_absolute_error(y_test, y_pred_rf)
    mse_rf = mean_squared_error(y_test, y_pred_rf)
    r2_rf = r2_score(y_test, y_pred_rf)

    print("Random Forest Model Evaluation:")
    print(f"Mean Absolute Error (MAE): {mae_rf}")
    print(f"Mean Squared Error (MSE): {mse_rf}")
    print(f"R-squared (R²): {r2_rf}")
    print()