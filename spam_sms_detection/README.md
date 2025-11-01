# 📱 SMS Spam Detection System

An advanced machine learning-powered web application for detecting spam SMS messages using Natural Language Processing techniques.

## 🚀 Features

- **Real-time SMS Classification**: Instantly classify messages as spam or legitimate
- **Advanced NLP Processing**: Text preprocessing with tokenization, stemming, and stopword removal
- **Interactive Web Interface**: Modern, responsive Streamlit-based UI
- **Confidence Scoring**: Shows prediction confidence when available
- **Sample Message Testing**: Pre-loaded examples for quick testing
- **Error Handling**: Robust error handling and user feedback
- **Performance Optimized**: Cached models and preprocessing for faster predictions

## 🛠️ Technology Stack

- **Frontend**: Streamlit with custom CSS styling
- **Backend**: Python with scikit-learn
- **NLP**: NLTK for text preprocessing
- **ML Model**: Pre-trained classification model
- **Vectorization**: TF-IDF vectorizer

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager

## 🔧 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sarumaliniRanjan/AICTE_INTERNSHIP.git
   cd AICTE_INTERNSHIP/spam_sms_detection
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure model files exist**:
   - `model.pkl` - Trained classification model
   - `vectorizer.pkl` - TF-IDF vectorizer
   - `spam.csv` - Training dataset

## 🚀 Usage

1. **Start the application**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Use the application**:
   - Enter an SMS message in the text area
   - Click "Analyze Message" to get predictions
   - Try sample messages for quick testing
   - View processed text and confidence scores

## 📊 How It Works

1. **Text Preprocessing**: 
   - Convert to lowercase
   - Tokenize into words
   - Remove punctuation and non-alphanumeric characters
   - Filter out stopwords
   - Apply stemming to reduce words to root forms

2. **Vectorization**: 
   - Transform preprocessed text using TF-IDF vectorizer

3. **Classification**: 
   - Use trained ML model to predict spam/ham
   - Calculate confidence scores

4. **Results Display**: 
   - Show classification result with visual indicators
   - Display confidence percentage
   - Provide processed text for transparency

## 🎨 UI Features

- **Modern Design**: Clean, professional interface with custom CSS
- **Responsive Layout**: Works on desktop and mobile devices
- **Color-coded Results**: Green for legitimate, red for spam messages
- **Interactive Sidebar**: Information about the system and how it works
- **Sample Testing**: Quick access to test messages
- **Error Handling**: User-friendly error messages and warnings

## 📁 Project Structure

```
spam_sms_detection/
├── app.py              # Main Streamlit application
├── model.pkl           # Trained ML model
├── vectorizer.pkl      # TF-IDF vectorizer
├── spam.csv           # Training dataset
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── .gitignore         # Git ignore file
```

## 🔍 Model Performance

The system uses a pre-trained machine learning model that has been optimized for SMS spam detection with high accuracy and low false positive rates.

## 🛡️ Security Features

- Input validation and sanitization
- Error handling for malformed inputs
- Safe file loading with proper exception handling
- No execution of user-provided code

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is part of the AICTE Internship program.

## 🆘 Support

If you encounter any issues or have questions, please check the error messages in the application or review the console output for debugging information.

## 🔮 Future Enhancements

- [ ] Multi-language support
- [ ] Batch processing for multiple messages
- [ ] Model retraining interface
- [ ] Performance metrics dashboard
- [ ] API endpoint for integration
- [ ] Message history and analytics