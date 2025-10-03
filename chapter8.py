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
    create_image_text_layout("attached_assets/generated_images/8.jpg", layout="full")


    text0 = """
    <h2>Chapter 8: Akshara Brahma Yoga (Yoga of the Imperishable Absolute)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <span style="color:#FF5733;">Shloka 8.1 to 8.5 : </span>
<span style="color:#77beda;">Arjuna</span> poochta hai:
Hey <span style="color:#77beda;">Purushottam</span>!
<span style="color:#77beda;">brahma</span> kya hai? Adhyatma kya hai? Karma kya hai?
Adhibhoot (<span style="color:#77beda;">material</span>), Adhidaiv (<span style="color:#77beda;">divine forces</span>) kya hai? Hey <span style="color:#77beda;">Madhusudan</span>! Adhiyajna (<span style="color:#77beda;">yagya ka swaroo</span>p) kaun hai is sharir mein?
Aur ant samay mein kaise tujhe yaad karein jisse mukti mile? <span style="color:#77beda;">brahma</span> ka arth hai: Akshar – jo kabhi na mitne wala
Adhyatma – Atma ka swabhav
Karma – wo kriya jo jeevon ke utpatti mein kaaran banta hai Adhibhoot – jo nashwar (material) hai,
Adhidaiv – Devata ka roop,
Aur Adhiyajna – Main khud hoon,
Jo har sharir mein sthit hoon. Jo vyakti antim samay mein mujhe smaran karta hua sharir chhodta hai,
Woh mujhe hi prapt hota hai – ismein koi sandeh nahi. 
    """ 
    create_image_text_layout("attached_assets/generated_images/81.jpg", text1, layout="side", image_position="left")


    text2 = """
    <span style="color:#FF5733;">Shloka 8.6 to 8.10 : </span>
Ant samay mein vyakti jiska smaran karta hai,
Wahi bhav lekar agla janm paata hai. Isliye <span style="color:#77beda;">Arjuna</span>, har samay mujhe smaran karte hue apna karma karo (<span style="color:#77beda;">yudh karo</span>).
Mujh mein mann aur buddhi lagaoge to nischit roop se mujhe prapt kar loge. Jo bhakt sada abhyas (<span style="color:#77beda;">practice</span>) ke saath mujhmein mann lagata hai,
Aur anya kisi mein nahi bhatakta – woh mujhe zarur prapt karta hai. Jo vyakti ant samay mein us Purush ka smaran karta hai –
Jo sabse prachin, sabka niyamak, sabse chhota aur sabse bada,
Sab kuch dharan karne wala, tejomay, aur andhkaar ke paar hai –
Woh usko prapt karta hai. Jo vyakti mrityu ke samay mann ko sthir karta hai,
Bhakti aur yog-shakti ke saath, praan ko bhru-madhya mein sthir karta hai,
Aur mujhe smaran karta hai – woh mujhe, us <span style="color:#77beda;">divya Purush</span> ko, prapt karta hai.
    """ 
    create_image_text_layout("attached_assets/generated_images/82.jpg", text2, layout="side", image_position="right")



    text3 = """
    <span style="color:#FF5733;">Shloka 8.11 to 8.15 : </span>
Jise ved-gyani “<span style="color:#77beda;">Akshar Brahma</span>” kehte hain,
Jisme vairaagi yogi pravesh karte hain,
Jiske liye brahmacharya ka paalan karte hain —
Woh rahasya main ab batata hoon. Jo yogi sab indriyon ko control karta hai,
Mann ko hriday mein sthir karta hai,
Aur praan ko <span style="color:#77beda;">bhrumadhya</span> mein le jata hai —
Woh yog-dhaarana ki sthiti mein sthit ho jaata hai. Jo vyakti <span style="color:#77beda;">‘Om’</span> uchcharan karte hue mujhe smaran karta hai,
Aur usi bhaav se sharir tyagta hai —
Woh meri divya gati ko prapt karta hai. Jo bhakt sada mujhe bina bhatakaye yaad karta hai —
Main uske liye atyant sulabh ho jaata hoon. Jo mahatma mujhe prapt kar lete hain,
Woh is dukhmay aur ashashvat jagat mein phir kabhi janm nahi lete.
    """
    create_image_text_layout("attached_assets/generated_images/83.jpg", text3, layout="side", image_position="left")

    text5 = """
    <span style="color:#FF5733;">Shloka 8.16 to 8.20 : </span> 
Hey <span style="color:#77beda;">Arjuna</span>! Brahmalok se lekar prithvi tak, sabhi lok punarjanm ke chakr mein hai.
Par jo mujhe prapt karta hai, woh phir janm nahi leta. Brahma ke ek din mein <span style="color:#77beda;">1000</span> yug (<span style="color:#77beda;">approx. 4.32 billion years</span>) hote hain,
Aur raat bhi utni hi hoti hai —
Ye gyaan yogi log jaante hain. Brahma ke din mein sab jeev prakat hote hain avyakt se —
Aur raat ke aane par sabhi usi avyakt mein vilin ho jaate hain. Yeh jeev-jagat baar-baar utpann hota hai aur vilin hota hai —
Raat ke aate hi sab kuch mit jaata hai, aur din ke aate hi dobara shuru ho jaata hai. Us avyakt se bhi ek para-avyakt (<span style="color:#77beda;">Supreme Unmanifested</span>) hai —
Jo anadi hai, aur sab kuch ke mit jaane par bhi nahi mit ta.
    """
    create_image_text_layout("attached_assets/generated_images/84.jpg", text5, layout="side", image_position="right")



    text6 = """
    <span style="color:#FF5733;">Shloka 8.21 to 8.25 : </span> 
Woh akshar, avyakt aur param gati hai —
Jise paakar vyakti kabhi laut kar sansar mein nahi aata —
Wahi mera Param Dham hai. Woh Param Purush sirf ek-nishtha bhakti se prapt hota hai —
Jiske andar sab sthit hain, aur jo sab mein vyapak hai. Hey <span style="color:#77beda;">Arjuna</span>! Main ab tujhe woh kaal (<span style="color:#77beda;">time</span>) bataata hoon jisme
yogi agar sharir chhodte hain to mukti milti hai,
aur jis samay chhodne se punarjanm hota hai. Jo yogi agni, prakash, shukla paksha aur uttarayan kaal mein sharir tyagte hain —
Woh <span style="color:#77beda;">Brahma</span> ko prapt karte hain aur punarjanm nahi lete. Jo yogi dhoom (<span style="color:#77beda;">smoke</span>), raat, <span style="color:#77beda;">krishna</span> paksha aur dakshinayan mein sharir chhodte hain —
Woh chandramasi lok mein jaakar phir punarjanm lete hain.
    """
    create_image_text_layout("attached_assets/generated_images/85.jpg", text6, layout="side", image_position="left")



    text7 = """
    <span style="color:#FF5733;">Shloka 8.26 to 8.28 : </span>
Shwet marg se yogi <span style="color:#77beda;">moksha</span> prapt karte hain –
Aur <span style="color:#77beda;">krishna</span> marg se phir se janm lete hain. Jo yogi in margon ko jaanta hai, woh kabhi bhramit nahi hota.
Isliye, <span style="color:#77beda;">Arjuna</span> – har samay yog mein sthit raho. Jo yogi mujhe jaankar bhakti karta hai,
Woh ved paath, yagya, tapasya aur daan ke sabhi punyon se upar uth jaata hai –
Aur Param Sthaan (<span style="color:#77beda;">Moksha</span>) ko prapt karta hai.
    """
    create_image_text_layout("attached_assets/generated_images/86.jpg", text7, layout="side", image_position="right")


    create_image_text_layout("attached_assets/generated_images/8banner.jpg", layout="full")
