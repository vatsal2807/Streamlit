import streamlit as st
st.title("CALCULATOR")

no1 = st.text_input("Enter 1st No:")
no2 = st.text_input("Enter 2nd No:")

sum = st.checkbox("SUM")
sub = st.checkbox("SUB")
mul = st.checkbox("MUL")
div = st.checkbox("DIV")
if(st.button("click me")):

    if (sum):
         st.balloons()
         c = int(no1)+int(no2)
         st.write("ANSWER : ", c)
        #st.balloons()
    elif(sub):
         st.balloons()
         d=int(no1)-int(no2)
         st.write("ANSWER :",d)
    elif(mul):
         st.balloons()
         e=int(no1)*int(no2)
         st.write("ANSWER :",e)
    elif(div):
         st.balloons()
         f=int(no1)/int(no2)
         st.write("ANSWER :",f)
    else :
         st.warning("Please select an option to continue with calculation!!!!")
        
else:
          st.text("ANSWER:")