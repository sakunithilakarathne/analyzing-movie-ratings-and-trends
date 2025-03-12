from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle

def xg_boost_model(x_test,x_train,y_test,y_train):
    # Initialize and train the XGBoost model
    xgb_model = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
    xgb_model.fit(x_train, y_train)

    # Make predictions
    y_pred_xgb = xgb_model.predict(x_test)

    model_filename = "Models/xg_boost_model.pkl"
    pickle.dump(xgb_model, open(model_filename, 'wb'))
    print(f"Model saved to {model_filename}")

    # Evaluate the model
    mae_xgb = mean_absolute_error(y_test, y_pred_xgb)
    mse_xgb = mean_squared_error(y_test, y_pred_xgb)
    r2_xgb = r2_score(y_test, y_pred_xgb)

    print("XGBoost Model Evaluation:")
    print(f"Mean Absolute Error (MAE): {mae_xgb}")
    print(f"Mean Squared Error (MSE): {mse_xgb}")
    print(f"R-squared (R²): {r2_xgb}")