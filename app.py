import streamlit as st
import openai

# Title and description
st.title("Personalized Meal Prep Assistant")
st.write("Use GPT to generate personalized meal prep plans!")

# Input for meal preferences
st.write("Please provide the following information:")
num_days = st.slider("Number of Days for Meal Prep", min_value=1, max_value=7, value=5)
num_meals_per_day = st.slider("Number of Meals per Day", min_value=1, max_value=5, value=3)
cuisine_options = ["None", "American", "Asian", "Barbecue", "Brazilian", "British", "Cajun & Creole", "Caribbean", 
                   "Chinese", "Cuban", "French", "German", "Greek", "Hawaiian", "Indian", "Irish", "Italian", "Japanese", 
                   "Korean", "Mediterranean", "Mexican", "Middle Eastern", "Moroccan", "Peruvian", "Portuguese", 
                   "Russian", "Southern", "Spanish", "Swedish", "Thai", "Turkish", "Vietnamese"]
cuisine = st.multiselect("Cuisine Preference", cuisine_options)
excluded_ingredients = st.text_input("Excluded Ingredients", placeholder="Non-veg, allergies, dairy, gluten etc..")
# List of fitness goals
goals = st.multiselect("Fitness Goals", ["Weight Loss", "Muscle Gain", "Maintain Weight", "Improve Cardiovascular Health", 
                                        "Increase Strength", "Improve Flexibility", "Improve Endurance", 
                                        "Enhance Athletic Performance", "Reduce Stress", "Improve Sleep", 
                                        "Improve Overall Wellness"])
# List of special needs in diet
special_needs = st.multiselect("Special Needs", ["Diabetic Diet", "Low Sodium Diet", "Gluten-Free Diet",
                                                  "Vegan Diet", "Vegetarian Diet", "Paleo Diet",
                                                  "Ketogenic Diet", "Low Carb Diet", "High Protein Diet",
                                                  "Low Fat Diet", "None"])
num_snacks_per_day = st.slider("Number of Snacks per Day", min_value=0, max_value=3, value=1)
activity_level_options = ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"]
activity_level = st.selectbox("Physical Activity Level", activity_level_options)

# Input for user profile
age = st.number_input("Age", min_value=18, max_value=120, step=1)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
height = st.number_input("Height (in cm)", min_value=130, max_value=200, step=1)
weight = st.number_input("Weight (in kg)", min_value=30, max_value=200, step=1)

# Generate meal prep plan using GPT
if st.button("Generate Meal Prep Plan"):
    st.write("Here's your personalized meal prep plan:")
    input_text = f"""Generate a {num_days}-day personalised meal prep plan consisting of {num_meals_per_day} meals per day and {num_snacks_per_day} snacks per day, focusing on {', '.join(cuisine)} cuisine, excluding {excluded_ingredients}. Keep in mind the following:

Age: {age}
Gender: {gender}
Height: {height} cm
Weight: {weight} kg
Goals: {', '.join(goals)}. 
Physical activity level: {activity_level}.
Special Needs: {special_needs}

Provide serving size and calories. Maintain a daily average of atleast 1400 calories. Output as markdown table"""
    # with st.spinner("Loading.."):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": input_text}]
        )
    meal_prep_plan = response['choices'][0]['message']['content']
    st.markdown(meal_prep_plan)
    st.markdown("Contact your dietician before starting a personalised meal plan. If you do not have a dietician [click here](https://www.linkedin.com/in/faziha-ziyan-623323256/)")