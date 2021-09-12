import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

from PIL import Image
# image = Image.open(r"1.jpg")
# st.image(image)

image = Image.open('pen.jpg')
body_part_image = Image.open('bodyparts.jpg')
# img_adelie = Image.open('1.jpg')S
video_file = open('gentoo.mp4', 'rb')
video_bytes = video_file.read()

video_file1 = open('ade.mp4', 'rb')
video_bytes1 = video_file1.read()

video_file2 = open('ade.mp4', 'rb')
video_bytes2 = video_file2.read()

st.title("Pygoscelis Penguins")
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
# print('Culmen Length Distribution')
fig, ax = plt.subplots()
df_1 = df[['species', 'bill_length_mm']]
ax = sns.violinplot(data=df_1, x="species", y="bill_length_mm",
                    orient='v', palette=["orange", "c", "#8A2BE2"])
# plt.show()

st.pyplot(fig)
st.markdown("***")


st.markdown('''
            The Gentoo species have a very long flipper length! \nAfter some research I found that gentoos like all penguins are awkward on land, \nbut they’re pure grace underwater. \nThey have streamlined bodies and strong, paddle-shaped flippers that propel them up to\n22 miles an hour, faster than any other diving bird.
            '''
            )
# print('Flipper Length Distribution')
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
# print('Culmen Length Distribution')
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


a = st.selectbox("Who would you like to know more about?",
                 ['Adelie Penguin', 'Gentoo Penguin', 'Chinstrap Penguin'])

if a == 'Adelie Penguin':
    st.markdown(
        '''
                # **Adelie Penguins!**
        '''
    )

    st.markdown(
        '''
            The Adélie penguin (Pygoscelis adeliae) is a species of penguin common along the entire coast of the Antarctic continent, which is its only habitat. It is the most widely spread penguin species,
            as well as the most southerly distributed of all penguins, along with the emperor penguin. It is named after Adélie Land, in turn named for Adèle Dumont d'Urville, who was married to French explorer Jules Dumont d'Urville, who first discovered this penguin in 1840. Adélie penguins obtain their food by both predation and foraging, with a diet of mainly krill and fish.
        '''
    )
    st.video(video_bytes1)
    st.markdown(
        '''
            - **COMMON NAME**: Adélie Penguin
            - **SCIENTIFIC NAME**: Pygoscelis adeliae
            - **TYPE**: Birds
            - **DIET**: Carnivore
            - **GROUP NAME**: Colony
            - **AVERAGE LIFE SPAN IN THE WILD**: 11 to 20 years
            - **SIZE**: 27.5 inches
            - **WEIGHT**: 8.5 to 12 pounds
        '''
    )
    st.markdown('''**CURRENT POPULATION TREND: Increasing**''')

    st.markdown('''
    Adélie penguins live on the Antarctic continent and on many small, surrounding coastal islands. They spend the winter offshore in the seas surrounding the Antarctic pack ice.


    **Diet**


    Adélies feed on tiny aquatic creatures, such as shrimp-like krill, but also eat fish and squid. They have been known to dive as deep as 575 feet in search of such quarry, though they usually hunt in far shallower waters less than half that depth.

    Like other penguins, Adélies are sleek and efficient swimmers. They may travel 185 miles round-trip to procure a meal.

    **Breeding**


    During the spring breeding season (in October), they take to the rocky Antarctic coastline where they live in large communities called colonies. These groups can include thousands of birds.

    Once on land, Adélies build nests and line them with small stones. Though they move with the famed “penguin waddle” they are capable walkers who can cover long overland distances. In early spring, before the vast sheets of ice break up, they may have to walk 31 miles from their onshore nests to reach open water.

    Male Adélie penguins help their mates rear the young and, without close inspection, the two sexes are nearly indistinguishable. They take turns sitting on a pair of eggs to keep them warm and safe from predators. When food is short, only one of the two chicks may survive. After about three weeks, parents are able to leave the chicks alone, though the offspring gather in groups for safety. Young penguins begin to swim on their own in about nine weeks.''')

