import streamlit as st
import google.generativeai as genai
import re

GEMINI_API_KEY = "AIzaSyDCi65n5TeUCk592gPnnXzHZUjgQoDIiAo"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-pro-latest')

def get_travel_recommendations(source, destination):
    prompt = f"""
    You are a travel planning assistant. Provide travel options between {source} and {destination}.
    Include the following modes of transport: cab, train, bus, and flight.
    For each mode, provide:
    1. Estimated cost in Indian Rupees (INR).
    2. Approximate travel time.
    3. Pros and cons of each mode.
    4. Additional travel tips and best time to book.
    
    Format the response in a structured and user-friendly format.
    """
    response = model.generate_content(prompt)
    return response.text

st.title("Wered Travel Planner")
st.write("Plan your travel with AI-powered recommendations!")

col1, col2 = st.columns(2)
with col1:
    source = st.text_input("Enter Source City:")
with col2:
    destination = st.text_input("Enter Destination City:")

st.markdown("---")
st.subheader("🚗 Travel Options")

if st.button("Get Travel Recommendations", type="primary"):
    if source and destination:
        with st.spinner("Fetching travel options..."):
            try:
                recommendations = get_travel_recommendations(source, destination)
                st.success("Travel Recommendations:")
                st.write(recommendations)
                
                cheapest_match = re.search(r"Cheapest Option:\s*(.*?)\n", recommendations, re.DOTALL)
                fastest_match = re.search(r"Fastest Option:\s*(.*?)\n", recommendations, re.DOTALL)
                
                st.markdown("---")
                st.subheader("📌 Summary")
                
                if cheapest_match and fastest_match:
                    cheapest = cheapest_match.group(1)
                    fastest = fastest_match.group(1)
                    col_cheap, col_fast = st.columns(2)
                    with col_cheap:
                        st.markdown(f"**Cheapest Option:** {cheapest}")
                        st.caption("Most Budget-Friendly Option")
                    with col_fast:
                        st.markdown(f"**Fastest Option:** {fastest}")
                        st.caption("Quickest Travel Option")
                else:
                    st.warning("🚨 AI response format is different than expected. Unable to extract Cheapest and Fastest options.")
                
                st.markdown("---")
                st.warning("*Important Note:* Prices are estimates and may vary based on demand, season, and booking time. Always verify with service providers.")
                
                st.subheader("📍 Additional Travel Tips")
                st.write("1. Book early to get the best prices.")
                st.write("2. Compare multiple travel platforms for better deals.")
                st.write("3. Consider layovers to reduce flight costs.")
                st.write("4. Check luggage policies before booking.")
                
                st.markdown("---")
                st.subheader("🛎 Accommodation Recommendations")
                st.write("Explore budget hotels, hostels, or Airbnb options.")
                st.write("Check platforms like OYO, MakeMyTrip, and Booking.com.")
                
                st.markdown("---")
                st.subheader("🍽️ Local Food Suggestions")
                st.write("Try local delicacies and explore top-rated restaurants.")
                st.write("Use Google Maps and food apps like Swiggy and Zomato.")
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter both source and destination.")