from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data
        gender = request.form.get("gender", "").strip()
        age = request.form.get("age", "").strip()
        height = request.form.get("height", "").strip()
        weight = request.form.get("weight", "").strip()
        
        # Validate that all required fields are provided
        if not (age and height and weight and gender):
            return render_template("result.html", pred="Please fill all required fields.")
        
        # Convert inputs to proper data types
        age = int(age)  # Convert age to integer
        height = float(height)  # Height in cm
        weight = float(weight)  # Weight in kg
        
        # Validate realistic ranges for metric values
        if not (100 <= height <= 250):
            return render_template("result.html", pred="Please enter a realistic height (in cm) between 100 and 250.")
        if not (20 <= weight <= 300):
            return render_template("result.html", pred="Please enter a realistic weight (in kg) between 20 and 300.")
        if not (1 <= age <= 120):
            return render_template("result.html", pred="Please enter a realistic age between 1 and 120.")
        
        # Convert height from centimeters to meters for BMI calculation
        height_m = height / 100
        
        # Calculate BMI and round to 2 decimal places
        BMI = round(weight / (height_m * height_m), 2)
        
        # Determine BMI category
        if BMI < 16:
            category = "Severely Underweight"
        elif 16 <= BMI < 18.5:
            category = "Underweight"
        elif 18.5 <= BMI < 25:
            category = "Normal"
        elif 25 <= BMI < 30:
            category = "Overweight"
        elif 30 <= BMI <34:
            category = "Obese"
        else:
            category = "extramely Obese"
        
        # Calculate healthy weight range (BMI 18.5 to 24.9)
        healthy_lower = round(18.5 * (height_m * height_m), 2)
        healthy_upper = round(24.9 * (height_m * height_m), 2)
        
        # Prepare the result message
        prediction = (
            f"<strong>Age:</strong> {age} years<br>"
            f"<strong>Gender:</strong> {gender.capitalize()}<br><br>"
            f"<strong>Calculated BMI:</strong> {BMI}<br>"
            f"<strong>Category:</strong> {category}<br><br>"
            f"<strong>Healthy weight range for your height:</strong> {healthy_lower} kg - {healthy_upper} kg"
        )
        
        return render_template("result.html", pred=prediction)
    
    except ValueError:
        return render_template("result.html", pred="Invalid input. Please enter valid numerical values.")
    except Exception as e:
        return render_template("result.html", pred=f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
