import streamlit as st 
import joblib
import numpy as np

model = joblib.load("IDS.pkl")
scaler= joblib.load("scaler.pkl")

st.title("🚨 Intrusion Detection System")
st.write(" This system detects network attacks using machine learning model")

st.header("Enter Network Traffic Data")

duration = st.number_input("Duration",min_value=0)
st.markdown("❗Here 0 for TCP, 1 for UDP,2 for ICMP")
protocol_type = st.selectbox("Protocol Type",options=[0,1,2])
service = st.number_input("Service", min_value=0)
flag = st.number_input("Flag", min_value=0)
src_bytes = st.number_input("Source Bytes", min_value=0)
dst_bytes = st.number_input("Destination Bytes", min_value=0)
count = st.number_input("Connection Count", min_value=0)
srv_count = st.number_input("Service Count", min_value=0)
serror_rate = st.number_input("Serror Rate", min_value=0.0, max_value=1.0)
srv_serror_rate = st.number_input("Service Serror Rate", min_value=0.0, max_value=1.0)
same_srv_rate = st.number_input("Same Service Rate", min_value=0.0, max_value=1.0)
diff_srv_rate = st.number_input("Different Service Rate", min_value=0.0, max_value=1.0)

#We only take input of 12 features and the other 29 features are set to zero
#These are not crucial for basic ids .
input_features = np.array([[duration, protocol_type, service, flag, src_bytes, dst_bytes,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, count, srv_count, serror_rate, srv_serror_rate,
                            0, 0, same_srv_rate, diff_srv_rate, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0]])

scaled_features = scaler.transform(input_features)

if st.button("🔎 Detect Intrusion"):
    prediction = model.predict(scaled_features)[0]
    result = "🔴 Attack Detected!" if prediction == 1 else "🟢 Normal Traffic"
    st.subheader(result)