"""
Configuration file for SMS Spam Detection System
"""

# Model file paths
MODEL_PATH = "model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"
DATASET_PATH = "spam.csv"

# UI Configuration
PAGE_TITLE = "SMS Spam Detector"
PAGE_ICON = "📱"
LAYOUT = "wide"
INITIAL_SIDEBAR_STATE = "expanded"

# App Metadata
APP_NAME = "SMS Spam Detection System"
APP_VERSION = "2.0.0"
APP_DESCRIPTION = "Advanced AI-powered SMS spam detection with real-time analysis"
DEVELOPER = "AICTE Internship Project"

# Enhanced sample messages for comprehensive testing
SAMPLE_MESSAGES = {
    "👋 Friendly Message": "Hi! How are you doing today? Would you like to meet for coffee this weekend?",
    "🚨 Prize Scam": "URGENT! You've won £1000! Click here to claim your prize now! Limited time offer expires in 1 hour!",
    "🏦 Phishing Attack": "ALERT: Your bank account has been compromised. Click this link immediately to secure your account or it will be closed.",
    "📅 Business Appointment": "Your appointment with Dr. Smith is confirmed for tomorrow at 2 PM. Please arrive 10 minutes early.",
    "💝 Personal Message": "Thanks for the wonderful evening! The dinner was amazing. Let's do it again soon!",
    "📱 Tech Scam": "WINNER! You have been selected to receive a FREE iPhone 15! Text CLAIM to 12345 now! Don't miss out!",
    "🏪 Legitimate Promotion": "Hi John, your order #12345 has been shipped and will arrive tomorrow. Track your package at our website.",
    "⚠️ Fake Emergency": "EMERGENCY: Your credit card has been used for $500 purchase. If this wasn't you, call 555-SCAM immediately!",
    "🎓 Educational Reminder": "Reminder: Your assignment is due tomorrow at 11:59 PM. Please submit it through the online portal.",
    "💰 Lottery Fraud": "Congratulations! You've won $50,000 in the international lottery! Send $100 processing fee to claim your prize!"
}

# Text preprocessing settings
REMOVE_STOPWORDS = True
APPLY_STEMMING = True
MIN_TEXT_LENGTH = 2
MAX_TEXT_LENGTH = 1000
MIN_MEANINGFUL_CHARS_RATIO = 0.5

# Enhanced UI Colors and Styling
COLORS = {
    "primary": "#3b82f6",
    "secondary": "#8b5cf6",
    "spam": "#ef4444",
    "ham": "#10b981",
    "warning": "#f59e0b",
    "info": "#06b6d4",
    "success": "#22c55e",
    "error": "#ef4444",
    "background": "#f8fafc",
    "surface": "#ffffff",
    "text_primary": "#1e293b",
    "text_secondary": "#64748b",
    "border": "#e2e8f0",
    "gradient_start": "#667eea",
    "gradient_end": "#764ba2"
}