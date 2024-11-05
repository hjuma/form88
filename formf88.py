mport streamlit as st
from datetime import datetime

st.title("Kenya Passenger Declaration Form (Form F88)")

st.write("""
This form must be completed by all passengers arriving in Kenya and presented to customs officials.
Please fill in the details below.
""")

# Personal and Travel Information
st.header("Personal and Travel Information")
surname = st.text_input("Surname")
first_name = st.text_input("First Name")
passport_number = st.text_input("Passport Number")
date_of_birth = st.date_input("Date of Birth")
date_of_arrival = st.date_input("Date of Arrival")
country_arriving_from = st.text_input("Country Arriving From")
countries_visited = st.text_area("Countries visited in the last six days")
address_in_kenya = st.text_input("Address in Kenya (e.g., Hotel/Residence)")
email_address = st.text_input("Email Address")
flight_or_vehicle_no = st.text_input("Flight No./Vehicle No./Vessel No")
gender = st.radio("Gender", ["Male", "Female"])
nationality = st.text_input("Nationality")

# Declaration Section
st.header("Declaration of Items")
st.write("Please indicate if you are bringing any of the following items into Kenya:")

animal_products = st.checkbox("Animal or plant products, microbes, biological products, human tissues")
valuable_goods = st.checkbox("Goods valued at or above USD 500 (for residents) or will remain in Kenya (for non-residents)")
spirits = st.checkbox("Spirits exceeding 1 Liter or wine exceeding 2 Liters")
perfumes = st.checkbox("Perfumes/toiletries exceeding 1 Liter (with perfume not over 250ml)")
tobacco_products = st.checkbox("Cigarettes, cigars, or tobacco products exceeding 250 grams")
currency_exceeding_limit = st.checkbox("Currency or monetary instruments exceeding USD 10,000")
commercial_goods = st.checkbox("Goods of commercial value, trade goods, samples, or advertisement products")
filming_equipment = st.checkbox("Filming equipment")
other_articles = st.checkbox("Other articles to declare (firearms, dangerous/prohibited items)")

# Detailed Declaration (if any items are checked)
if any([animal_products, valuable_goods, spirits, perfumes, tobacco_products, currency_exceeding_limit, commercial_goods, filming_equipment, other_articles]):
    st.subheader("Details of Declared Items")
    item_description = st.text_area("Description of Items")
    item_quantity = st.number_input("Quantity", min_value=0, step=1)
    item_value = st.number_input("Value in USD", min_value=0.0, step=0.01)
    remarks = st.text_area("Remarks")

# Declaration Signature
st.write("By submitting, I declare the information provided above is true and accurate to the best of my knowledge.")
passenger_signature = st.text_input("Passenger’s Signature")
signature_date = st.date_input("Date", datetime.now())

# Submit Button
if st.button("Submit"):
    st.success("Form submitted successfully! Please present it to Customs officials upon arrival.")

