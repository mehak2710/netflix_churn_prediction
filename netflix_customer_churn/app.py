import streamlit as st
import numpy as np
from model import train_model

st.set_page_config(page_title="Customer Churn Prediction")

st.title("📉 Customer Churn Prediction App")
st.write("Predict whether a customer will leave the platform")

model, scaler, accuracy = train_model()

# Show model accuracy
st.info(f"📊 Model Accuracy: **{accuracy*100:.2f}%**")

watch_time = st.slider("Watch Time (hours)", 0, 300, 100)
last_login = st.slider("Days Since Last Login", 0, 30, 5)
monthly_charges = st.slider("Monthly Charges (₹)", 100, 1000, 400)

if st.button("Predict Churn"):
    input_data = np.array([[watch_time, last_login, monthly_charges]])
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)[0][1]

    st.write(f"🔍 **Churn Risk:** {probability*100:.2f}%")

    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to CHURN")

        st.markdown("### 💡 Business Recommendation")
        st.write(
            "- Offer a **personalized discount**\n"
            "- Send **re-engagement notifications**\n"
            "- Recommend content based on watch history"
        )
    else:
        st.success("✅ Customer is likely to STAY")

        st.markdown("### 💡 Business Recommendation")
        st.write(
            "- Offer **loyalty rewards** or cashback\n"
            "- Promote **premium plan upgrades**\n"
            "- Encourage **referrals** with incentives"
        )
