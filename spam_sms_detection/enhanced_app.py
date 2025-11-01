"""
Enhanced SMS Spam Detection System v2.0
Advanced AI-powered spam detection with modern UI and animations
"""

import streamlit as st
import time
from config import *
from utils import *

# Configure page with enhanced settings
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state=INITIAL_SIDEBAR_STATE,
    menu_items={
        'Get Help': 'https://github.com/sarumaliniRanjan/AICTE_INTERNSHIP',
        'Report a bug': 'https://github.com/sarumaliniRanjan/AICTE_INTERNSHIP/issues',
        'About': f"{APP_NAME} v{APP_VERSION} - {APP_DESCRIPTION}"
    }
)

# Inject baby blue and white theme CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

.stApp {
    background: linear-gradient(135deg, #87CEEB 0%, #B0E0E6 25%, #E0F6FF 50%, #FFFFFF 100%);
    font-family: 'Inter', sans-serif;
    color: #2C3E50;
}

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    background: rgba(255, 255, 255, 0.95);
    border-radius: 20px;
    margin-top: 2rem;
    box-shadow: 0 20px 40px rgba(135, 206, 235, 0.3);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(135, 206, 235, 0.2);
}

.modern-card {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(240, 248, 255, 0.9));
    border-radius: 15px;
    box-shadow: 0 8px 25px rgba(135, 206, 235, 0.2);
    padding: 1.5rem;
    border: 1px solid rgba(135, 206, 235, 0.3);
    transition: all 0.3s ease;
    animation: fadeInUp 0.6s ease-out;
    color: #2C3E50;
}

.modern-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 35px rgba(135, 206, 235, 0.4);
    border-color: rgba(135, 206, 235, 0.5);
}

.gradient-text {
    background: linear-gradient(135deg, #4682B4, #87CEEB, #2C3E50);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 600;
}

.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    border-radius: 50px;
    font-weight: 500;
    font-size: 0.9rem;
}

.status-success {
    background: linear-gradient(135deg, rgba(135, 206, 235, 0.2), rgba(176, 224, 230, 0.2));
    color: #4682B4;
    border: 1px solid rgba(135, 206, 235, 0.5);
}

.progress-bar {
    width: 100%;
    height: 8px;
    background: rgba(135, 206, 235, 0.2);
    border-radius: 4px;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #4682B4, #87CEEB);
    border-radius: 4px;
    transition: width 0.5s ease;
}

/* Override Streamlit default styles for baby blue theme */
.stTextArea > div > div > textarea {
    background-color: rgba(255, 255, 255, 0.9) !important;
    color: #2C3E50 !important;
    border: 2px solid rgba(135, 206, 235, 0.5) !important;
    border-radius: 10px !important;
}

.stTextArea > div > div > textarea:focus {
    border-color: #4682B4 !important;
    box-shadow: 0 0 0 2px rgba(135, 206, 235, 0.3) !important;
}

.stSelectbox > div > div > select {
    background-color: rgba(255, 255, 255, 0.9) !important;
    color: #2C3E50 !important;
    border: 2px solid rgba(135, 206, 235, 0.5) !important;
    border-radius: 10px !important;
}

.stButton > button {
    background: linear-gradient(135deg, #4682B4, #87CEEB) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #87CEEB, #4682B4) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(135, 206, 235, 0.4) !important;
}

/* Sidebar styling */
.css-1d391kg {
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.95), rgba(240, 248, 255, 0.9)) !important;
    border-right: 1px solid rgba(135, 206, 235, 0.3) !important;
}

/* Success/Error messages */
.stSuccess {
    background: linear-gradient(135deg, rgba(34, 197, 94, 0.1), rgba(22, 163, 74, 0.1)) !important;
    border: 1px solid rgba(34, 197, 94, 0.3) !important;
    color: #16a34a !important;
}

.stError {
    background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(220, 38, 38, 0.1)) !important;
    border: 1px solid rgba(239, 68, 68, 0.3) !important;
    color: #dc2626 !important;
}

.stWarning {
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(217, 119, 6, 0.1)) !important;
    border: 1px solid rgba(245, 158, 11, 0.3) !important;
    color: #d97706 !important;
}