elif a == 'Gentoo Penguin':
    # Gentoo

    st.markdown(
        '''
                # **Gentoo Penguins!**
        '''
    )

    st.markdown(
        '''
            The gentoo penguin is a penguin species in the genus Pygoscelis, most closely related to the Adélie penguin and the chinstrap penguin. The earliest scientific description was made in 1781 by Johann Reinhold Forster with a type locality in the Falkland Islands.
        '''
    )
    st.video(video_bytes)
    st.markdown(
        '''
            - **COMMON NAME**: Gentoo Penguin
            - **SCIENTIFIC NAME**: Pygoscelis papua
            - **TYPE**: Birds
            - **DIET**: Carnivore
            - **GROUP NAME**: Colony
            - **AVERAGE LIFE SPAN IN THE WILD**: 15 to 20 years
            - **SIZE**: 30 inches
            - **WEIGHT**: 12 pounds
        '''
    )
    st.markdown('''**CURRENT POPULATION TREND: Decreasing**''')

    st.markdown('''
    With flamboyant red-orange beaks, white-feather caps, and peach-colored feet, gentoo penguins stand out against their drab, rock-strewn Antarctic habitat.



    **Habitat**

    These charismatic waddlers, who populate the Antarctic Peninsula and numerous islands around the frozen continent, are the penguin world’s third largest members, reaching a height of 30 inches and a weight of 12 pounds.

    Gentoos are partial to ice-free areas, including coastal plains, sheltered valleys, and cliffs. They gather in colonies of breeding pairs that can number from a few dozen to many thousands.


    **Parenting**


    Gentoo parents, which often form long-lasting bonds, are highly nurturing. At breeding time, both parents will work to build a circular nest of stones, grass, moss, and feathers. The mother then deposits two spherical, white eggs, which both parents take turns incubating for more than a month. Hatchlings remain in the nest for up to a month, and the parents alternate foraging and brooding duties.

    **Underwater Adaptations**


    Like all penguins, gentoos are awkward on land. But they’re pure grace underwater. They have streamlined bodies and strong, paddle-shaped flippers that propel them up to 22 miles an hour, faster than any other diving bird.

    **Hunting**


    Adults spend the entire day hunting, usually close to shore, but occasionally ranging as far as 16 miles out. When pursuing prey, which includes fish, squid, and krill, they can remain below for up to seven minutes and dive as deep as 655 feet.

    **Threats to Survival**


    Gentoo penguins are a favored menu item of the leopard seals, sea lions, and orcas that patrol the waters around their colonies. On land, adults have no natural predators other than humans, who harvest them for their oil and skin. Gentoo eggs and chicks, however, are vulnerable to birds of prey, like skuas and caracaras.

    Gentoo numbers are increasing on the Antarctic Peninsula but have plummeted in some of their island enclaves, possibly due to local pollution or disrupted fisheries. They are protected by the Antarctic Treaty of 1959 and received near threatened status on the IUCN Red List in 2007.''')
    # Chinstrap

else:
    st.markdown(
        '''
                # **Chinstrap Penguins!**
        '''
    )

    st.markdown(
        '''
            The chinstrap penguin is a species of penguin that inhabits a variety of islands and shores in the Southern Pacific and the Antarctic Oceans. Its name stems from the narrow black band under its head, which makes it appear as if it were wearing a black helmet, making it easy to identify.
        '''
    )
    st.video(video_bytes2)
    st.markdown(
        '''
            - **COMMON NAME**: Chinstrap Penguin
            - **SCIENTIFIC NAME**: Pygoscelis antarcticus
            - **TYPE**: Birds
            - **DIET**: Carnivore
            - **GROUP NAME**: Colony
            - **SIZE**: 28 inches
            - **WEIGHT**: 6.6 to 11 pounds
        '''
    )
    st.markdown('''**CURRENT POPULATION TREND: Decreasing**''')

    st.markdown('''
    Instantly recognizable by the black band that gives them their name, chinstrap penguins are the most abundant penguin in the Antarctic, where they gather in massive breeding colonies.

    After spending the winter north of the sea ice, chinstraps return in late October or early November to their nest sites, usually with the same breeding partners. These colonies are on the rocky, ice-free coasts of the South Sandwich Islands, South Shetland Islands, and Antarctic continent.

    The sheer number of birds in the colonies is astounding. The largest colony, on the uninhabited South Sandwich island of Zavodovski, hosts some 1.2 million breeding pairs. Baily Head in the South Shetland Islands is home to more than 100,000 pairs.''')

    st.markdown('''

    **Threats**


    In the water, where they feed primarily on krill, the penguins’ main predator is the leopard seal. On land, chinstraps face threats from skuas, giant petrels, and other birds that steal the penguins’ eggs and attack chicks, as well as a more unusual threat: volcanic activity. An ill-timed eruption in 2016 on Zavodovski Island covered much of the colony in ash as the birds were undergoing their annual molt. During molt, when they lose their waterproof feathers, they are land-locked and can’t go in the sea until their feathers regrow.

    Chinstrap penguin numbers increased in the mid-20th century, attributed by some to the rebound of krill from centuries of seal and whale hunting. Today, some populations are declining, though not precipitously. Restrictions are in place to keep tourists from approaching breeding birds too closely.


    **Breeding and nesting**


    A female chinstrap typically will lay two eggs in a circular nest made from stones. The parents share egg-sitting duties, each spending several days on the nest before a shift change. After about 37 days, the chicks hatch. They spend another few weeks in the nest, then waddle into a crèche, where the fluffy, gray juveniles are cared for communally. At around two months old, they get their adult feathers and are able to head to sea.''')
