import joblib as jb
import gradio as gr
from pydantic import BaseModel

# 1. Load the trained model
model = jb.load('frauddetection.pkl')

# 2. Define the input data schema using Pydantic BaseModel
class InputData(BaseModel):
    Year: int
    Month: int
    UseChip: int
    Amount: int
    MerchantName: int
    MerchantCity: int
    MerchantCountry: int
    mcc: int
   

# 3. Define the prediction function
def predict(year, month, use_chip, amount, merchant_name, merchant_city, merchant_country, mcc):
    # Perform the prediction using the loaded model
    prediction = model.predict([[year, month, use_chip, amount, merchant_name, merchant_city, merchant_country, mcc]])[0]  # Replace ... with the rest of the features

    # Convert the prediction to a string (or any other format you prefer)
    result = "Fraud" if prediction == 1 else "Genuine"

    return result

# 4. Create a Gradio interface
iface = gr.Interface(
    fn=predict,
    inputs=[
        gr.components.Number(label="Year"),
        gr.components.Number(label="Month"),
        gr.components.Number(label="UseChip"),
        gr.components.Number(label="Amount"),
        gr.components.Number(label="MerchantName"),
        gr.components.Number(label="MerchantCity"),
        gr.components.Number(label="MerchantCountry"),
        gr.components.Number(label="mcc"),
        # Add the rest of the input features as individual Gradio input components
    ],
    outputs=gr.components.Textbox(),
    title="Credit Card Fraud Detection Web App"
)

# 5. Launch the Gradio interface
iface.launch()
