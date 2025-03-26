import streamlit as st
from PIL import Image

# ✅ Must come before any other Streamlit commands
st.set_page_config(page_title="Fresh Hearth Dashboard", layout="wide")

# Then show logo or title
logo = Image.open("brandpulselogo.png")
with st.sidebar:
    st.image(logo, width=150)

import pandas as pd
import plotly.express as px
import random

# Sidebar - Customized Profile Section
st.sidebar.markdown("### 👤 Your Profile")
name = st.sidebar.text_input("Name", "Sathwick")
goal = st.sidebar.selectbox("Primary Wellness Goal", ["Improve Gut Health", "Lose Weight", "Gain Muscle", "Increase Energy", "Better Sleep"])
level = st.sidebar.radio("Your Current Level", ["Beginner", "Wellness Warrior", "Health Hero", "Nutrition Ninja"])

st.sidebar.markdown("---")
st.sidebar.markdown("📅 Weekly Streak: **6 Days**")
st.sidebar.markdown("🔥 Calories Burned: **1,750 kcal**")
st.sidebar.markdown("💧 Water Intake: **10L this week**")

# Main title
st.title("🥗 Fresh Hearth - Personalized Nutrition Dashboard")

# Points and Progress
st.subheader("🌟 Your Health Points")
st.metric("Total Points", "🏅 1,230")
st.progress(0.75)  # 75% towards next reward tier

# Rewards Section
st.subheader("🎁 Rewards Center")
st.markdown("- ✅ Completed 7-day meal tracking")
st.markdown("- 🔓 Unlocked: Hydration Hero Badge")
st.markdown("- 🎯 3 days left to complete 'Meatless Monday Challenge'")

# Weekly Feedback Quiz
st.subheader("🧠 Weekly Feedback Quiz")
with st.expander("Take Quiz"):
    st.write("**Which nutrient is most important for muscle growth?**")
    answer = st.radio("Choose one:", ["Protein", "Vitamin C", "Calcium"], index=None, key="quiz_q1")
    if answer:
        if answer == "Protein":
            st.success("Correct! 🏋️‍♀️ Protein is essential for muscle growth.")
            st.balloons()
        else:
            st.error("Oops! That's not quite right. Try again next week!")

# Meal Tracking Chart
st.subheader("📊 Your Weekly Calorie Intake")
data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Calories": [1800, 1900, 2000, 1750, 1850, 2200, 2100]
})
fig = px.line(data, x="Day", y="Calories", markers=True, title="Calorie Intake Over the Week")
st.plotly_chart(fig)

# Leaderboard Section
st.subheader("🏆 Weekly Leaderboard")
leaderboard_data = pd.DataFrame({
    "Name": ["Rohan", "Nipun", "Ashick", "Sathwick", "Salaar"],
    "Points": [3200, 2800, 1230, 950, 730]
})
leaderboard_data = leaderboard_data.sort_values(by="Points", ascending=False).reset_index(drop=True)
st.table(leaderboard_data)

# Smart Insights
st.subheader("💡 Smart Insights")
st.info("🔎 You tend to consume higher calories on weekends. Consider lighter dinner options.")
st.info("🥗 You skipped breakfast 3 times this week. Want to set a morning reminder?")

# Tip of the Day
tips = [
    "Eat more fiber today 🍎",
    "Hydrate often 💧",
    "Take a 10-min walk 🏃‍♂️",
    "Try adding a plant-based meal 🌱",
    "Limit sugary snacks 🍬"
]
st.warning(f"💬 Tip of the Day: {random.choice(tips)}")

# Footer
st.markdown("---")
st.caption("Fresh Hearth - Empowering Healthy Living Through Data")
