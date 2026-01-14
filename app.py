import streamlit as st

st.set_page_config(
    page_title="Deployed ML Models",
    layout="wide"
)

st.title("Deployed Machine Learning & NLP Models")
st.write(
    "A centralized dashboard showcasing my deployed ML and NLP applications."
)

models = [
    {   
        "name": "Blog: RAG and Small LLMs",
        "description": "Technical article on RAG frameworks and small LLMs in healthcare.",
        "tech": "LLMs, RAG, NLP",
        "url": "https://www.johnsnowlabs.com/the-power-of-small-llms-in-healthcare-a-rag-framework-alternative-to-large-language-models/"
    },
    {
        "name": "Turkish NLP App",
        "description": "Turkish NLP application deployed on Railway.",
        "tech": "NLP, Transformers, Turkish Language",
        "url": "https://turkish-nlp-app-production-451f.up.railway.app/"
    },
    {
        "name": "SiparisEng (HuggingFace Space)",
        "description": "Order understanding and NLP pipeline hosted on Hugging Face Spaces.",
        "tech": "NER, Text Classification, HuggingFace",
        "url": "https://huggingface.co/spaces/bgk/sipariseng"
    },
    {
        "name": "Churn Prediction App",
        "description": "Customer churn prediction system with interactive UI.",
        "tech": "Classification, Feature Engineering",
        "url": "https://bugeki-churn-prediction-streamlit-my-app-cjk7og.streamlit.app/"
    },
    {
        "name": "AutoScout ML Deployment",
        "description": "Car price prediction and analysis application.",
        "tech": "Regression, Data Analysis",
        "url": "https://bugeki-autoscoutdeployment-my-app-s7pttf.streamlit.app/"
    }
]

for model in models:
    with st.container():
        st.subheader(model["name"])
        st.write(model["description"])
        st.caption(f"Tech Stack: {model['tech']}")
        st.markdown(f"🔗 [Open Application]({model['url']})")
        st.divider()
