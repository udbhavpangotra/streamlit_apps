import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image


image = Image.open('pen.jpg')
body_part_image = Image.open("bodyparts.jpg")

st.title("Penguins")
st.markdown("***")
st.image(image)

st.markdown("***")
# import our data
df = pd.read_csv("data.csv")
st.write("**The default data is provided by Palmer LTER. The data we have has observations about", len(df.species.unique()), "different kinds of penguins, for the years between ", df.year.min(), "and", df.year.max(), ".", "\n The data has ",
         df.shape[0], " rows and ", df.shape[1], " columns**")
st.markdown("***")
st.markdown(
    '''
    The definition for the columns in the dataset is as follows : 
- **Species**: penguin species that are present in the dataset
- **Culmen_length_mm**: culmen length (mm)
- **Culmen_depth_mm**: culmen depth (mm)
- **Flipper_length_mm**: flipper length (mm)
- **Body_mass_g**: body mass (g)
- **Island**: island name 
- **Sex**: penguin sex
    '''
)
st.markdown("***")

st.markdown('''
            **Anatomy Explained :**
            \n **Culmen : ** The culmen is "the upper ridge of a bird's beak"\n
**Flippers : **  Penguins wings are called flippers. They are flat, thin, and broad with a long, tapered shape and a blunt, rounded tip''')

# st.image(body_part_image)
st.markdown("***")
st.text('''
        \n
        \n
        \n
        ''')


st.markdown('''**The distribution of the species in the dataset** 
            \n As we can see 
            Adelie occupies around 44% of the total, while Gentoo has around 36%, the rest around 20% is occupied by Chinstrap''')


labels = ['Adelie', 'Gentoo', 'Chinstrap']
sizes = [152, 124, 68]
colors = ["orange", "teal", "blueviolet"]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        startangle=90, colors=["orange", "teal", "blueviolet"])
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)

st.markdown("***")

st.markdown('''
            As we can see we have equal distribution of males and females for Adelie and Chinstraps, while for Gentoo we have a few more males.
            '''
            )
labels = ["Female Adelie", "Male Adelie", "Female Gentoo",
          "Male Gentoo", "Female Chinstrap", "Male Chinstrap"]
colors = ["orange", "darkorange",
          "cadetblue", "teal", "indigo", "blueviolet"]
sizes = [73, 73, 58, 61, 34, 34]
fig, ax = plt.subplots()
ax.pie(sizes, radius=1, autopct='%1.1f%%',
       colors=colors,
       labels=labels, startangle=90)
ax.axis("equal")
st.pyplot(fig)

st.markdown("***")

np.random.seed(10)
collectn_1 = np.random.normal(100, 10, 200)
collectn_2 = np.random.normal(80, 30, 200)
collectn_3 = np.random.normal(90, 20, 200)

# combine these different collections into a list
data_to_plot = [collectn_1, collectn_2, collectn_3]

fig = plt.figure()

# Create an axes instance
ax = fig.add_axes([0, 0, 1, 1])
ax.violinplot(data_to_plot)

st.pyplot(fig)