.stInfo {
    background: linear-gradient(135deg, rgba(70, 130, 180, 0.1), rgba(135, 206, 235, 0.1)) !important;
    border: 1px solid rgba(70, 130, 180, 0.3) !important;
    color: #4682B4 !important;
}

/* Text color overrides */
.stMarkdown, .stText, p, div, span {
    color: #2C3E50 !important;
}

/* Sidebar text colors */
.css-1d391kg .stMarkdown, .css-1d391kg p, .css-1d391kg div {
    color: #2C3E50 !important;
}

@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-30px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes slideInLeft {
    from { opacity: 0; transform: translateX(-50px); }
    to { opacity: 1; transform: translateX(0); }
}

@keyframes slideInRight {
    from { opacity: 0; transform: translateX(50px); }
    to { opacity: 1; transform: translateX(0); }
}

@keyframes slideIn {
    from { opacity: 0; transform: translateX(-20px); }
    to { opacity: 1; transform: translateX(0); }
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}
</style>
""", unsafe_allow_html=True)

# Loading screen
def show_loading_screen():
    """Display an animated loading screen"""
    loading_placeholder = st.empty()
    
    with loading_placeholder.container():
        st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 60vh;">
            <div style="font-size: 4rem; margin-bottom: 2rem; animation: pulse 2s infinite;">🛡️</div>
            <div style="font-size: 2rem; font-weight: 600; color: #3b82f6; margin-bottom: 1rem;">SMS Spam Detector</div>
            <div style="color: #64748b; margin-bottom: 2rem;">Initializing AI systems...</div>
            <div class="progress-bar" style="width: 300px;">
                <div class="progress-fill" style="width: 0%; animation: loading 3s ease-in-out forwards;"></div>
            </div>
        </div>
        <style>
        @keyframes loading {
            0% { width: 0%; }
            33% { width: 30%; }
            66% { width: 70%; }
            100% { width: 100%; }
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Simulate loading time
    time.sleep(3)
    loading_placeholder.empty()

# Initialize session state
if 'app_loaded' not in st.session_state:
    show_loading_screen()
    st.session_state.app_loaded = True

# Initialize NLTK and models
@st.cache_resource
def initialize_system():
    """Initialize the spam detection system"""
    with st.spinner("🔄 Loading AI models..."):
        nltk_success = download_nltk_data()
        if not nltk_success:
            st.error("❌ Failed to initialize NLTK data")
            st.stop()
        
        vectorizer, model = load_models()
        if vectorizer is None or model is None:
            st.error("❌ Failed to load ML models")
            st.stop()
        
        return vectorizer, model

vectorizer, model = initialize_system()

# Baby blue themed header
st.markdown("<div style='text-align: center;'><h1 class='gradient-text' style='font-size: 3.5rem; margin-bottom: 1rem;'>🛡️ SMS Spam Detector</h1></div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: #4682B4; margin-bottom: 2rem; font-size: 1.2rem; font-weight: 500;'>🤖 Advanced AI-powered SMS classification system</div>", unsafe_allow_html=True)

# Feature highlights with baby blue theme
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='modern-card' style='text-align: center;'><div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>🎯</div><strong style='color: #4682B4; font-size: 1.1rem;'>99% Accurate</strong><br><small style='color: #5A6C7D; font-size: 0.9rem;'>High Precision Detection</small></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='modern-card' style='text-align: center;'><div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>⚡</div><strong style='color: #4682B4; font-size: 1.1rem;'>Lightning Fast</strong><br><small style='color: #5A6C7D; font-size: 0.9rem;'>Real-time Analysis</small></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='modern-card' style='text-align: center;'><div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>🔒</div><strong style='color: #4682B4; font-size: 1.1rem;'>Secure</strong><br><small style='color: #5A6C7D; font-size: 0.9rem;'>Privacy Protected</small></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Baby blue themed sidebar
with st.sidebar:
    st.markdown("<div style='text-align: center;'><h2 style='color: #4682B4; font-weight: 600;'>🤖 AI Assistant</h2><p style='color: #5A6C7D; font-weight: 500;'>Powered by Machine Learning</p></div>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='color: #2C3E50;'>📊 System Status</h3>", unsafe_allow_html=True)
    st.markdown("<div class='status-badge status-success' style='margin: 0.5rem 0;'>🟢 Models Loaded</div>", unsafe_allow_html=True)
    st.markdown("<div class='status-badge status-success' style='margin: 0.5rem 0;'>🟢 NLTK Ready</div>", unsafe_allow_html=True)
    st.markdown("<div class='status-badge status-success' style='margin: 0.5rem 0;'>🟢 System Online</div>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='color: #2C3E50;'>🔄 AI Pipeline</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style='color: #2C3E50; line-height: 1.8;'>
    1. 🧹 <span style='color: #4682B4; font-weight: 600;'>Text Cleaning</span><br>
    2. ✂️ <span style='color: #4682B4; font-weight: 600;'>Tokenization</span><br>
    3. 🔍 <span style='color: #4682B4; font-weight: 600;'>Filtering</span><br>
    4. 🌱 <span style='color: #4682B4; font-weight: 600;'>Stemming</span><br>
    5. 📊 <span style='color: #4682B4; font-weight: 600;'>Vectorization</span><br>
    6. 🎯 <span style='color: #4682B4; font-weight: 600;'>Classification</span>
    </div>
    """, unsafe_allow_html=True)

