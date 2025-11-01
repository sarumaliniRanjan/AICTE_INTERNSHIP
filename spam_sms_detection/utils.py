"""
Utility functions for SMS Spam Detection System
"""

import streamlit as st
import pickle
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
from config import MODEL_PATH, VECTORIZER_PATH

@st.cache_resource
def download_nltk_data():
    """Download required NLTK data with error handling"""
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('punkt_tab', quiet=True)
        nltk.download('stopwords', quiet=True)
        return True
    except Exception as e:
        st.error(f"Error downloading NLTK data: {e}")
        return False

@st.cache_resource
def load_models():
    """Load ML models with comprehensive error handling"""
    try:
        if not os.path.exists(VECTORIZER_PATH):
            st.error(f"Vectorizer file '{VECTORIZER_PATH}' not found.")
            return None, None
        
        if not os.path.exists(MODEL_PATH):
            st.error(f"Model file '{MODEL_PATH}' not found.")
            return None, None
        
        with open(VECTORIZER_PATH, 'rb') as f:
            vectorizer = pickle.load(f)
        
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        
        return vectorizer, model
    
    except Exception as e:
        st.error(f"Error loading models: {str(e)}")
        return None, None

@st.cache_data
def preprocess_text(text):
    """
    Advanced text preprocessing pipeline
    
    Args:
        text (str): Input text to preprocess
        
    Returns:
        str: Preprocessed text
    """
    if not text or not text.strip():
        return ""
    
    try:
        # Initialize stemmer
        stemmer = PorterStemmer()
        
        # Convert to lowercase
        text = text.lower()
        
        # Tokenize
        tokens = nltk.word_tokenize(text)
        
        # Filter alphanumeric tokens only
        tokens = [token for token in tokens if token.isalnum()]
        
        # Remove stopwords and punctuation
        stop_words = set(stopwords.words('english'))
        tokens = [
            token for token in tokens 
            if token not in stop_words and token not in string.punctuation
        ]
        
        # Apply stemming
        tokens = [stemmer.stem(token) for token in tokens]
        
        return " ".join(tokens)
    
    except Exception as e:
        st.error(f"Error in text preprocessing: {str(e)}")
        return ""

def get_prediction_confidence(model, vector_input):
    """
    Get prediction confidence score if model supports it
    
    Args:
        model: Trained ML model
        vector_input: Vectorized input
        
    Returns:
        float or None: Confidence score
    """
    try:
        if hasattr(model, 'predict_proba'):
            probabilities = model.predict_proba(vector_input)[0]
            return max(probabilities)
        return None
    except Exception:
        return None

def validate_input(text):
    """
    Enhanced input validation with detailed feedback
    
    Args:
        text (str): Input text
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not text:
        return False, "Please enter a message to analyze."
    
    if not text.strip():
        return False, "Message cannot be empty or contain only whitespace."
    
    stripped_text = text.strip()
    
    if len(stripped_text) < 2:
        return False, "Message is too short for meaningful analysis (minimum 2 characters)."
    
    if len(text) > 1000:
        return False, f"Message is too long ({len(text)} characters). Please limit to 1000 characters."
    
    # Check for potentially problematic characters
    if len([c for c in text if c.isalnum() or c.isspace()]) < len(text) * 0.5:
        return False, "Message contains too many special characters for reliable analysis."
    
    return True, ""

def format_confidence_score(confidence):
    """
    Format confidence score for display with enhanced visual indicators
    
    Args:
        confidence (float): Confidence score
        
    Returns:
        str: Formatted confidence string with emoji and description
    """
    if confidence is None:
        return "❓ N/A"
    
    percentage = confidence * 100
    if percentage >= 95:
        return f"🟢 {percentage:.1f}% (Excellent)"
    elif percentage >= 85:
        return f"🟢 {percentage:.1f}% (Very High)"
    elif percentage >= 75:
        return f"🟡 {percentage:.1f}% (High)"
    elif percentage >= 65:
        return f"🟠 {percentage:.1f}% (Medium)"
    elif percentage >= 55:
        return f"🔴 {percentage:.1f}% (Low)"
    else:
        return f"🔴 {percentage:.1f}% (Very Low)"