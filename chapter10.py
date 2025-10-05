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
    create_image_text_layout("attached_assets/generated_images/10main.jpg", layout="full")


    text0 = """
    <h2>Chapter 10: Vibhuti Yoga (Yoga of Divine Glories)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <span style="color:#FF5733;">Shloka 10.1 to 10.5 : </span>
Hey <span style="color:#77beda;">Arjuna</span>! Tu mujhe priya hai, isliye main tujhe firse wohi uttam gyaan de raha hoon —
Jo teri bhalayi ke liye hai. Devta aur maharishi bhi mujhe poori tarah nahi jaan sakte,
Kyuki main hi unka aadi (<span style="color:#77beda;">origin</span>) hoon. Jo mujhe aj (<span style="color:#77beda;">ajanma</span>), anadi (<span style="color:#77beda;">anaadi</span>) aur jagat ka swami samajhta hai,
Woh sab paapon se mukta ho jaata hai. Buddhi, gyaan, satya, kshama, sukha-dukh, bhay-abhay —
Sab kuch mujhse hi nikalta hai. Ahimsa, santosh, tapasya, daan, yash-apyash —
Yeh sab alag-alag bhaav bhi mujhse hi utpann hote hain.
    """ 
    create_image_text_layout("attached_assets/generated_images/101.jpg", text1, layout="side", image_position="left")


    text2 = """
    <span style="color:#FF5733;">Shloka 10.6 to 10.10 : </span>
Purane <span style="color:#77beda;">saptarishi</span>, <span style="color:#77beda;">chaar Kumar</span> aur <span style="color:#77beda;">Manu</span> – sab mere hi mann se utpann hue hain,
Aur unse hi yah sansaar aaya. Jo meri vibhuti (<span style="color:#77beda;">shaktiyon</span>) aur yog (<span style="color:#77beda;">divyata</span>) ko samajhta hai,
Woh dridha yog mein sthir ho jaata hai – ismein koi sandeh nahi. Main sab kuch ka kaaran hoon – sab kuch mujhse hi utpann hota hai.
Jo is bhaav se mujhe jaante hain, woh bhakti mein lag jaate hain. Mere bhakt apna chitta mujh mein laga kar, mujhe lekar baatein karte hain,
Paraspar mujhe smaran karte hain, aur usme hi sukh paate hain. Jo mujhe prem se bhajta hai – main usko buddhi-yog deta hoon,
Jisse woh mujhe prapt kar sake.
    """ 
    create_image_text_layout("attached_assets/generated_images/102.jpg", text2, layout="side", image_position="right")



    text3 = """
    <span style="color:#FF5733;">Shloka 10.11 to 10.15 : </span>
Jo mujhe prem se bhajate hain, un par kripa karke main unke hriday ka agyaan nasht karta hoon
Aur gyaan ka prakash jalaata hoon. Hey <span style="color:#77beda;">Krishna</span>! Aap hi param Brahman, param dhaam, param pavitra ho.
Aap hi sanatan, adidev, ajanma aur sab per vyapak ho. Sab rishi, jaise Narad, Asit, Deval aur Vyasa bhi aapko isi roop mein maante hain,
Aur aap khud bhi yeh keh rahe ho. Hey <span style="color:#77beda;">Keshav</span>! Jo kuch bhi aap keh rahe ho, main use satya maanta hoon.
Devta aur asur bhi aapko poori tarah nahi jaan sakte. Hey <span style="color:#77beda;">Purushottam</span>! Aap hi apne aap ko achhi tarah jaante ho.
Aap hi sab jeevon ke kartā, devtaon ke devta, aur jagat ke swami ho.
    """
    create_image_text_layout("attached_assets/generated_images/103.jpg", text3, layout="side", image_position="left")

    text5 = """
    <span style="color:#FF5733;">Shloka 10.16 to 10.20 : </span> 
Hey <span style="color:#77beda;">Krishna</span>! Kripya mujhe apni sabhi divya vibhootiyan (<span style="color:#77beda;">shaktis</span>) bataaiye,
Jinke madhyam se aap sab lokon mein vyapak hain. Hey <span style="color:#77beda;">Yogeshwar</span>! Main aapko kis roop mein dhyaan karun?
Aap kis-kis bhaav mein sthit ho kar bhakt ke chintan yogya ho? Hey <span style="color:#77beda;">Janardan</span>! Mujhe aapki leela sunne mein anant sukh milta hai,
Aap mujhe aur batayein – kyuki mujhe aapka amrit-roop gyaan kabhi bhi booring nahi lagta. Hey <span style="color:#77beda;">Arjuna</span>! Ab main tujhe apni mukhya vibhutiyon ka varnan karunga.
Mere roopon ka koi ant nahi hai – main bas pramukh batane jaa raha hoon. Hey <span style="color:#77beda;">Gudakesh</span> (<span style="color:#77beda;">Arjuna</span>)! Main hi sab jeevon ka <span style="color:#77beda;">antar-aatma</span> hoon,
Main hi sab ka <span style="color:#77beda;">aadi, madhya aur ant</span> hoon.
    """
    create_image_text_layout("attached_assets/generated_images/104.jpg", text5, layout="side", image_position="right")



    text6 = """
    <span style="color:#FF5733;">Shloka 10.21 to 10.25 : </span> 
Main Adityon (<span style="color:#77beda;">devtaon</span>) mein <span style="color:#77beda;">Vishnu</span> hoon,
Jyotiyon mein Ravi (<span style="color:#77beda;">Surya</span>),
Maruto mein <span style="color:#77beda;">Marichi</span>,
Aur nakshatron mein <span style="color:#77beda;">Chandrama</span> hoon. Main Vedon mein <span style="color:#77beda;">Saamveda</span> hoon,
Devtaon mein <span style="color:#77beda;">Indra</span> (<span style="color:#77beda;">Vasava</span>),
Indriyon mein <span style="color:#77beda;">mann</span> hoon,
Aur jeevon mein <span style="color:#77beda;">chetna</span> hoon. Rudron mein <span style="color:#77beda;">Shankar</span> hoon,
Yaksh-Rakshason mein dhan ke devta <span style="color:#77beda;">Kuber</span> hoon,
Vasus mein <span style="color:#77beda;">Agni</span> hoon,
Aur parvaton mein Main <span style="color:#77beda;">Meru</span> hoon. Purohiton mein <span style="color:#77beda;">Brihaspati</span> hoon,
Senapatiyon mein <span style="color:#77beda;">Kartikeya</span> (<span style="color:#77beda;">Skanda</span>) hoon,
Aur jalashay (<span style="color:#77beda;">saritaon</span>) mein main <span style="color:#77beda;">Sagarr</span> hoon. Maharshiyon mein <span style="color:#77beda;">Bhrigu</span> hoon,
Vaani mein <span style="color:#77beda;">Akshar Om</span> hoon,
Yagyaon mein <span style="color:#77beda;">Jap-Yagya</span> hoon,
Aur achal cheezon mein <span style="color:#77beda;">Himalaya</span> hoon.
    """
    create_image_text_layout("attached_assets/generated_images/105.jpg", text6, layout="side", image_position="left")



    text7 = """
    <span style="color:#FF5733;">Shloka 10.26 to 10.30 : </span>
Vrikshon mein <span style="color:#77beda;">Peepal</span> hoon,
Dev Rishiyon mein <span style="color:#77beda;">Narad</span> hoon,
Gandharvon mein <span style="color:#77beda;">Chitrarath</span> hoon,
Aur Siddhon mein <span style="color:#77beda;">Kapil Muni</span> hoon. Ghodo mein <span style="color:#77beda;">Ucchaishrava</span> hoon (<span style="color:#77beda;">jo samudra manthan se nikla</span>),
Haathiyon mein <span style="color:#77beda;">Airavat</span> hoon,
Aur manushyon mein <span style="color:#77beda;">Raja</span> hoon. Shastron mein <span style="color:#77beda;">Vajra</span> hoon (<span style="color:#77beda;">Indra ka astra</span>),
Gayon mein <span style="color:#77beda;">Kamdhenu</span> hoon,
Utpadan mein Kandarpa (<span style="color:#77beda;">Kaamdev</span>) hoon,
Sapon mein <span style="color:#77beda;">Vasuki</span> hoon. Naagon mein <span style="color:#77beda;">Shesh</span> hoon,
Jal mein <span style="color:#77beda;">Varun dev</span> hoon,
Pitraon mein <span style="color:#77beda;">Aryama</span> hoon,
Aur niyantran (control) karne walon mein <span style="color:#77beda;">Yamraj</span> hoon. Daityon (<span style="color:#77beda;">asuron</span>) mein <span style="color:#77beda;">Prahlad</span> hoon,
Ganit mein <span style="color:#77beda;">Samay</span> hoon,
Pashuon mein <span style="color:#77beda;">Singh</span> hoon,
Aur pakshiyon mein <span style="color:#77beda;">Garud</span> hoon.
    """
    create_image_text_layout("attached_assets/generated_images/106.jpg", text7, layout="side", image_position="right")


    text8 = """
    <span style="color:#FF5733;">Shloka 10.31 to 10.35 : </span>
Shuddhi karne walon mein <span style="color:#77beda;">Vayu</span> hoon,
Yodhon mein <span style="color:#77beda;">Shri Ram</span> hoon,
Machhliyon mein <span style="color:#77beda;">Makar</span> hoon,
Aur nadiyon mein <span style="color:#77beda;">Ganga</span> hoon. Main srishti ka <span style="color:#77beda;">aarambh, madhya aur ant hoon</span>,
Vidyaon mein <span style="color:#77beda;">Adhyatma-Vidya</span> hoon,
Aur vaadon mein <span style="color:#77beda;">satya-vad</span> hoon. Aksharon mein <span style="color:#77beda;">‘A’</span> hoon,
Vyakaran mein <span style="color:#77beda;">Dvandva samas</span> hoon,
Main hi akshar <span style="color:#77beda;">Kaal</span> hoon,
Aur sab dishao mein vyapak dhata hoon. Main hi Mrityu hoon jo sab kuch le jaata hai,
Main hi bhavishya mein hone wali <span style="color:#77beda;">srishti</span> hoon,
Naariyon mein Kirti, Shree (<span style="color:#77beda;">laxmi</span>), Vani (<span style="color:#77beda;">speech</span>), Smriti (<span style="color:#77beda;">memory</span>), Medha (<span style="color:#77beda;">intellect</span>), Dhriti (<span style="color:#77beda;">patience</span>), aur <span style="color:#77beda;">Kshama</span> hoon. Main Sama Veda ke madhur geeton mein <span style="color:#77beda;">Brihat-Saam</span> hoon,
Chhandon mein <span style="color:#77beda;">Gayatri</span> hoon,
Maason mein <span style="color:#77beda;">Margashirsh</span> hoon (<span style="color:#77beda;">Nov–Dec</span>),
Aur rituvon mein Phoolo wala <span style="color:#77beda;">basant</span> hoon.
    """
    create_image_text_layout("attached_assets/generated_images/107.jpg", text8, layout="side", image_position="left")

    text9 = """
    <span style="color:#FF5733;">Shloka 10.36 to 10.42 : </span>
Main chhalne waalon mein <span style="color:#77beda;">dyut</span> (<span style="color:#77beda;">chaturai, jaise Krishna ka mahabharat mein</span>),
Tejasvinon mein <span style="color:#77beda;">tej</span> hoon,
Main <span style="color:#77beda;">jeet</span> hoon, <span style="color:#77beda;">dridhta</span> hoon,
Aur shreshta logon mein unka <span style="color:#77beda;">sattvik gunn</span> hoon. Main Vrishni kul mein <span style="color:#77beda;">Vasudev</span> (<span style="color:#77beda;">khud Krishna</span>) hoon,
Pandavon mein <span style="color:#77beda;">Arjun</span> (<span style="color:#77beda;">Dhananjaya</span>),
Rishiyon mein <span style="color:#77beda;">Vyas</span> hoon,
Aur kavi mein <span style="color:#77beda;">Shukracharya</span> hoon. Dand dene waalon mein Main <span style="color:#77beda;">dand</span> hoon,
Jeetne ki ichha rakhne walon mein <span style="color:#77beda;">neeti</span> hoon,
Guptiyon mein main <span style="color:#77beda;">maun</span> hoon,
Aur gyaaniyon ka gyaan bhi main hi hoon. Hey <span style="color:#77beda;">Arjuna</span>! Main sab jeevon ka <span style="color:#77beda;">beej</span> hoon —
Aisa kuch bhi nahi jo mujhse alag ho, sab chala- achal mujhse hi utpann hain. Hey <span style="color:#77beda;">Arjuna</span>! Meri vibhootiyon ka koi ant nahi hai —
Jo kuch bataya gaya, woh bas udaharan tha. Jo kuch bhi shresth, shaktishaali, sundar ya ananya lagta hai —
Samajh le woh mera hi ek ansh hai, meri tej ki jhalak hai. Hey <span style="color:#77beda;">Arjuna</span>! Tujhe itni vibhootiyon ki kya zarurat hai?
Main to poore brahmand ko apne ek chhote se ansh se dharan karta hoon.
    """
    create_image_text_layout("attached_assets/generated_images/108.jpg", text9, layout="side", image_position="right")


    create_image_text_layout("attached_assets/generated_images/10banner.jpg", layout="full")