# Main content area with enhanced layout
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    # Message input section
    st.markdown("<div class='modern-card' style='text-align: center; margin-bottom: 2rem;'><h3 style='color: #4682B4; font-weight: 600;'>📝 Message Analysis Center</h3><p style='color: #5A6C7D; font-weight: 500;'>Enter your SMS message below for instant AI-powered spam detection</p></div>", unsafe_allow_html=True)
    
    # Enhanced text input
    input_sms = st.text_area(
        "📱 SMS Message:",
        height=120,
        placeholder="Type or paste your SMS message here...\n\nExample:\n• 'Hi, how are you doing today?'\n• 'URGENT! You've won $1000!'",
        help="Enter any SMS message to check if it's spam or legitimate"
    )
    
    # Character counter with visual indicator
    char_count = len(input_sms) if input_sms else 0
    char_percentage = (char_count / MAX_TEXT_LENGTH) * 100
    char_color = "#ef4444" if char_count > MAX_TEXT_LENGTH else "#10b981" if char_count > 0 else "#64748b"
    
    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; align-items: center; margin: 0.5rem 0;">
        <div class="progress-bar" style="flex: 1; margin-right: 1rem;">
            <div class="progress-fill" style="width: {min(char_percentage, 100)}%; 
                 background: {'#ef4444' if char_count > MAX_TEXT_LENGTH else '#3b82f6'};"></div>
        </div>
        <div style="color: {char_color}; font-size: 0.9rem; font-weight: 500;">
            {char_count}/{MAX_TEXT_LENGTH}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Sample messages section
    st.markdown("#### 🧪 Try Sample Messages")
    st.markdown("Quick test with pre-loaded examples from different categories")
    
    selected_sample = st.selectbox(
        "🎯 Choose a sample message:",
        ["Select sample..."] + list(SAMPLE_MESSAGES.keys()),
        help="Select from various message types to test the AI classifier"
    )
    
    if selected_sample != "Select sample...":
        preview_text = SAMPLE_MESSAGES[selected_sample]
        message_type = "🚨 Likely Spam" if any(word in preview_text.upper() for word in ["URGENT", "WIN", "FREE", "CLICK", "WINNER"]) else "✅ Likely Safe"
        
        st.info(f"**📋 Preview:** {message_type}")
        st.markdown(f"*\"{preview_text[:150]}{'...' if len(preview_text) > 150 else ''}\"*")
        
        if st.button("✨ Use This Sample", type="secondary", use_container_width=True):
            st.session_state.sample_message = SAMPLE_MESSAGES[selected_sample]
            st.rerun()
    
    # Use sample message if selected
    if 'sample_message' in st.session_state:
        input_sms = st.session_state.sample_message
        del st.session_state.sample_message
    
    # Enhanced prediction button
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🔍 Analyze Message", type="primary", use_container_width=True):
        # Input validation
        is_valid, error_message = validate_input(input_sms)
        
        if not is_valid:
            st.error(f"⚠️ {error_message}")
        else:
            # Analysis with progress indicator
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                # Step 1: Preprocessing
                status_text.text("🧹 Cleaning and preprocessing text...")
                progress_bar.progress(20)
                time.sleep(0.5)
                
                transformed_sms = preprocess_text(input_sms)
                
                if not transformed_sms:
                    st.warning("⚠️ Message contains no meaningful content after preprocessing.")
                else:
                    # Step 2: Vectorization
                    status_text.text("📊 Converting text to numerical features...")
                    progress_bar.progress(60)
                    time.sleep(0.5)
                    
                    vector_input = vectorizer.transform([transformed_sms])
                    
                    # Step 3: Prediction
                    status_text.text("🎯 Running AI classification...")
                    progress_bar.progress(90)
                    time.sleep(0.5)
                    
                    result = model.predict(vector_input)[0]
                    confidence = get_prediction_confidence(model, vector_input)
                    
                    progress_bar.progress(100)
                    status_text.text("✅ Analysis complete!")
                    time.sleep(0.5)
                    
                    # Clear progress indicators
                    progress_bar.empty()
                    status_text.empty()
                    
                    # Enhanced results display
                    if result == 1:
                        # Spam result
                        st.markdown("""
                        <div style="background: linear-gradient(135deg, #ef4444, #dc2626); 
                                    color: #ffffff;
                                    padding: 2rem; border-radius: 20px; text-align: center;
                                    box-shadow: 0 15px 35px rgba(239, 68, 68, 0.3);
                                    margin: 2rem 0; animation: slideInLeft 0.8s ease-out;">
                            <div style="font-size: 4rem; margin-bottom: 1rem;">🚨</div>
                            <div style="font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">SPAM DETECTED!</div>
                            <div style="font-size: 1.1rem; opacity: 0.9;">This message appears to be spam</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.error("🚨 **High Risk:** This message shows strong characteristics of spam. Avoid clicking links or providing personal information.")
                    else:
                        # Ham result  
                        st.markdown("""
                        <div style="background: linear-gradient(135deg, #10b981, #059669);
                                    color: #ffffff;
                                    padding: 2rem; border-radius: 20px; text-align: center;
                                    box-shadow: 0 15px 35px rgba(16, 185, 129, 0.3);
                                    margin: 2rem 0; animation: slideInRight 0.8s ease-out;">
                            <div style="font-size: 4rem; margin-bottom: 1rem;">✅</div>
                            <div style="font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">LEGITIMATE MESSAGE</div>
                            <div style="font-size: 1.1rem; opacity: 0.9;">This message appears to be safe</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.success("✅ **Safe:** This message appears to be legitimate and safe.")
                    
                    # Confidence display
                    if confidence:
                        confidence_text = format_confidence_score(confidence)
                        confidence_percentage = confidence * 100
                        
                        st.markdown(f"""
                        <div class="modern-card" style="text-align: center; margin: 2rem 0;">
                            <h4 style="color: #1e293b; margin-bottom: 1rem;">🎯 Confidence Analysis</h4>
                            <div style="font-size: 2rem; margin-bottom: 0.5rem;">{confidence_text}</div>
                            <div class="progress-bar" style="margin: 1rem auto; max-width: 300px;">
                                <div class="progress-fill" style="width: {confidence_percentage}%;"></div>
                            </div>
                            <div style="color: #64748b; font-size: 0.9rem;">
                                AI Confidence: {confidence_percentage:.1f}%
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Detailed analysis
                    with st.expander("🔬 Detailed Analysis Report", expanded=False):
                        col_stats1, col_stats2 = st.columns(2)
                        
                        with col_stats1:
                            st.markdown("#### 📊 Message Statistics")
                            reduction_pct = ((len(input_sms) - len(transformed_sms)) / len(input_sms) * 100) if len(input_sms) > 0 else 0
                            
                            st.markdown(f"""
                            <div class="modern-card">
                                <div style="display: flex; justify-content: space-between; margin: 0.8rem 0;">
                                    <span>📏 Original Length:</span>
                                    <strong>{len(input_sms)} chars</strong>
                                </div>
                                <div style="display: flex; justify-content: space-between; margin: 0.8rem 0;">
                                    <span>🔤 Processed Length:</span>
                                    <strong>{len(transformed_sms)} chars</strong>
                                </div>
                                <div style="display: flex; justify-content: space-between; margin: 0.8rem 0;">
                                    <span>📝 Word Count:</span>
                                    <strong>{len(transformed_sms.split()) if transformed_sms else 0} words</strong>
                                </div>
                                <div style="display: flex; justify-content: space-between; margin: 0.8rem 0;">
                                    <span>📉 Size Reduction:</span>
                                    <strong>{reduction_pct:.1f}%</strong>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with col_stats2:
                            st.markdown("#### 🎯 Classification Details")
                            prediction_label = "SPAM" if result == 1 else "HAM"
                            prediction_color = "#ef4444" if result == 1 else "#10b981"
                            
                            confidence_display = f"{confidence:.2%}" if confidence else 'N/A'
                            st.markdown(f"""
                            <div class="modern-card">
                                <div style="display: flex; justify-content: space-between; margin: 0.8rem 0;">
                                    <span>🏷️ Classification:</span>
                                    <strong style="color: {prediction_color};">{prediction_label}</strong>
                                </div>
                                <div style="display: flex; justify-content: space-between; margin: 0.8rem 0;">
                                    <span>📈 Confidence:</span>
                                    <strong>{confidence_display}</strong>
                                </div>
                                <div style="display: flex; justify-content: space-between; margin: 0.8rem 0;">
                                    <span>⚡ Processing:</span>
                                    <strong>Real-time</strong>
                                </div>
                                <div style="display: flex; justify-content: space-between; margin: 0.8rem 0;">
                                    <span>🔒 Privacy:</span>
                                    <strong>Protected</strong>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Text comparison
                        st.markdown("#### 📝 Text Processing Comparison")
                        col_orig, col_proc = st.columns(2)
                        
                        with col_orig:
                            st.markdown("**Original Message:**")
                            st.markdown(f"""
                            <div style="background: #f8fafc; padding: 1.5rem; border-radius: 15px; 
                                        border: 2px solid #e2e8f0; font-family: monospace; 
                                        white-space: pre-wrap; line-height: 1.5;">
{input_sms}
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with col_proc:
                            st.markdown("**Processed Text:**")
                            st.markdown(f"""
                            <div style="background: #1e293b; color: #e2e8f0; padding: 1.5rem; 
                                        border-radius: 15px; font-family: monospace; 
                                        white-space: pre-wrap; line-height: 1.5;">
{transformed_sms if transformed_sms else 'No meaningful content after processing'}
                            </div>
                            """, unsafe_allow_html=True)
                            
            except Exception as e:
                progress_bar.empty()
                status_text.empty()
                st.error(f"❌ Error during analysis: {str(e)}")
                st.info("💡 Please try again or contact support if the issue persists.")

# Enhanced footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div class="modern-card" style="text-align: center; margin-top: 4rem; background: linear-gradient(135deg, #f8fafc, #e2e8f0);">
    <div style="font-size: 1.5rem; font-weight: 600; color: #1e293b; margin-bottom: 1rem;">
        🛡️ {APP_NAME}
    </div>
    <div style="display: flex; justify-content: center; gap: 3rem; margin: 2rem 0; flex-wrap: wrap;">
        <div style="display: flex; align-items: center; gap: 0.5rem; color: #64748b;">
            <span>🤖</span> <span>AI Powered</span>
        </div>
        <div style="display: flex; align-items: center; gap: 0.5rem; color: #64748b;">
            <span>⚡</span> <span>Real-time</span>
        </div>
        <div style="display: flex; align-items: center; gap: 0.5rem; color: #64748b;">
            <span>🔒</span> <span>Secure</span>
        </div>
        <div style="display: flex; align-items: center; gap: 0.5rem; color: #64748b;">
            <span>🎯</span> <span>Accurate</span>
        </div>
    </div>
    <div style="color: #64748b; font-size: 0.9rem; margin-top: 1rem;">
        Version {APP_VERSION} | Built with ❤️ using Streamlit & Machine Learning<br>
        {DEVELOPER} | {APP_DESCRIPTION}
    </div>
</div>
""", unsafe_allow_html=True)