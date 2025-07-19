
import streamlit as st

st.title("🤖 ArogyaAI: Rural Health Assistant Demo")

st.write("Speak or type your symptoms in simple language (e.g., 'I have cough and fever') and ArogyaAI will provide basic health advice.")

symptom_input = st.text_input("🩺 Describe your symptoms:")

def check_symptoms(symptom_text):
    symptom_text = symptom_text.lower()
    if "cough" in symptom_text and "fever" in symptom_text:
        return "🧠 It may be flu or an early respiratory infection. Please rest, stay hydrated, and consult a doctor if symptoms worsen."
    elif "chest pain" in symptom_text:
        return "🚨 Chest pain can be serious. Please seek medical attention immediately."
    elif "rash" in symptom_text or "skin" in symptom_text:
        return "🧴 It might be a skin infection or allergy. Keep the area clean and dry. Consult a doctor if it spreads."
    elif "headache" in symptom_text:
        return "💆 You might be experiencing a tension headache or dehydration. Rest and drink fluids."
    else:
        return "ℹ️ Sorry, I couldn't recognize the condition. Please try to describe the symptoms in more detail."

if symptom_input:
    response = check_symptoms(symptom_input)
    st.success(response)

if st.button("📞 Connect to Doctor"):
    st.info("This feature will connect to a real doctor in the full version. (Demo only)")

uploaded_file = st.file_uploader("📷 Upload a photo of the symptom (optional):", type=["jpg", "png"])
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.info("Image uploaded successfully. (Image analysis coming soon)")
