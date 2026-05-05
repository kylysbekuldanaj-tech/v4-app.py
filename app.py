import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import *

st.set_page_config(page_title="Денсаулық қосымшасы", layout="centered")

st.markdown("""
<style>
body {background-color:#ffe6f0;}
.stButton>button {
    background-color:#ff66b2;
    color:white;
    border-radius:12px;
}
</style>
""", unsafe_allow_html=True)

st.title("💖 Денсаулық қосымшасы")

name=st.text_input("Атың")
age=st.number_input("Жас",10,100)
weight=st.number_input("Салмақ",30,200)
height=st.number_input("Бой",100,220)

if st.button("Есептеу"):
    bmi=calculate_bmi(weight,height)
    cat,color=bmi_category(bmi)

    st.markdown(f"<h3 style='color:{color}'>BMI {bmi:.2f} - {cat}</h3>",unsafe_allow_html=True)
    st.write("💧 Су:",water_intake(weight),"мл")
    st.write("🔥 Калория:",calories_needed(weight),"ккал")

    ideal=ideal_weight(height,age)
    st.success(f"Идеалды салмақ: {ideal} кг")

    diff=abs(weight-ideal)
    st.info(f"Шамамен {int(diff/2)+1} айда жетуге болады")

    st.subheader("🍽 Меню")
    for k,v in meal_plan().items():
        st.write(f"{k}: {v}")

    df=pd.DataFrame([[weight]],columns=["weight"])
    df.to_csv("data.csv",mode="a",header=False,index=False)

try:
    df=pd.read_csv("data.csv")
    st.subheader("📈 Салмақ графигі")
    fig,ax=plt.subplots()
    ax.plot(df["weight"])
    st.pyplot(fig)
except:
    pass

st.subheader("📅 Күнделікті трекер")
water=st.number_input("Ішкен су (мл)",0,5000)
cal=st.number_input("Калория",0,5000)
steps=st.number_input("Қадам",0,50000)

if st.button("Сақтау"):
    df=pd.DataFrame([[water,cal,steps]],columns=["water","cal","steps"])
    df.to_csv("tracker.csv",mode="a",header=False,index=False)
    st.success("Сақталды")

try:
    df=pd.read_csv("tracker.csv")
    st.subheader("📊 Трекер график")
    fig,ax=plt.subplots()
    ax.plot(df["water"],label="Су")
    ax.plot(df["cal"],label="Калория")
    ax.plot(df["steps"],label="Қадам")
    ax.legend()
    st.pyplot(fig)
except:
    pass

st.subheader("🤖 Кеңес")
if steps<5000:
    st.warning("Көбірек қозғалыс жаса")
elif steps>10000:
    st.success("Жақсы белсенділік")