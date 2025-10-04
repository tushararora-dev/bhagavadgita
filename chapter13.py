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
    create_image_text_layout("attached_assets/generated_images/13main.jpg", layout="full")


    text0 = """
    <h2>Chapter 13: Kshetra Kshetrajna Vibhaga Yoga (Yoga of Discriminating between the Field and the Knower of the Field)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <span style="color:#FF5733;">Shloka 13.1 to 13.5 : </span>
Hey <span style="color:#77beda;">Krishna</span>! Mujhe yeh samajhna hai:
Yeh Prakriti (<span style="color:#77beda;">Nature</span>) kya hai?
Yeh Purush (<span style="color:#77beda;">Conscious Sou</span>l) kya hai?
Yeh Kshetra (<span style="color:#77beda;">Body</span>) aur Kshetrajna (<span style="color:#77beda;">Knower of Body</span>) kaun hai? Hey <span style="color:#77beda;">Arjuna</span>! Yeh sharir hi kshetra (<span style="color:#77beda;">field</span>) kehlata hai,
Aur jo is sharir ko jaanta/samajhta hai – use kshetrajna kehte hain. Hey <span style="color:#77beda;">Arjuna</span>! Sab shariron ke andar Main (<span style="color:#77beda;">Krishna</span>) hi Kshetrajna hoon.
Yeh samajhna – ki sharir alag hai aur atma alag – yahi sachcha gyaan hai. Ab main tumhe batata hoon:
Yeh kshetra (<span style="color:#77beda;">sharir</span>) kya hai, kaisa hai, kis se bana hai, kya-kya vikaar isme hote hain —
Yeh sab gyaan ved-vyasa ke dwara tumhe prapt hoga. Ye gyaan tumhe Rishiyon ke geet, Ved-mantra, aur Brahma-sutra se milta hai —
Jo tark aur siddhant ke roop mein spasht kiya gaya hai.
    """ 
    create_image_text_layout("attached_assets/generated_images/131.jpg", text1, layout="side", image_position="left")

    text2 = """
    <span style="color:#FF5733;">Shloka 13.6 to 13.10 : </span>
Yeh sharir bana hai:
5 Mahabhoot (<span style="color:#77beda;">Prithvi, Jal, Agni, Vayu, Akash</span>)
, Ahankaar, Buddhi, Manas, 5 Gyaanendriyaan + 5 Karmendriyaan ( <span style="color:#77beda;">Desire, hate, joy, sorrow, body consciousness, etc.</span>) Jo gyaan ko dharan karta hai, usmein yeh gun hote hain:
Ahankaar ka tyag, Asaty se doori, Ahimsa, Kshama, Saralta, Guru seva, Shuddhata, Sanyam, Janm-mrityu se upar uthne ki ichchha.
    """ 
    create_image_text_layout("attached_assets/generated_images/132.jpg", text2, layout="side", image_position="right")



    text3 = """
    <span style="color:#FF5733;">Shloka 13.11 to 13.15 : </span>
Gyaani vyakti hamesha janm, mrityu, budhaapa, aur rogon ko dukh ke roop mein dekhta hai
Aur in sab se mukti paane ka prayas karta hai. Main tumhe Jneyam (<span style="color:#77beda;">jise jaana jaata hai</span>) ke baare mein bataunga –
Usse jaankar vyakti amrit (<span style="color:#77beda;">moksha</span>) ko prapt karta hai.
Woh Param Brahma hai – na sat hai na asat – woh sabse pare hai. Woh Param tattva sab ke haathon, pairon, aankhon, kaano ke roop mein vyapak hai.
Woh poore jagat ko dhak kar sthir hai. Woh indriyon se alag hai, lekin sab kuch indriyon ke jaisa lagta hai.
Woh nirgun hokar bhi sab gunaon ka bhokta hai. Woh tattva jeevon ke andar bhi hai, baahar bhi,
Woh achal bhi hai aur chalit bhi,
Woh dikhai nahi deta, lekin sabse paas bhi hai aur sabse door bhi.
    """
    create_image_text_layout("attached_assets/generated_images/133.jpg", text3, layout="side", image_position="left")

    text5 = """
    <span style="color:#FF5733;">Shloka 13.16 to 13.20 : </span> 
Woh tattva sab mein ek roop se vyapak hai,
Phir bhi lagta hai jaise sab mein alag-alag hai. Woh tattva sabhiyon ki jyoti ka bhi uttar hai –
Woh andhkaar se pare, gyaan hai, gyaan ka vishay hai, aur gyaan se prapt bhi hota hai.
Woh har ek ke hriday mein virajmaan hai. Jo bhakt is kshetra, gyaan, aur jneyam ko samajh leta hai,
Woh <span style="color:#77beda;">Krishna</span> ke svaroop mein sthit ho jaata hai. Prakriti aur Purush (<span style="color:#77beda;">jeev</span>) dono anadi hain,
Lekin jo bhi vikaar (<span style="color:#77beda;">change</span>) aur guna (<span style="color:#77beda;">qualities</span>) tum dekhte ho – woh sab prakriti se hi utpann hote hain. Karya aur karan (<span style="color:#77beda;">karma aur uske kaaran</span>) ka nirmaan prakriti karti hai,
Lekin atma (<span style="color:#77beda;">Purush</span>) unka bhokta hai – sukh aur dukh ka anubhav usi ko hota hai.
    """
    create_image_text_layout("attached_assets/generated_images/134.jpg", text5, layout="side", image_position="right")



    text6 = """
    <span style="color:#FF5733;">Shloka 13.21 to 13.25 : </span> 
Jab atma prakriti ke saath jud jaata hai,
Tab woh uske gunon (<span style="color:#77beda;">rajas, tamas, sattva</span>) ko bhokta ban jaata hai.
Isi gun-sangat se phir uska janm hota hai achhi ya buri yoni mein. Yeh Paramatma hi har deh mein
Upadrasta (<span style="color:#77beda;">witness</span>) hai
Anumanta (<span style="color:#77beda;">sanctioner</span>) hai
Bhokta, Bhartaa, aur Maheshwar bhi wahi hai
Yeh atma se bhi pare – Paramatma kehlata hai. Jo vyakti yeh samajh jaata hai ki
atma aur prakriti alag hai –
aur yeh sab gunaon se chalta hai,
To woh dobara janm nahi leta – mukt ho jaata hai. Kuch log dhyaan ke zariye atma ko anubhav karte hain,
Kuch log sankhya (<span style="color:#77beda;">vivek gyaan</span>) ke dwara,
Aur kuch log karma yog ke dwara —
sabhi marg moksha tak le ja sakte hain. Aur kuch log jo swayam nahi samajh paate,
Woh shraddha se sun kar <span style="color:#77beda;">Krishna</span> ki upasana karte hain,
Aise log bhi mrityu ke samudra ko paar kar jaate hain.
    """
    create_image_text_layout("attached_assets/generated_images/135.jpg", text6, layout="side", image_position="left")



    text7 = """
    <span style="color:#FF5733;">Shloka 13.26 to 13.30 : </span>
Jo bhi chetana roop sthavar (<span style="color:#77beda;">achalit</span>) ya jangam (<span style="color:#77beda;">chali</span>t) vastu tum dekhte ho,
Uska utpatti sharir (<span style="color:#77beda;">kshetra</span>) aur chetna (<span style="color:#77beda;">kshetrajna</span>) ke milan se hoti hai –
Aur dono ka aadhaar <span style="color:#77beda;">Krishna</span> hi hai. Jo vyakti sabhi jeevon mein ek saman atma ko dekh leta hai,
Jo sharir ke nash hone par bhi avinashi roop mein sthit hai –
Wahi vastav mein dekhta hai. Jo sab mein ek hi Ishwar ka darshan karta hai,
Woh kabhi bhi kisi ko dukhi nahi karta,
Aur aise vyakti ko milti hai param gati (<span style="color:#77beda;">mukti</span>). Jo samajhta hai ki saare karm prakriti ke dwara ho rahe hain,
Aur atma to keval sakshi hai –
Wahi gyaani hai, wahi sahi se dekhta hai. Jab vyakti dekhta hai ki sab jeev ek hi tattva se nikle hain,
Aur sab usme hi samahit ho rahe hain –
Tabhi woh Brahma mein sthit ho jaata hai.
    """
    create_image_text_layout("attached_assets/generated_images/136.jpg", text7, layout="side", image_position="right")


    text8 = """
    <span style="color:#FF5733;">Shloka 13.31 to 13.35 : </span>
Atma anadi hai, nirmal hai,
Woh karm karti nahi, aur karm se bandhti nahi –
Woh prakriti ke guno se alag hai. Jaise ek Surya poore sansaar ko prakashit karta hai,
Waise hi Kshetrajna (<span style="color:#77beda;">atma</span>) apne sharir ke kshetra ko chetna deta hai. Jo log atma aur sharir ke bhed ko gyaan ke drishti se samajh lete hain,
Aur prakriti ke bandhan se mukta ho jaate hain –
Wahi log Param gati ko prapt karte hain.
    """
    create_image_text_layout("attached_assets/generated_images/137.jpg", text8, layout="side", image_position="left")

    create_image_text_layout("attached_assets/generated_images/13banner.jpg", layout="full")
