import streamlit as st
import re
import random

# Set page title
st.set_page_config(page_title="🔐 Password Strength Meter")

# Commonly used weak passwords
blacklist = {"password", "123456", "password123", "12345678", "qwerty", "admin", "letmein", "welcome"}
special_characters = "!@#$%^&*"

def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in blacklist:
        feedback.append("❌ This password is too common.")
        return 1, feedback

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0–9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append(f"❌ Include at least one special character ({special_characters}).")

    return score, feedback

def suggest_strong_password():
    lower = random.choice("abcdefghijklmnopqrstuvwxyz")
    upper = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digit = random.choice("0123456789")
    special = random.choice(special_characters)
    others = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" + special_characters, k=4))
    password_list = list(lower + upper + digit + special + others)
    random.shuffle(password_list)
    return ''.join(password_list)

# --- Streamlit UI ---

st.title("🔐 Password Strength Meter")

password = st.text_input("Enter a password to check", type="password")

if password:
    score, feedback = check_password_strength(password)

    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider improving it.")
    else:
        st.error("❌ Weak Password")

    if feedback:
        st.subheader("💡 Suggestions:")
        for tip in feedback:
            st.write("- " + tip)

    if score < 4:
        if st.button("🔄 Suggest a Strong Password"):
            st.info(f"Suggested Strong Password: `{suggest_strong_password()}`")
