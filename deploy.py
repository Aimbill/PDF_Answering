#cdqa pipeline.to('cpu')
#joblib.dump(cdqa_pipeline, ' /models/bert_qa_custom.joblib')
#streamlit run --server.enableCORS false qaapp.py
import joblib 
import requests 
import streamlit as st

st. set_option('deprecation.showfileUploaderEncoding', False)
st. title("Question Answering Webapp*)
st.text("what would you like to know about Amazon today?")

@st.cache(allow_output_nutation=True)
def load model():
model=joblib. load( 'bert_qa_custon.joblib')
return model

with st.spinner ('Loading Model Into Memory....'):
model = load_model()
text = st. text_input('Enter your questions here..')
if text:
st .write("Response :")
with st.spinner ('Searching for answers.....'):
prediction = model. predict (text)
st.write('answer: ()' format(prediction(e]))
st.write('title: ()'. format (prediction(1]))
st.write( 'paragraph: ()' format(prediction[2]))
st.write("")
