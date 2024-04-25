
import streamlit as st

# Set the page title
st.title('Harvest Decision Model')

# Use Streamlit's slider widget to get user input
# Input botrytis probability, ranging from 0% to 100%
botrytis = st.slider("Enter botrytis probability as a whole number (e.g., 50 for 50%):", 0, 100, 50) / 100

# Input the probability for no sugar, ranging from 0% to 100%
no_sugar = st.slider("Enter no sugar probability as a whole number:", 0, 100, 33) / 100

# Input the probability for typical sugar level, ranging from 0% to 100%
typical = st.slider("Enter typical sugar probability as a whole number:", 0, 100, 33) / 100

# Input the probability for high sugar level, ranging from 0% to 100%
high_sugar = st.slider("Enter high sugar probability as a whole number:", 0, 100, 34) / 100

# Calculate expected value
E_storm = botrytis * 275000 + (1 - botrytis) * 35000
E_nostorm = no_sugar * 80000 + typical * 117500 + high_sugar * 125000

E_value = 12 * (0.5535 * (0.3225 * E_nostorm + 0.6775 * E_storm) + 0.4465 * (0.16 * E_nostorm + 0.84 * E_storm))

# Display the expected value
st.write(f'The expected value is: {E_value}')

# Determine the recommended action based on E_value
result = E_value - 80000 * 12
if result < 0:
    recommendation = 'Harvest immediately'
elif result > 0:
    recommendation = 'Wait to harvest'
else:
    recommendation = 'Both actions have the same expected value'

# Display the recommended action
st.write(f'Recommended action: {recommendation}')