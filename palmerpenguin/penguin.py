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
- **Culmen_length_mm / bill_length_mm**: culmen length (mm)
- **Culmen_depth_mm / bill_depth_mm**: culmen depth (mm)
- **Flipper_length_mm**: flipper length (mm)
- **Body_mass_g**: body mass (g)
- **Island**: island name
- **Sex**: penguin sex
    '''
)

# st.table(df.head(1))
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

st.markdown('''**The distribution of the species based on island in the dataset**
            \n As we can see
            Biscoe and Dream have a majority of the penguins with some of them in the Torgersen island also.''')

fig, ax = plt.subplots()
ax = sns.countplot(data=df, x="island", palette=["orange", "c", "#8A2BE2"])
st.pyplot(fig)
st.markdown("***")

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


st.markdown('''
            As we can see the bill length of the Adelie penguins is very small compared to the others! 
            '''
            )
print('Culmen Length Distribution')
fig, ax = plt.subplots()
df_1 = df[['species', 'bill_length_mm']]
ax = sns.violinplot(data=df_1, x="species", y="bill_length_mm",
                    orient='v', palette=["orange", "c", "#8A2BE2"])
# plt.show()

st.pyplot(fig)
st.markdown("***")


st.text('''
            The Gentoo species have a very long flipper length! \nAfter some research I found that gentoos like all penguins are awkward on land, \nbut they’re pure grace underwater. \nThey have streamlined bodies and strong, paddle-shaped flippers that propel them up to\n22 miles an hour, faster than any other diving bird.
            '''
        )
print('Flipper Length Distribution')
fig, ax = plt.subplots()
df_1 = df[['species', 'flipper_length_mm']]
ax = sns.violinplot(data=df_1, x="species", y="flipper_length_mm",
                    orient='v', palette=["orange", "c", "#8A2BE2"])
# plt.show()

st.pyplot(fig)


st.markdown("***")


st.markdown('''
            Gentoo Penguins are slightly heavier also compared to others. :P
            '''
            )
print('Culmen Length Distribution')
fig, ax = plt.subplots()
df_1 = df[['species', 'body_mass_g']]
ax = sns.violinplot(data=df_1, x="species", y="body_mass_g",
                    orient='v', palette=["orange", "c", "#8A2BE2"])
# plt.show()

st.pyplot(fig)
st.markdown("***")

st.markdown('''
            *Now we go into depth for all three of these penguins and try to learn more about them!*
            ''')

st.markdown(
    '''
             **Adelie Penguins!** 
    '''
)
