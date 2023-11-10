import streamlit as st
st.write('Hola mundo!')

# set the app's title
st.title("My first app")

# header
st.header("Roaming the web realms")

# subheader
st.subheader("Streamlit testing")

# markdown
# display text in bold formatting
st.markdown("**Streamlit** is a widely used open-source Python framework, facilitates the creation and deployment of web apps for Machine Learning and Data Science.")
# display text in italic formatting
st.markdown("Visit [Streamlit](https://docs.streamlit.io) to learn more about Streamlit.")

# code block
code = '''
def add(a, b):
    print("a+b = ", a+b)
'''
st.code(code, language='python')

# latex
st.latex('''
(a+b)^2 = a^2 + b^2 + 2*a*b
''')
