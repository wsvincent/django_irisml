import joblib
import numpy as np
from django.shortcuts import render
from .models import IrisPrediction  # new

# Load the trained model
model = joblib.load("iris.joblib")


def predict(request):
    prediction = None
    form_data = {}  # To store user inputs

    if request.method == "POST":
        try:
            # Store form inputs
            form_data = {
                "sepal_length": request.POST.get("sepal_length"),
                "sepal_width": request.POST.get("sepal_width"),
                "petal_length": request.POST.get("petal_length"),
                "petal_width": request.POST.get("petal_width"),
            }

            # Convert inputs to float and make a prediction
            features = np.array([[float(v) for v in form_data.values()]])
            prediction = model.predict(features)[0]

            # Save prediction to database
            IrisPrediction.objects.create(
                sepal_length=form_data["sepal_length"],
                sepal_width=form_data["sepal_width"],
                petal_length=form_data["petal_length"],
                petal_width=form_data["petal_width"],
                prediction=prediction,
            )

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render(
        request, "predict.html", {"prediction": prediction, "form_data": form_data}
    )
