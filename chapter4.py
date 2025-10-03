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
    create_image_text_layout("attached_assets/generated_images/4banner.jpg", layout="full")


    text0 = """
    <h2>Chapter 4: Jnana Karma Sannyasa Yoga (Yoga of Knowledge, Renunciation, and Action)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <span style="color:#FF5733;">Shloka 4.1 to 4.5 : </span>
<span style="color:#77beda;">Krishna</span> kehte hain — Yeh avyay (<span style="color:#77beda;">amarpan</span>) yog ka gyaan maine Surya dev (<span style="color:#77beda;">Vivasvan</span>) ko diya tha,
Surya ne Manu ko, aur Manu ne Ikshvaku ko bataya. Yeh yog parampara se <span style="color:#77beda;">raja-rishiyon</span> tak pahucha,
lekin samay ke saath iska gyaan prithvi se chhup gaya. Wahi purana yog aaj main tumse keh raha hoon, kyunki tum mere bhakt aur sakha (<span style="color:#77beda;">mitra</span>) ho.
Yeh gyaan ati rahasya aur uttam hai. <span style="color:#77beda;">Arjuna</span> kehta hai — Aapka janm abhi hua, aur Surya dev ka to pehle hua.
To aapne unhe gyaan kaise diya? Hey <span style="color:#77beda;">Arjuna</span>! Mera bhi aur tumhara bhi anek janm ho chuka hai.
Main sab yaad rakhta hoon — lekin tum nahi.
    """ 
    create_image_text_layout("attached_assets/generated_images/41.jpg", text1, layout="side", image_position="left")


    text2 = """
    <span style="color:#FF5733;">Shloka 4.6 to 4.10 : </span>
Main aj (<span style="color:#77beda;">ajanma</span>), avyay (<span style="color:#77beda;">avinashi</span>), aur sab ka swami hoon.
Phir bhi main apni maya se prakriti ko adheen karke avataar leta hoon. Jab-jab dharm ki hani hoti hai, aur adharm badhta hai —
Tab-tab main swayam prakat hota hoon. Main har yug mein avataar leta hoon — bhakton ka rakshan karne, paapiyon ka naash karne,
aur dharm ki sthapana ke liye. Jo vyakti mere divya janm aur karm ko tattva se samajhta hai —
Woh deh tyag ke baad phir janm nahi leta, balki mujhme hi sthit ho jaata hai. Jo log raga (<span style="color:#77beda;">asakti</span>), bhay (<span style="color:#77beda;">dar</span>), aur krodh (<span style="color:#77beda;">gussa</span>) se mukt ho kar mere mein lean hote hain,
Aur jnana-tapas se shuddh hote hain — woh meri divya gati ko prapt karte hain.
    """ 
    create_image_text_layout("attached_assets/generated_images/42.jpg", text2, layout="side", image_position="right")



    text3 = """
    <span style="color:#FF5733;">Shloka 4.11 to 4.15 : </span>
Jo jaise mujhe bhajta hai, main usi bhaav se usse milta hoon.
Hey <span style="color:#77beda;">Arjuna</span>! Sabhi log mere hi raaste par chal rahe hain – chahe jaane ya na jaane. Log devtaon ki pooja isliye karte hain kyunki unhe karm ka turant phal chahiye.
Aur unhe yeh turant mil bhi jaata hai. Main ne hi <span style="color:#77beda;">chaar varna</span> banaye – unke gun aur karm ke aadhar par.
Lekin mujhe un sabka karta maano, lekin main akarta hoon. Karm mujhe chhoo nahi sakta, na hi mujhe karm ke phalon ki ichchha hai.
Jo vyakti mujhe aise samajhta hai, uska bhi karm se bandhan toot jaata hai. Purane yogi aur mukti ki ichchha rakhne wale bhi is jnana se karm karte the.
Tum bhi waise hi karm karo.
    """
    create_image_text_layout("attached_assets/generated_images/43.jpg", text3, layout="side", image_position="left")

    text5 = """
    <span style="color:#FF5733;">Shloka 4.16 to 4.20 : </span> 
Karm kya hai aur akarm kya hai, ismein bade-bade gyaani bhi uljhe rahe hain.
Ab main tumhe iska gyaan doonga – jisse tum paap se mukta ho jaoge. <span style="color:#77beda;">Karm, vikarm, aur akarm</span> – in tino ko samajhna zaroori hai.
Kyonki karm ki gati bahut gahan (<span style="color:#77beda;">deep</span>) hai. Jo karm mein akarm, aur akarm mein karm dekhta hai – wahi buddhimaan hai.
Wahi yogi hai jo sab kuch sahi roop se karta hai. Jiske sab karm phal ki ichchha se mukt hain, aur jnana-agni mein jal gaye hain –
Usse hi pandit (<span style="color:#77beda;">gyaani</span>) kehte hain. Jo vyakti phal ki asakti chhod deta hai, hamesha santusht rehta hai, aur aashray se mukt hota hai –
Woh karm karta hua bhi karta hua nahi hota.
    """
    create_image_text_layout("attached_assets/generated_images/44.jpg", text5, layout="side", image_position="right")



    text6 = """
    <span style="color:#FF5733;">Shloka 4.21 to 4.25 : </span> 
Jo vyakti ichchhaon se mukt hai, jiska mann aur indriya sanyamit hain,
aur jo sirf sharirik avashyakta ke liye karm karta hai – uska karm <span style="color:#77beda;">paap nahi banata.</span> Jo vyakti jaisa bhi mil jaaye usme santusht rehta hai,
dukh-sukh se pare hai, aur jo safalta-asafalta mein samaan rehta hai — uska karm kabhi bandhan nahi banata. Jo vyakti asakti se mukt hai, jiska mann gyaan mein sthit hai,
aur jo har karm ko yajna (<span style="color:#77beda;">samarpan</span>) ke roop mein karta hai – uska sab karm vilin ho jaata hai. Yajna mein arpan karne wala, havan ka padarth, agni, aur grahan karne wala – sabhi Brahma hi hai.
Jo is bhaav se karm karta hai, woh <span style="color:#77beda;">Brahma</span> ko hi prapt karta hai. Kuch yogi devtaon ke liye yajna karte hain, aur kuch log sab kuch <span style="color:#77beda;">Brahma</span> mein arpan karte hain.
    """
    create_image_text_layout("attached_assets/generated_images/45.jpg", text6, layout="side", image_position="left")



    text7 = """
    <span style="color:#FF5733;">Shloka 4.26 to 4.30 : </span>
Kuch yogi apni indriyon (<span style="color:#77beda;">jaise shravan, drishti</span>) ko sanyam agni mein arpan karte hain.
Aur kuch viṣhayon (<span style="color:#77beda;">jaise shabd, roop</span>) ko indriya-agni mein yajna roop se arpan karte hain. Kuch log sabhi indriya-karm aur praan-kriya ko apne atm-samyam aur gyaan ke agni mein arpan karte hain. Kuch log dhan ka daan karte hain, kuch tap karte hain, kuch yog ka abhyas karte hain,
aur kuch log svadhyaya (<span style="color:#77beda;">adhyayan</span>) aur gyaan ka yajna karte hain. Kuch yogi praan (<span style="color:#77beda;">shwas</span>) ko apaan mein, aur apaan (<span style="color:#77beda;">nishwas</span>) ko praan mein arpan karte hain.
Woh praan-aapaan ki gatiyon ko rok kar praanayam ka yajna karte hain. Kuch log apne aahar ko niyantrit karke, praanon ko praan mein hi arpan karte hain.
Sabhi yajna ko jaane wale log paap se mukt ho jaate hain.
    """
    create_image_text_layout("attached_assets/generated_images/46.jpg", text7, layout="side", image_position="right")


    text9 = """
    <span style="color:#FF5733;">Shloka 4.31 to 4.35 : </span>
Jo log yajna ke baad bacha hua prasad (<span style="color:#77beda;">amrit</span>) grahan karte hain,
Woh sanatan Brahma tak pahuch jaate hain.
Jo yajna nahi karta, uske liye yeh duniya bhi nahi – to dusri ka to prashna hi nahi! Yeh sab yajna, jo ved ke mukh se nikle hain,
Woh karm se paida hote hain – inhe jaan kar tum karm se mukt ho jaoge. Hey <span style="color:#77beda;">Arjuna</span>! Dravya (<span style="color:#77beda;">dhan, vastu</span>) se kiya gaya yajna se bada hai – <span style="color:#77beda;">gyaan-yajna</span>.
Kyonki sabhi karmon ka ant gyaan mein hota hai. Tum gyaan paane ke liye guru ke paas jao – vinamrata se, prashna karke, seva karke.
Jo tattva-darshi hain, woh tumhe yeh gyaan denge. Hey <span style="color:#77beda;">Arjuna</span>! Jab tum yeh gyaan pa jaoge, tab kabhi phir moh mein nahi padoge.
Tab tum sabhi jeevon ko apne aatma mein aur mujhme dekh paoge.
    """
    create_image_text_layout("attached_assets/generated_images/47.jpg", text9, layout="side", image_position="left")


    text10 = """
    <span style="color:#FF5733;">Shloka 4.36 to 4.42 : </span>
Agar tum sabse bada paapi bhi ho – to bhi gyaan ki naav tumhe paapon se paar kar degi. Jaise agni lakdi ko bhasm kar deti hai,
Waise hi gyaan ki agni sab paapon ko bhasm kar deti hai. Is sansaar mein gyaan se bada aur pavitra kuch bhi nahi.
Aur yogi use samay ke saath apne andar prapt karta hai. Jo shraddha se bhara hota hai, jiska mann laga hua hai, aur jiska indriyon par sanyam hai –
Wahi <span style="color:#77beda;">gyaan prapt</span> karta hai, aur use param shanti milti hai. Jo agyaani hai, shraddha se rahit hai, aur sandeh se bhara hai – woh vinash ko prapt hota hai.
Na yeh duniya uske liye sukhmay hoti hai, na agla lok. Hey <span style="color:#77beda;">Dhananjay</span> (<span style="color:#77beda;">Arjuna</span>)!
Jo vyakti yog dwara apne karm tyag chuka hai,
Jiska sandeh gyaan se chhinn ho chuka hai,
Aur jo swayam mein sthit hai – usse koi karm bandhan nahi deta. Isliye, tumhare hriday mein jo agyaan se paida hua sandeh hai,
Use apne gyaan-ki-talwar se kaat do –
Aur yog mein sthit hokar khade ho jao, <span style="color:#77beda;">Arjuna</span>!
    """
    create_image_text_layout("attached_assets/generated_images/48.jpg", text10, layout="side", image_position="right")



    create_image_text_layout("attached_assets/generated_images/4.jpg", layout="full")
