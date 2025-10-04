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
    create_image_text_layout("attached_assets/generated_images/15main.jpg", layout="full")


    text0 = """
    <h2>Chapter 15: Purushottama Yoga (Yoga of the Supreme Person)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <span style="color:#FF5733;">Shloka 15.1 to 15.5 : </span>
Yeh duniya ka ped (<span style="color:#77beda;">śhvattha vriksha</span>a) hai: Jiski jad upar (<span style="color:#77beda;">Brahma mein</span>) hai, Aur shaakhaayen neeche – karma, icchaon, sambandhon ke roop mein. Ved iska patta hai
Jo is vriksh ko samajhta hai – vah hi gyaani hai. Is samsaar-vriksh ki shaakhaayen upar aur neeche fel gayi hain,
Yeh sattva, rajas, tamas guno se badi hoti hain
Ismein vishayon (<span style="color:#77beda;">indriya sukh</span>) ke patte hain
Aur karm ke phal se manushya inmein ulajhta chala jaata hai. Is vriksh ka na to ant hai, na aarambh,
Yeh ati gehra hai – isse pehchanna bhi mushkil hai,
Par isse kaata ja sakta hai ek hi hathiyar se:
Asakti-rahit gyaan (<span style="color:#77beda;">asaṅga-śhastreṇa</span>) Jab tum is sansaar-vriksh ko kaat dete ho,
Tab tumhe khojna chahiye woh gati (<span style="color:#77beda;">param sthiti</span>),
Jahan jaane ke baad wapas aana nahi padta
Jo hai <span style="color:#77beda;">Purushottam Krishna</span> ka adhyatmik lok Jo vyakti:
Ahankaar-mukt, Asakti se pare, Kaamnaayein tyag chuka hai, Aur sukh-dukha ke dvandv se pare ho gaya hai –
Wahi Purushottam pad ko prapt karta hai.
    """ 
    create_image_text_layout("attached_assets/generated_images/151.jpg", text1, layout="side", image_position="left")

    text2 = """
    <span style="color:#FF5733;">Shloka 15.6 to 15.10 : </span>
Wah sthaan (<span style="color:#77beda;">lok</span>) jahan:
Na surya, Na chandrama, Na agni roshni dete hain –
Mera apna roop hi prakash hai. Wah param dham hai – jahan se lautna nahi hota. Jeev mera hi ansh hai – lekin
Jab woh prakriti ke bandhan mein padta hai,
Tab woh mann aur indriyon ke dwara kheenchta hai –
Aur bhool jaata hai apna asli roop. Jab jeev ek shareer chhodkar doosra grahan karta hai,
Tab woh mann, buddhi aur ahankaar ko saath le jaata hai –
Jaise hawa sugandh le jaati hai ek sthan se doosre tak. Jeev <span style="color:#77beda;">kaanon, aankhon, twacha, jeebh, naak aur mann</span> ke madhyam se
Vishayon ka bhog karta hai,
Aur usmein asakti aur bandhan utpann hota hai. Jab jeev:
Shareer se nikalta hai, Shareer mein sthit rehta hai, Ya indriyon ke saath bhog mein laga hota hai –
Agyaani log isey nahi samajhte. Sirf gyaan-chakshu waale hi is raaz ko dekh paate hain.
    """ 
    create_image_text_layout("attached_assets/generated_images/152.jpg", text2, layout="side", image_position="right")



    text3 = """
    <span style="color:#FF5733;">Shloka 15.11 to 15.15 : </span>
Jo yogi gyaani hote hain,
Wahi apne andar sthit atma ko dekh paate hain.
Par agyaani aur ashuddh mann waale,
Chahe koshish bhi karein, apne aap ko nahi jaan paate. Jo roshni Surya, Chandrama aur Agni se poore jagat mein failti hai,
Us prakash ko mera hi tejas (<span style="color:#77beda;">divya urja</span>) samjho. Main prithvi mein pravesh karke,
Sab jeevon ko jeevan aur bal deta hoon.
Main hi sab auṣadhi (<span style="color:#77beda;">vanaspati</span>) ko ras aur jeevan deta hoon. Main Vaishvanar Agni bankar tumhare shareer mein sthit ho jaata hoon,
Aur prana-apana ke dwara bhojan ko pachata hoon –
Chaar prakar ke ann (<span style="color:#77beda;">khaya-peeya-chusa-gila sab</span>). Main hi sabke hriday mein sthit hoon,
Aur smriti (<span style="color:#77beda;">yaad</span>), gyaan aur vismriti sab mujhse hi aati hai.
Vedon ka saar bhi main hi hoon,
Main Veda-vid bhi hoon aur Veda-kaar bhi. 
    """
    create_image_text_layout("attached_assets/generated_images/153.jpg", text3, layout="side", image_position="left")

    text5 = """
    <span style="color:#FF5733;">Shloka 15.16 to 15.20 : </span> 
Is sansaar mein do prakaar ke purush (<span style="color:#77beda;">aatma roop</span>) hain:
Kshar Purush – Jo shareer dharan karte hain,
Akshar Purush – Jo avyakt, sthir aur parmatma ke samaan hain. Par ek aur Purush hai – Uttam Purush –
Jo Paramatma ke roop mein jaana jaata hai.
Main (<span style="color:#77beda;">Krishna</span>) hi hoon:
Jo teenon lokon mein vyapt hoon, Jo sab kuch dharan karta hoon,
Aur Ishwar hoon – avyaya (<span style="color:#77beda;">anashvar</span>). Main hi hoon jo:
Kshar (<span style="color:#77beda;">jeev</span>) se upar hoon
Akshar (<span style="color:#77beda;">avyakt</span>) se bhi upar hoon
Isliye Ved aur lok mujhe kehte hain:
<span style="color:#77beda;">Purushottam</span> – sabse uchch, sabse divya. Jo vyakti bhram rahit ho kar,
Mujhe <span style="color:#77beda;">Purushottam</span> ke roop mein jaanta hai –
Woh sarvagya (<span style="color:#77beda;">poorna gyaani</span>) ban jaata hai,
Aur sarv bhav se meri bhakti karta hai. Hey <span style="color:#77beda;">Arjuna</span>!
Mainne tumhe Gita ka sabse rahasya roop (<span style="color:#77beda;">Purushottam Yoga</span>) bataya hai.
Jo ise samajh leta hai,
Woh ban jaata hai:
Buddhimaan, Aur jeevan ka kartavya poora kar leta hai.
    """
    create_image_text_layout("attached_assets/generated_images/154.jpg", text5, layout="side", image_position="right")


    create_image_text_layout("attached_assets/generated_images/15banner.jpg", layout="full")
