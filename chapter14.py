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
    create_image_text_layout("attached_assets/generated_images/14main.jpg", layout="full")


    text0 = """
    <h2>Chapter 14: Guna-Traya Vibhaga Yoga (oga of the Classification of the Three Gunas)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <span style="color:#FF5733;">Shloka 14.1 to 14.5 : </span>
Main tumhe ek aisa gyaan dene jaa raha hoon,
Jo sabhi gyaanon se uchch hai,
Jise jaankar <span style="color:#77beda;">Rishimuni</span> param siddhi ko prapt kar chuke hain. Jo log is gyaan mein sthit hote hain,
Woh srishti ke samay janm nahi lete,
Aur pralaya ke samay dukhi nahi hote –
Woh mere svaroop mein sthit ho jaate hain. Meri prakriti (<span style="color:#77beda;">maaya</span>) ko samanya roop se mahad brahma kaha gaya hai,
Usmein main beej roop mein chetna daalta hoon,
Aur wahin se sab jeevon ka utpatti hota hai. Hey <span style="color:#77beda;">Arjuna</span>! Sabhi yoni mein jitne bhi jeev paida hote hain,
Unka sharirik aadhaar meri prakriti hai,
Aur chetna ka beej main daalta hoon –
Main hi sab ka pita hoon. Yeh teen guna – Sattva (<span style="color:#77beda;">gyaan, shuddhi</span>), Rajas (<span style="color:#77beda;">iccha, kaam</span>), Tamas (<span style="color:#77beda;">moh, alasy</span>) –
Prakriti se utpann hote hain,
Aur yehi jeev-atma ko sharir mein baandh dete hain.
    """ 
    create_image_text_layout("attached_assets/generated_images/141.jpg", text1, layout="side", image_position="left")

    text2 = """
    <span style="color:#FF5733;">Shloka 14.6 to 14.10 : </span>
Sattva guna shuddh, prakashmay, aur rog-rahit hota hai,
Woh gyaan aur sukh ke sang mein jeev ko baandhta hai –
Yani achha lagta hai, par still bandhan hi hai. Rajas guna ka swabhav raag (<span style="color:#77beda;">iccha</span>) aur trishna hai,
Woh kaam aur karma ke dwara jeev ko baandhta hai –
Yeh vyakti ko sthayi ashanti deta hai. Tamas guna ka janm hota hai agyaan se,
Aur yeh bhram, alasya, nidra, pramaad ke roop mein jeev ko baandhta hai –
Yeh vyakti ko sochne aur jaagne se rokta hai. Sattva sukh mein baandhta hai,
Rajas karma mein, Tamas agyaan ke andhkaar mein –
Teeno jeev ko apni apni or kheenchte hain. Kabhi Rajas aur Tamas ke kam hone par Sattva badhta hai,
Kabhi Rajas badhta hai, toh kabhi Tamas –
Yani ek satat sangharsh chalta rehta hai manushya ke andar.
    """ 
    create_image_text_layout("attached_assets/generated_images/142.jpg", text2, layout="side", image_position="right")



    text3 = """
    <span style="color:#FF5733;">Shloka 14.11 to 14.15 : </span>
Jab sharir ke sabhi indriyon mein prakash (<span style="color:#77beda;">spasht gyaan</span>) dikhai dene lage,
Tab samajh jao ki Sattva guna badh gaya hai. Jab lobh, restless karma, ashaanti, aur adhik iccha ka prabhav ho –
Tab samajh jao ki Rajas guna prachand hai. Jab prakash ka abhaav (<span style="color:#77beda;">bhram</span>), kuch na karna (<span style="color:#77beda;">inactivity</span>),
aur moh, alasy, galat faisle hon –
Samajh jao ki Tamas guna upar aa gaya hai. Jo vyakti Sattva guna mein sthit hokar shareer chhodta hai,
Woh uttam gyaaniyon ki yoni ya dev-lok mein janm paata hai. Jo Rajas mein shareer chhodta hai, woh karma-vaale gharon mein janm leta hai,
Aur jo Tamas mein shareer chhodta hai, woh moodha yoni (<span style="color:#77beda;">jaise andhkaar mein</span>) paida hota hai.
    """
    create_image_text_layout("attached_assets/generated_images/143.jpg", text3, layout="side", image_position="left")

    text5 = """
    <span style="color:#FF5733;">Shloka 14.16 to 14.20 : </span> 
Sattva se milta hai shuddh gyaan aur shanti,
Rajas se milta hai dukh,
Aur Tamas se milta hai bhram aur andhkaar. Sattva → Gyaan, Rajas → Lobh & kaamnaayein, Tamas → Bhram, agyaan aur pramaad. Sattvik log upar (<span style="color:#77beda;">uchch yon</span>i) jaate hain,
Rajasik log madhya mein hi rahte hain,
Aur Tamasik log neeche aur pashuyoni mein janm lete hain. Jab vyakti yeh samajhta hai ki main nahi, guna hi sab kuch kar rahe hain,
Aur main inn gunaon se alag hoon –
Tab woh <span style="color:#77beda;">Krishna</span> ke svaroop mein sthit ho jaata hai. Jo vyakti Sattva, Rajas, aur Tamas – in teen gunaon se pare ho jaata hai,
Woh janm, mrityu, budhaapa aur dukh se mukta ho jaata hai,
Aur amrit (<span style="color:#77beda;">mukti</span>) ko prapt karta hai.
    """
    create_image_text_layout("attached_assets/generated_images/144.jpg", text5, layout="side", image_position="right")



    text6 = """
    <span style="color:#FF5733;">Shloka 14.21 to 14.25 : </span> 
"Hey <span style="color:#77beda;">Krishna</span>! Gunateet vyakti ke kaunse lakshan hote hain?
Woh kaisa aacharan karta hai? Aur woh kaise in teen gunaon se upar uth jaata hai?" Jo vyakti:
Prakash (<span style="color:#77beda;">gyaan</span>),
Pravritti (<span style="color:#77beda;">karma</span>),
Moh (<span style="color:#77beda;">bhram</span>) –
In teeno ke aane-par jaane-par
na to dvesh karta hai, na ichchha rakhta hai,
Wahi vyakti gunateet kehlata hai. Gunateet vyakti:
Sukh-dukha mein samaan,
Mitti, pathar, sona mein koi bhed nahi,
Ninda ya prashansa mein ek samaan,
Woh dheera aur sthir-buddhi wala hota hai. Woh vyakti:
Maan-amaan mein tulya,
Mitra aur shatru dono ke prati samaan,
Sabhi kaamon ke phalon ka tyagi hota hai –
Wahi gunateet kehlata hai.
    """
    create_image_text_layout("attached_assets/generated_images/145.jpg", text6, layout="side", image_position="left")



    text7 = """
    <span style="color:#FF5733;">Shloka 14.26 to 14.27 : </span>
Jo vyakti mujh (<span style="color:#77beda;">Krishna</span>) ki nishtha se bhakti karta hai,
Woh teen gunaon ko paar kar jaata hai,
Aur Brahma-roop (<span style="color:#77beda;">divya chetna</span>) mein sthit ho jaata hai. Main (<span style="color:#77beda;">Krishna</span>) hi hoon Brahma (<span style="color:#77beda;">Parmatattva</span>) ka aadhaar,
Main hi hoon:
Amrit (<span style="color:#77beda;">amar gyaan</span>) ka,
Avyaya (<span style="color:#77beda;">anashvar</span>) ka,
Shaashwat dharma ka,
Aur param sukh ka ekmatra srot.
    """
    create_image_text_layout("attached_assets/generated_images/146.jpg", text7, layout="side", image_position="right")


    create_image_text_layout("attached_assets/generated_images/14banner.jpg", layout="full")
