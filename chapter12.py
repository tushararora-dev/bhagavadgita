import streamlit as st
from app import create_image_text_layout   # reuse function from main.py

def display_content():

    st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bungee+Spice:wght@700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Beth+Ellen&display=swap');
    h2 {
        font-family: 'Bungee Spice', cursive !important;
        font-size: 45px;
        text-align: center;
        color: #e7b66c !important;
    }
    p, li { 
        font-size: 18px !important;
        # line-height: 1.6 !important;
        text-align: justify !important;
        color: oldlace;
    }

    .st-emotion-cache-1gcegfv h2 {
    font-size: 1.5rem;
    }
    table {
        border-collapse: collapse;
        width: 100%;
    }

    td {
        border: 2px solid #444 !important;
        padding: 5px;
        font-size: 16px !important;
        line-height: 1.2 !important;
        text-align: justify !important;
        color: oldlace;
        background-color: #6969691f; /* dark background to contrast oldlace */
    }


    .beth1 {
            font-family: 'Beth Ellen', cursive !important; /* <-- use Beth Ellen (imported) */
            font-size: 22px;
            color: oldlace !important;
            text-align: center !important;
            margin-top: 0.2em;
            color: dimgray !important;
        }

    </style>
    """,
    unsafe_allow_html=True
    )
    create_image_text_layout("attached_assets/generated_images/12main.jpg", layout="full")


    text0 = """
    <h2>Chapter 12: Bhakti Yoga (The Yoga of Devotion)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <span style="color:#FF5733;">Shloka 12.1 to 12.5 : </span>
Hey <span style="color:#77beda;">Krishna</span>! Jo log tumhare roop mein bhakti karte hain
aur jo log nirgun (<span style="color:#77beda;">roop-rahit</span>) brahm ki upasana karte hain —
Unmein se kaun zyada uttam yogi hai? Jo apna man mere roop mein laga kar bhakti karte hain,
Aur jo mujhe shraddha se poojte hain,
Wahi mere liye sabse yogy bhakt hain. Jo log nirgun, avyakt Brahm ki upasana karte hain,
Jo indriyon ko sanyam mein rakhte hain, sab mein sama bhav rakhte hain —
Woh bhi mujhe prapt kar lete hain. Jo avyakt (<span style="color:#77beda;">nirgun Brahm</span>) ki upasana karte hain —
Unke liye yeh marg bahut kathin hai,
Kyonki deh mein jeev rehkar nirakar mein man lagana bahut mushkil hota hai.
    """ 
    create_image_text_layout("attached_assets/generated_images/121.jpg", text1, layout="side", image_position="left")

    text2 = """
    <span style="color:#FF5733;">Shloka 12.6 to 12.10 : </span>
Jo log mujh mein man laga kar, ananya bhakti se mujhe poojte hain,
Main unhe mrityu aur sansaar ke samudra se bahut jald paar kara deta hoon. Agar tum man aur buddhi dono mujhmein laga do,
To tum nishchit roop se mujhe prapt karoge. Hey <span style="color:#77beda;">Arjuna</span>! Agar tumhara man sthir nahi ho raha,
To abhyas kar ke mujhe prapt karne ki koshish karo. Agar tum abhyas bhi nahi kar sakte,
To kam se kam mere liye karm karo —
Isse tum safalta (<span style="color:#77beda;">siddhi</span>) prapt kar loge.
Isme koi sandeh nahi.
    """ 
    create_image_text_layout("attached_assets/generated_images/122.jpg", text2, layout="side", image_position="right")



    text3 = """
    <span style="color:#FF5733;">Shloka 12.11 to 12.15 : </span>
Agar tum mere liye karm bhi nahi kar sakte,
To kam se kam phal ka tyag karo —
Aur atmavash bano, niyantran mein raho. Abhyas se gyaan behtar hai, gyaan se bhi behtar hai dhyan,
Dhyan se bada hai karm ke phal ka tyag,
Aur tyag se antar shanti milti hai. Jo kisi se dvesh nahi karta, sabse mitra aur karuna ka bhav rakhta hai,
Jo ahankar rahit, sukh-dukh mein samaan, aur kshemi (<span style="color:#77beda;">maaf karne wala</span>) ho,
Jo santusht, atma-nigrah mein sthir, aur mujhmein man aur buddhi samarpit karta hai —
Woh bhakt mujhe atyant priya hai. Jo duniya ko ashant nahi karta, aur jise duniya dekh kar bhi ashant nahi hoti,
Jo khushi, irsha, bhay, ghabrahat se mukta hai —
Woh mujhe bahut priya hai.
    """
    create_image_text_layout("attached_assets/generated_images/123.jpg", text3, layout="side", image_position="left")

    text5 = """
    <span style="color:#FF5733;">Shloka 12.16 to 12.20 : </span> 
Jo kisi se apeksha nahi rakhta, shuddh, chatur, santulit, aur chinta-mukt hai,
Jo har karm mein nishkaam bhav rakhta hai —
Woh bhakt bhi mujhe priya hai. Jo na to harshit hota hai, na dukh mein dukhi hota hai,
Na to kisi vashtu ki iccha karta hai, na shok mein dube rehta hai,
Jo achhe-bure fal ka tyag kar deta hai —
Woh bhakt mujhe bahut priya hai. Jo dost aur dushman, maan aur apmaan, sukh-dukh, thand-garmi mein samaan bhav rakhta hai,
Jo maun, ninda-stuti mein ek jaisa, santusht, aur nirgranth (<span style="color:#77beda;">ghar se lagav rahit</span>) hai —
Woh bhakt mujhe priya hai. Jo log is dharmik amrit ko shraddha se poojan karte hain,
Jo mujhe sarvaswa maante hain —
Aise bhakt mujhe atyant priya hote hain. 
    """
    create_image_text_layout("attached_assets/generated_images/124.jpg", text5, layout="side", image_position="right")



    create_image_text_layout("attached_assets/generated_images/12banner.jpg", layout="full")
