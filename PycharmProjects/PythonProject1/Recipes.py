import streamlit as st
import base64

def set_background(image_path):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("images/cb.png")
st.title("🍎🥗HEALTHY BYTES 🥗🍎")



st.write("Welcome to my healthy recipes app!")
st.write("made by me ❤️")
recipes = {
    "Fruit salad": {
        "ingredients": [ "banana", "apple", "cucumber"],
        "steps": ["chop the fruits", "mix in the bowl"],
        "funfact": "Its a salad"
    },
    "Strawberry milkshake": {
        "ingredients": ["sugary strawberry", "milk"],
        "steps": ["put strawberry in mixer", "add milk and grind it"],
        "funfact": "Its a milkshake"
    }
}

if "mode" not in st.session_state:
    st.session_state["mode"] = "all"

main, side = st.columns([5, 2])
with main:
    st.header("Recipes")

with side:
    st.header("Search & Filters")

with main:
    if st.session_state["mode"] == "all":
        st.write("printing all recipes")
    elif st.session_state["mode"] == "name":
        st.write("printing recipe with name")
    elif st.session_state["mode"] == "type":
        st.write("printing recipe with type")
    elif st.session_state["mode"] == "time":
        st.write("printing recipe with time")
    elif st.session_state["mode"] == "ingredients":
        st.write("printing recipe with include ingredients")



recipe_name = st.selectbox(
    "Select recipe name 🙂",
    list(recipes.keys())
)
recipe = recipes[recipe_name]

st.subheader(recipe_name)
#st.image("images/back.png")
st.write(recipe["steps"][0])
st.write(recipe["funfact"])
#st.write("➡️ Ingredients ")
st.markdown ("### ➡️ Ingredients")
for ingredient in recipes[recipe_name]["ingredients"]:
    st.write("- ", ingredient)

st.write("➡️ Steps ")
count = 1
for step in recipes[recipe_name]["steps"]:
    st.write(f"     {count}. {step}")
    count = count + 1
#st.write("🌟Fun Fact:" , recipes[recipe_name]["funfact"])
#st.divider()
if st.button("🌟show fun fact"):
    st.success(recipes[recipe_name]["funfact"])
