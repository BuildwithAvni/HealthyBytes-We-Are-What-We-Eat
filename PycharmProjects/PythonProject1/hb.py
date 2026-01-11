import streamlit as st
from PIL import Image

st.markdown("""
<style>
/* Base card styling */
div[data-testid="stContainer"]:has(.card-raw) {
    background-color: #e8f5e9;
}

div[data-testid="stContainer"]:has(.card-snack) {
    background-color: #fff3e0;
}

div[data-testid="stContainer"]:has(.card-main) {
    background-color: #e3f2fd;
}

div[data-testid="stContainer"]:has(.card-drink) {
    background-color: #f3e5f5;
}

div[data-testid="stContainer"]:has(.card-sweet) {
    background-color: #fffde7;
}

/* Common card padding & rounding */
div[data-testid="stContainer"] {
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 16px;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Healthy Bytes",
    layout="wide"
)

import streamlit as st
import os
import base64

# Function to convert image to base64
def image_to_base64(image_path):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(BASE_DIR, image_path)
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")


logo_path = "images/wrlogo.png"  # replace with your logo path
logo_base64 = image_to_base64(logo_path)

st.markdown(f"""
<!-- Load Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Roboto&display=swap" rel="stylesheet">
<div style="display: flex; justify-content: center; align-items: center; text-align: center; margin-bottom: 20px;">
    <!-- Logo -->
    <img src="data:image/png;base64,{logo_base64}" width="270" style="margin-right: 20px;" />
    <!-- Text container -->
    <div style="display: flex; flex-direction: column; justify-content: center;">
        <!-- Main title in cursive -->
        <span style="font-family: 'Pacifico', cursive; font-size: 80px; line-height: 1; color: #FF6347;">
            Healthy Bytes
        </span>
        <!-- Subtitle in small caps next to it -->
        <span style="font-family: 'Roboto', sans-serif; font-variant: small-caps; font-size: 40px; color: #555;">
            We Are What We Eat
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

#st.title("🍎🥗 HEALTHY BYTES  🥗🍎")
#st.write("WE ARE WHAT WE EAT")
import streamlit as st
import base64

import streamlit as st
import base64

def set_bg(image_path):
    with open(image_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{data}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


#set_bg("images/b1.jpeg")


left_col, divider_col, right_col = st.columns([2.5, 0.05, 2])
with divider_col:
    st.markdown(
        "<div style='height: 200vh; border-left: 2px solid #cccccc;'></div>",
        unsafe_allow_html=True
    )



recipes = [
        {
            "name": "Tangy mango lassi",
            "serves": 3,
            "time": 30,
            "type": "drink",
            "ingredients": {"Raw mango" : "1 peeled and cubed/grated", "curd" : "2 cups",
                            "cumin seeds": "1.5 tsp" , "black salt" : "1 tsp",
                            "sugar" : "2 tsp" ,"mint leaves" : " 6 - 8 ", "salt" : "to taste"},
            "steps": [
                "Cook the mango with 1/4th cup of water for 1 whistle in a pressure cooker.",
                "Allow it to cool completely",
                "Blend the cooked mango with curd. Add cumin seeds, black salt , sugar and salt. Blend.",
                "Serve chilled with mint leaves on top."

            ],
            "image": "images/tangymangolassi.jpg",
            "imagerotation": -90,
            "imageheight": 350,
            "imagewidth": 200
        },
        {
            "name": "Green Gram Sprout Salad",
            "serves": 3,
            "time": 25,
            "type": "raw",
            "ingredients": {"sprouted green gram" : "1/2 cup", "dates" : "4 seedless,chopped", "rasins" : "2tbsp",
                            "carrot" : "1 - 2 peeled and grated", "coconut" : " 1 tbsp grated", "olive oil" : "a dash",
                            "honey" : "to taste", "lemon juice" : "to taste"
                             },
            "steps": [
                "Mix the sprouts, dates , carrots and coconut together in a deep bowl",
                "In a separate bowl mix lemon juice, olive oil and honey together to make the dressing.",
                "Pour the dressing over the sprouts mixture and mix thoroughly ",
                "Serve"
            ],
            "image": "images/sproutssalad.jpg",
            "imagerotation": 0,
            "imageheight": 150,
            "imagewidth": 200
        },
        {
            "name": "Strawberry Milkshake",
            "serves": 1,
            "time": 10,
            "type": "drink",
            "ingredients": {"strawberry" : "5 big", "Milk" : "1 cup boiled and cooled", "sugar/jaggery" : "1 tsp" },
            "steps": [
                "Boil and cool the milk.",
                "Blend all ingredients.",
                "Serve chilled. ",
            ],
            "image": "images/broccolicorn.jpg",
            "imagerotation": 0,
            "imageheight": 200,
            "imagewidth": 200
        },
        {
            "name": "Pressure Baked Brocolli Corn",
            "serves": 3,
            "time": 15,
            "type": "snack",
            "ingredients": {"herb butter" : "2 tsp", "Brocolli" : "1 chopped into big florets", "sweet corn" : "2 cups",
                            "cheese" : "2 tbsp (optional)",
                             },
            "steps": [
                "Heat the cooker and put the butter in it.",
                "Cover the base with brocolli.",
                "Wash sweet corn and put it on top of the brocolli. ",
                "Add cheese(optional)",
                "Cook on high flame for 1 whistle",
                "Immediately release pressure ",
                "Mix and serve"
            ],
            "image": "images/broccolicorn.jpg",
            "imagerotation": 0,
            "imageheight": 200,
            "imagewidth": 200
        },
        {
            "name": "Jaggery Coconut Laddoo",
            "serves": 8,
            "time": 45,
            "type": "sweet",
            "ingredients": {"Grated coconut" : "1.5 cup", "Jaggery" : "3/4 cup, broken", "Ghee" : "1 tsp"},
            "steps": [
                "Add 1/4 cup water to grated jaggery and melt it on low flame.",
                "Heat a heavy bottomed pan and add 1 tsp ghee.",
                "Add coconut and fry for about 2-3 minutes on a medium flame, stirring constantly.",
                "Mix the jaggery syrup with the coconut.",
                "Continue to cook for about 3 minutes till all the moisture evaporates."
                "Off the stove and let it cool for about 5 minutes."
                "Grease your palm and roll into lemon sized balls."
            ],
            "image": "images/jaggerycoconutladdoo.jpg",
            "imagerotation": 0,
            "imageheight": 200,
            "imagewidth": 200
        }
]

def display_recipe(recipe):

    color_map = {
        "raw": "#e8f5e9",
        "snack": "#fff3e0",
        "main": "#e3f2fd",
        "drink": "#f3e5f5",
        "sweet": "#fffde7"
    }

    header_color = color_map.get(recipe["type"], "#eeeeee")

    with st.container(border=True):

        # COLOURED HEADER STRIP (THIS ALWAYS WORKS)
        st.markdown(
            f"""
            <div style="
                background-color: {header_color};
                padding: 10px;
                border-radius: 8px;
                font-weight: bold;
                font-size: 18px;
            ">
                {recipe["name"].upper()} • {recipe["type"].upper()}
            </div>
            """,
            unsafe_allow_html=True
        )

        left_col, right_col = st.columns([3, 1])

        with left_col:
            st.write(f"**Serves:** {recipe['serves']}")
            st.write("**Ingredients:**")
            for item, val in recipe["ingredients"].items():
                st.write(f"- {item} - {val}")

        with right_col:
            st.markdown(f"**🕒 {recipe['time']} mins**")
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            img_path = os.path.join(BASE_DIR, recipe["image"])
            img = Image.open(img_path)
            img = img.rotate(recipe["imagerotation"], expand=True)
            img = img.resize((recipe["imagewidth"], recipe["imageheight"]))
            st.image(img)

        st.write("**Steps:**")
        for i, step in enumerate(recipe["steps"], start=1):
            st.write(f"{i}. {step}")


def filter_recipes():
    filtered = recipes

    if search_name:
        filtered = [
            r for r in filtered
            if search_name.lower() in r["name"].lower()
        ]

    if recipe_type != "All":
        filtered = [
            r for r in filtered
            if r["type"] == recipe_type
        ]

    if time_limit != "Any":
        limit = int(time_limit.split()[0])
        filtered = [
            r for r in filtered
            if r["time"] <= limit
        ]

    if selected_ingredients:
        filtered = [
            r for r in filtered
            if all(ing in r["ingredients"] for ing in selected_ingredients)
        ]

    return filtered


with right_col:
    st.header("Search & Filters")

    recipe_names = list(r["name"] for r in recipes)
    search_name = st.selectbox("Search recipe name", recipe_names)

    recipe_type = st.selectbox(
        "Type",
        ["All", "snack", "raw", "main", "drink", "sweet"]
    )

    time_limit = st.selectbox(
        "Time taken",
        ["Any", "10 mins or less", "20 mins or less", "30 mins or less"]
    )

    all_ingredients = sorted(
        list({ing for r in recipes for ing in r["ingredients"]})
    )

    selected_ingredients = st.multiselect(
        "Include ingredients",
        all_ingredients
    )

    submit = st.button("Search")


with left_col:
    st.header("Recipes")

    if submit:
        results = filter_recipes()
    else:
        results = recipes

    if results:
        for recipe in results:
            display_recipe(recipe)
    else:
        st.warning("No recipes found 😢")

with right_col:
    st.markdown("---")
    st.subheader("About Me")

    # Create two columns: image on left, text on right
    col1, col2 = st.columns([1, 2])  # ratio: 1 part image, 2 parts text

    with col1:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(BASE_DIR, "images", "cb.png")
        st.image(img_path, width=150)

    with col2:
        st.write("""
        Hi! 👋  
        I am a 7th-grade student passionate about:
        - Healthy food 🥗
        - Coding 💻
        - Crochet 🧶
        - Creativity 🎨
        """)
