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
    create_image_text_layout("attached_assets/generated_images/7.jpg", layout="full")


    text0 = """
    <h2>Chapter 7: Jñāna Vijnāna Yoga (Yoga of Knowledge and Wisdom)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <span style="color:#FF5733;">Shloka 7.1 to 7.5 : </span>
Hey <span style="color:#77beda;">Arjuna</span>! Jab mann mujhmein lagta hai,
Aur yog ke dwara, meri sharan mein aakar sadhana karta hai –
Toh mujhe samagra roop se aur bina sandeh ke jaana ja sakta hai. Main tujhe poorn jñān aur vijñān (<span style="color:#77beda;">anubhav</span>) samjhaunga –
Jise jaanne ke baad is sansar mein aur kuch jaanna baaki nahi rehta. Hazaaron mein koi ek siddhi ke liye prayatna karta hai –
Aur unme se bhi koi-koi mujhe tattvatah (<span style="color:#77beda;">vastavik roop se</span>) jaanta hai. Ye jo jagat hai, woh meri <span style="color:#77beda;">8 prakritiyon</span> se bana hai –
Dharti (<span style="color:#77beda;">bhumi</span>), paani (<span style="color:#77beda;">aapah</span>), agni (<span style="color:#77beda;">fire</span>), hawa (<span style="color:#77beda;">vayu</span>), aakash (<span style="color:#77beda;">space</span>), mann, buddhi, aur ahankaar. Ye 8 prakriti meri lower (jada) prakriti hai –
Lekin iske alawa ek meri para-prakriti hai – jo <span style="color:#77beda;">jeev-aatma</span> hai,
Jo is pure sansar ko dharan kar rahi hai.
    """ 
    create_image_text_layout("attached_assets/generated_images/71.jpg", text1, layout="side", image_position="left")


    text2 = """
    <span style="color:#FF5733;">Shloka 7.6 to 7.10 : </span>
Ye sab jeev-jagat mere hi dwara utpann hua hai –
Main is poore jagat ka aadi aur ant hoon (<span style="color:#77beda;">srishti aur pralaya dono</span>). Hey <span style="color:#77beda;">Arjuna</span>! Mujhse upar kuch bhi nahi hai –
Ye sab kuch meri mala ke daanon ki tarah mujh mein hi gira hua hai. Main paani ka <span style="color:#77beda;">swaad</span> hoon,
Surya aur chandra ka <span style="color:#77beda;">prakash</span> hoon,
Vedo mein <span style="color:#77beda;">‘Om’</span> hoon,
Akashar mein <span style="color:#77beda;">shabd</span> hoon, aur purushon mein <span style="color:#77beda;">veerta</span> hoon. Main dharti ka pavitra <span style="color:#77beda;">gandh</span> hoon,
Agni ka <span style="color:#77beda;">tej</span> hoon,
Sab jeevon ka <span style="color:#77beda;">jivan</span> hoon,
Aur tapasviyon ka <span style="color:#77beda;">tap</span> hoon. Hey <span style="color:#77beda;">Arjuna</span>! Main sabhi jeevon ka <span style="color:#77beda;">sanatan beej</span> hoon –
Main buddhimaan ka <span style="color:#77beda;">buddhi</span> hoon,
Aur tejsviyon ka <span style="color:#77beda;">tej</span> hoon.
    """ 
    create_image_text_layout("attached_assets/generated_images/72.jpg", text2, layout="side", image_position="right")



    text3 = """
    <span style="color:#FF5733;">Shloka 7.11 to 7.15 : </span>
Main balwaan logon ka woh <span style="color:#77beda;">bal</span> hoon jo kaam aur vasna se rahit hai.
Aur jo kaam dharma ke viruddh nahi hai – woh bhi main hoon. <span style="color:#77beda;">Sattva, Rajas, aur Tamas</span> – teen gunon se utpann sab bhav bhi mujhse hi aaye hain.
Par main un gunon mein bandha nahi hoon – aur na hi woh mere andar hain. Ye teen gun (<span style="color:#77beda;">Sattva, Rajas, Tamas</span>) poore sansar ko moh mein daal dete hain –
Aur is moha ke kaaran log mujhe nahi jaan paate – jo in sab se para hoon. Meri ye gunon wali maya ati kathin hai –
Par jo bhakt meri sharan lete hain, woh ise asaani se paar kar lete hain. Paapi, moorkh, aur dusht prakriti wale log mujhe nahi maante –
Unka gyaan maya ke dwara chhin gaya hota hai – aur unmein <span style="color:#77beda;">asuri bhavna</span> hoti hai.
    """
    create_image_text_layout("attached_assets/generated_images/73.jpg", text3, layout="side", image_position="left")

    text5 = """
    <span style="color:#FF5733;">Shloka 7.16 to 7.20 : </span> 
Hey <span style="color:#77beda;">Arjuna</span>! Chaar prakaar ke log bhakti karte hain – 1. Aart (<span style="color:#77beda;">dukh mein</span>), 2. Artharthi (<span style="color:#77beda;">paise ya laabh ke liye</span>), 3. Jigyasu (<span style="color:#77beda;">gyaan ki ichchha se</span>), 4. Gyani (<span style="color:#77beda;">mujhe jaan chuka</span>). Un chaaron mein gyani sabse vishesh hai –
Woh mujhme sadaiv sthit hota hai, ek-bhakti se bhakta hota hai –
Main use atyant priya hoon, aur woh mujhe. Ye sab bhakt udaar aur mahan hai –
Par gyani mujhi ki roop hai, meri atma mein hi sthit hai –
Aur mujhe hi apna antim lakshya maanta hai. Kai janmon ke gyaan aur tapasya ke baad –
Ek gyani mujhe samarpit hota hai, aur kehta hai: ‘Vasudeva (<span style="color:#77beda;">Krishna</span>) hi sab kuch hai’ –
Aisa mahatma bahut durlabh hota hai. Jo log vasnaon se gyaan chhinta chuke hain –
Woh anya devataon ki pooja karte hain,
Apni prakriti ke anusaar, kuch niyamo ke anusaar unmein aastha rakhte hain.
    """
    create_image_text_layout("attached_assets/generated_images/74.jpg", text5, layout="side", image_position="right")



    text6 = """
    <span style="color:#FF5733;">Shloka 7.21 to 7.25 : </span> 
Jo bhakt jis devata ko poojna chahta hai,
Main uski us shraddha ko majboot karta hoon. Woh bhakt apni shraddha se devata ki pooja karta hai,
Aur jo phal milta hai, <span style="color:#77beda;">woh bhi main hi deta hoon</span>. Anya devata ki pooja ka phal simit hota hai –
Jo unhe poojte hain, unhi ke paas jaate hain.
Parantu mere bhakt mere paas aate hain. Jo log mujhe ek sharir mein samjhte hain,
Woh mere asli, avyakt aur sarvottam swaroop ko nahi pehchaan paate. Main sabke hriday mein hoon, par meri yog-maya mujhe sabse chhupa leti hai.
Isliye log mujhe anadi aur avyay roop mein nahi jaan paate. 
    """
    create_image_text_layout("attached_assets/generated_images/75.jpg", text6, layout="side", image_position="left")



    text7 = """
    <span style="color:#FF5733;">Shloka 7.26 to 7.30 : </span>
Hey <span style="color:#77beda;">Arjuna</span>! Main sab bhoot, bhavishya aur vartaman ko jaanta hoon –
Par koi mujhe poori tarah nahi jaanta. Moh ke kaaran, ichchha aur dvesh se janme dwandwa logon ko bhramit kar dete hain –
Aur janm ke saath hi sab jeev bhram mein pad jaate hain. Jo log apne paapon se mukta ho chuke hain aur punya karmon mein lage rahe hain –
Woh moha aur dwandwa se mukta hokar mujhe bhakti se yaad karte hain. Jo log janm aur mrityu se mukti chahte hain –
Woh meri sharan lekar <span style="color:#77beda;">brahma</span>, adhyatma aur karm ke tattv ko jaante hain. Jo bhakt mujhe sabhi roopon mein jaante hain –
Aur mrityu ke samay bhi mujhe smaran karte hain –
Woh mujhe prapt kar lete hain.
    """
    create_image_text_layout("attached_assets/generated_images/76.jpg", text7, layout="side", image_position="right")


    create_image_text_layout("attached_assets/generated_images/7banner.jpg", layout="full")
