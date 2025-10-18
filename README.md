# 🧠 LLM Text Summarizer

A simple and interactive **Text Summarization App** built using **Large Language Models (LLMs)** from **Hugging Face Transformers** and **Streamlit**.  
It allows users to input large text and generate concise summaries in seconds!

---

## 🚀 Features

- 📝 Summarizes long paragraphs or articles using pre-trained LLMs  
- ⚡ Built with **Streamlit** for an interactive web interface  
- 🤗 Uses Hugging Face’s pre-trained model (facebook/bart-large-cnn) 
- 🔒 Clean, minimal, and beginner-friendly code
- 🔒 Can be run locally without an internet connection (after model download

---

## 🛠️ Tech Stack

| Component | Technology Used |
|------------|------------------|
| Programming Language | Python |
| Framework | Streamlit |
| NLP Library | Hugging Face Transformers |
| Model | `facebook/bart-large-cnn` or `t5-small` |
| Environment | Virtual Environment (venv) |

---

## 📦 Installation & Setup

### 1️⃣ Clone this Repository
```
git clone https://github.com/SahanaReddy06/LLM_Text_Summarizer.git
cd LLM_Text_Summarizer

Create a Virtual Environment
python -m venv venv
venv\Scripts\activate       # On Windows

Install Dependencies
pip install -r requirements.txt

Run the App
streamlit run app.py

```
💡 Future Improvements

-Add multilingual summarization
-Support document upload (PDF, DOCX)
-Provide summary length customization

🧠 How It Works

The LLM Text Summarizer uses a pre-trained Large Language Model (LLM) such as facebook/bart-large-cnn from Hugging Face Transformers to generate concise summaries from long text inputs.

1.** User Input: ** The user enters or pastes a paragraph into the Streamlit interface.
This text is passed to the Hugging Face pipeline() function in your app.py
```
from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
summary = summarizer(input_text, max_length=150, min_length=30, do_sample=False)
```

2. **Tokenization:**The text is converted into tokens (numerical IDs) that the model can understand.This tokenization is handled internally by the model’s tokenizer from Hugging Face.

3. **Encoding & Decoding:**

    - The encoder reads the input text and converts it into a context vector — a representation of meaning.
    -The decoder then generates a shorter version of the text (summary) by predicting the next words step by step.

4. **Output: ** The tokens are converted back into readable text and displayed as the final summary in the app.

Internally, models like BART and T5 use a transformer-based encoder-decoder architecture with self-attention, enabling them to understand context and rephrase information effectively

👩‍💻 Author
-Sahana



