import streamlit as st
import google.generativeai as genai
import time

# 1. Page Configuration & Styling
st.set_page_config(page_title="Toronto Business AI", page_icon="🍁", layout="centered")

st.title("Business AI Consultant")
st.caption("Powered by Gemma")
st.write("---")

# 2. Securely input your API Key in the sidebar
with st.sidebar:
    st.header("🔑 Configuration")
    api_key = st.text_input("Enter Google AI Studio API Key:", type="password")
    st.info("Your API key is processed locally and never stored online.")

# 3. Main Application Interface
st.subheader("What operational bottleneck can I help your business solve today?")
prompt_text = st.text_area(
    label="Describe the business scenario, industry, and goals:",
    placeholder="Example: A boutique clothing store wants to move from manual excel tracking to an automated inventory system..."
)

# 4. Execution Logic with Auto-Retry Capabilities
if st.button("Generate Strategy", type="primary"):
    if not api_key:
        st.error("Please enter your Google AI Studio API key in the sidebar to run the model.")
    elif not prompt_text:
        st.warning("Please type a business scenario first!")
    else:
        with st.spinner("Analyzing operations and generating custom change management roadmap..."):
            
            # Configure the SDK
            genai.configure(api_key=api_key)
            
            # Wrap the input beautifully
            contextual_prompt = f"""
            You are an expert change management and operations consultant specializing in helping small-to-medium businesses.
            
            Analyze the following business scenario and provide 3 quick, practical, low-risk steps they should take this week to optimize operations or prepare staff for transition.
            
            Business Scenario:
            {prompt_text}
            """
            
            # Use a robust 3-strike retry engine to absorb free-tier rate limits
            max_retries = 3
            success = False
            
            for attempt in range(max_retries):
                try:
                    # Leverage the highly optimized and fast 2.0 Flash model architecture
                    model = genai.GenerativeModel('gemini-2.0-flash')
                    response = model.generate_content(contextual_prompt)
                    
                    st.success("Analysis Complete!")
                    st.write(response.text)
                    success = True
                    break # Break the loop on success!
                    
                except Exception as e:
                    # If it's a quota error, wait 4 seconds and try again
                    if "429" in str(e) or "quota" in str(e).lower():
                        if attempt < max_retries - 1:
                            st.warning(f"Server is busy (Free Tier Rate Limit). Retrying in 4 seconds... (Attempt {attempt + 1}/{max_retries})")
                            time.sleep(4)
                        else:
                            st.error("The Free Tier quota limit is temporarily exhausted. Please wait 1 minute before clicking generate again.")
                    else:
                        st.error(f"An unexpected error occurred: {e}")
                        break