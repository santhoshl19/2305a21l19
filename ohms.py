import streamlit as st
import math

# Define the Elec_Power function
def Elec_Power(V, I, PF):
    phi = math.acos(PF)
    P = V * I * math.cos(phi)/1000
    Q = V * I * math.sin(phi)/1000
    S = V * I/1000
    return P, Q, S

# Streamlit UI
st.title('2305A21L19-PS2')

# Input fields for voltage, current, and power factor
V = st.number_input('Enter Voltage (V) in Volts:', min_value=100.0, step=1.0)
I = st.number_input('Enter Current (I) in Amps:', min_value=10.0, step=1.0)
PF = st.number_input('Enter Power Factor (PF):', min_value=0.90, max_value=1.0, step=0.01)

# Calculate and display results
if V > 0 and I > 0 and PF >= 0 and PF <= 1:
    P, Q, S = Elec_Power(V, I, PF)
    
    st.write(f'Active Power (P): {P:.2f} kWatts')
    st.write(f'Reactive Power (Q): {Q:.2f} kVARs')
    st.write(f'Apparent Power (S): {S:.2f} kVA')
else:
    st.write('Please enter valid input values for voltage, current, and power factor.')
