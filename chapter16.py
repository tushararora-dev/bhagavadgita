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
    create_image_text_layout("attached_assets/generated_images/16main.jpg", layout="full")


    text0 = """
    <h2>Chapter 16: Daivi-Asuri Sampad Vibhaga Yoga (The Yoga of the Division Between Divine and Demoniac Qualities)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <span style="color:#FF5733;">Shloka 16.1 to 16.5 : </span>
Yeh sab Daivi Sampatti ke lakshan hain:
Nidarata (<span style="color:#77beda;">Abhay</span>), Antahkaran ki shuddhata, Gyaan mein sthir rehna, Daan aur indriyon par niyantran, Yagya, swadhyaya (<span style="color:#77beda;">self-study</span>), Tapasya, honesty, daya, kshama, alobh, ahimsa, Nirmalta, lajja, daya, steadiness, tyag, vinamrata. Jinke andar ho: Dambh (<span style="color:#77beda;">show-off</span>), Ahankaar, ghamand, krodh, Kathor bartaav, agyaan aur paap mein ruchi, Unmein Asuri Sampatti prabal hai – jo patan laati hai. Daivik gun – mukti ki or le jaate hain. Asurik gun – janm-mrityu ke bandhan mein aur jod dete hain. In sab gunon se manushya divya ban jaata hai.
    """ 
    create_image_text_layout("attached_assets/generated_images/161.jpg", text1, layout="side", image_position="left")

    text2 = """
    <span style="color:#FF5733;">Shloka 16.6 to 16.10 : </span>
<span style="color:#77beda;">Krishna</span> kehte hain –
Yeh sansaar do prakriti mein vibhakt hai:
<span style="color:#77beda;">Daivik log</span> – shant, sadhak, tyagi. <span style="color:#77beda;">Asurik log</span> – ahankaari, kaami, lobhi Jo log asuri pravritti mein jeete hain,
Woh kya karna chahiye, kya nahi – iska vivek hi kho dete hain. <span style="color:#77beda;">Asuri log kehte hain</span>:
“Yeh sansaar jhootha hai” , “Na koi Ishwar hai, na niyam”, “Sab kuch bas kaam-vasana se chala hai”. Aise log:
Apne aap ko khote hain, Alpa buddhi se jeete hain, Sansaar mein atyachar failate hain, Aur duniya ko naash ki or le jaate hain. Ye log bina seema ke kaam aur lobh mein doob jaate hain, Ahankaar aur dikhawa unke jeevan ka hissa hota hai, Ye galat dharanayein pakad kar jeete hain, Aur ashuddh karmo mein lage rehte hain
    """ 
    create_image_text_layout("attached_assets/generated_images/162.jpg", text2, layout="side", image_position="right")



    text3 = """
    <span style="color:#FF5733;">Shloka 16.11 to 16.15 : </span>
Asuri log kehte hain: “Zindagi ka ek hi lakshya hai – <span style="color:#77beda;">bhog karna.</span>”. Woh anant chinta mein jeete hain
Aur samajhte hain: “Yehi sab kuch hai, marne tak bhog hi karna hai.” Ye log: Aashaon ke dandon mein bandhe hote hain, Kaam aur krodh mein jeete hain, Anyay aur dhokhe se paisa kamaate hain —
Sirf apne bhogon ke liye. Unki soch hoti hai: “Yeh sab maine hi kamaya hai!”, “Ab main aur bhi ichchhaayein poori karunga.”, Ahankaar aur control ka poora bhram hota hai. <span style="color:#77beda;">Woh kehte hain</span>: “Maine apne shatru ko maar giraya hai!”, “Main sab kuch jeet gaya hoon – main hi Ishwar hoon!”, Yeh soch unhe patit bana deti hai. <span style="color:#77beda;">Unka sochna hota hai</span>:
“Main dhanvaan hoon!”, “Main special hoon, mere jaise koi nahi!”, “Main daan dunga, yagya karunga, aur maje mein jeeunga!”. Yeh sab agyaan ke bhram se utpann hota hai.
    """
    create_image_text_layout("attached_assets/generated_images/163.jpg", text3, layout="side", image_position="left")

    text5 = """
    <span style="color:#FF5733;">Shloka 16.16 to 16.20 : </span> 
Ye log: Anant chintaon mein doob jaate hain. Moh ke jaal mein phans jaate hain. Bhog-vilas mein doob kar gire jaate hain gande narak mein. <span style="color:#77beda;">Asuri log</span>: Apne aap mein hi khush, Ghamand aur paison mein doobe, Dharmik karam bhi karte hain par sirf dikhawa ke liye, Niyam ke bina, bina bhakti ke. Ye log: Ahankaar, krodh, kaam mein jite hain. <span style="color:#77beda;">Krishna</span> aur Ishwar ko apne andar ya doosron mein dekhte hi nahi. Aur isliye woh maya mein gir jaate hain. <span style="color:#77beda;">Krishna</span> kehte hain: Jo log paapi, dveshi aur krur hain,
Main unhe baar-baar janm deta hoon asuri yoni mein. Jahan se woh aur patit hote jaate hain. Jo log baar-baar asuri yoni mein janm lete hain Woh kabhi <span style="color:#77beda;">Krishna</span> ko nahi paate. Aur ant mein girte hain gatiheen, adham avastha mein
    """
    create_image_text_layout("attached_assets/generated_images/164.jpg", text5, layout="side", image_position="right")

    text6 = """
    <span style="color:#FF5733;">Shloka 16.21 to 16.24 : </span> 
<span style="color:#77beda;">Krishna</span> kehte hain: Kaam (<span style="color:#77beda;">lust</span>), Krodh (<span style="color:#77beda;">anger</span>), Lobh (<span style="color:#77beda;">greed</span>). Yeh teenon atma ka naash karte hain. Yeh hain Narak ke mukhya dwar. Inhe turant chhod dena chahiye. Jo vyakti kaam, krodh aur lobh se Mukt ho jaata hai,
Woh apne liye shreyaskari jeevan jeeta hai,
Aur aakhir mein mukti (<span style="color:#77beda;">param gati</span>) prapt karta hai. Jo vyakti: Shastra ke niyamon ko tyag kar, Apne kaam vasnaon se jeeta hai. Usse na toh safalta milti hai, Na sukh, na param gati – sirf patan milta hai. Isliye <span style="color:#77beda;">Arjuna</span>! Tumhe apne jeevan mein, Kya karna hai aur kya nahi, Iska nirnay sirf Shastra se lena chahiye. Gyaan prapt karne ke baad us anusaar karma karo.
    """
    create_image_text_layout("attached_assets/generated_images/165.jpg", text6, layout="side", image_position="left")


    create_image_text_layout("attached_assets/generated_images/16banner.jpg", layout="full")
