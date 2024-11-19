from models.json_schema import GeneratedJSON
from pydantic import ValidationError
from sklearn.linear_model import LinearRegression
import numpy as np

class ValidationAgent:
    def __init__(self):
        self.regression_model = LinearRegression()

    def validate_json(self, json_data: GeneratedJSON) -> bool:
        try:
            # Pydantic validation
            json_data.validate()
            # Additional validation with a simple regression model as an example
            input_data = np.array([[len(json_data.key), len(json_data.value)]])
            expected_output = np.array([1])  # Example expected output for demonstration
            self.regression_model.fit(input_data, expected_output)  # Simple fitting step
            prediction = self.regression_model.predict(input_data)

            if prediction[0] != expected_output[0]:
                print(f"Regression-based validation failed. Predicted: {prediction[0]}")
                return False

            print("Validation passed with regression analysis.")
            return True
        except ValidationError as e:
            print(f"Validation Error: {e}")
            return False
