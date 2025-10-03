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
    create_image_text_layout("attached_assets/generated_images/9.jpg", layout="full")


    text0 = """
    <h2>Chapter 9: Raja Vidya Raja Guhya Yoga (Yog through the King of Sciences)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <span style="color:#FF5733;">Shloka 9.1 to 9.5 : </span>
Hey <span style="color:#77beda;">Arjuna</span>! Tu asuya (<span style="color:#77beda;">ninda</span>) nahi karta, isliye main tujhe sabse gupt gyaan batata hoon.
Yeh jnana-vijnana se yukt hai — isse jaan kar tu sab paapon se mukt ho jaayega. Yeh hai rajavidya (<span style="color:#77beda;">gyaan ka raja</span>), rajaguhya (<span style="color:#77beda;">sabse gupt</span>),
Pavitra, turant anubhav hone yogya, dharmmay aur karne mein sukhdayak hai —
Aur avinashi hai. Jin logon mein shraddha nahi hoti, woh is dharm ko nahi apnaate —
Aur phir janm-mrityu ke chakra mein hi ghoomte rehte hain. Main avyakta (<span style="color:#77beda;">unseen</span>) roop mein poore jagat mein vyapak hoon,
Sab jeev mujh mein hi sthit hain – par main unmein sthit nahi hoon. Woh sab mujh mein sthit hain, par main unmein sthit nahi hoon –
Yeh mera adbhut divya yog hai.
Main un sab jeevon ka aadhar hoon – par unmein bastaa nahi.
    """ 
    create_image_text_layout("attached_assets/generated_images/91.jpg", text1, layout="side", image_position="left")


    text2 = """
    <span style="color:#FF5733;">Shloka 9.6 to 9.10 : </span>
Jaise vayu (<span style="color:#77beda;">hawa</span>) sada aakash mein chhupi hoti hai —
Waise hi sab jeev mujh mein sthit hain. Hey <span style="color:#77beda;">Kaunteya</span>! Kalp ke ant mein sab prani meri prakriti mein sama jaate hain —
Aur kalp ke prarambh mein main unhe phir se rachata hoon. Main apni prakriti par niyantran rakhkar baar-baar sab jeevon ka srishti karta hoon —
Aur sabhi mere prakriti ke niyam se pravritt hote hain. Hey <span style="color:#77beda;">Dhananjaya</span>! Ye sab karm mujhe bandhte nahi –
Main sab kuch karta hua bhi asakta (<span style="color:#77beda;">on-attached</span>) hoon. Meri adhyakshata mein hi prakriti (<span style="color:#77beda;">maya</span>) chalti hai —
Wahi sab jeev (<span style="color:#77beda;">char-achar</span>) ka srishti karti hai.
    """ 
    create_image_text_layout("attached_assets/generated_images/92.jpg", text2, layout="side", image_position="right")



    text3 = """
    <span style="color:#FF5733;">Shloka 9.11 to 9.15 : </span>
Murkh log mujhe ek manushya roop mein dekhkar mere upar hansi udate hain,
Kyuki unhe yeh samajh hi nahi aata ki main sab ka <span style="color:#77beda;">Ishwar</span> hoon. Jinmein bhakti nahi hoti, unki aasha, karm aur gyaan sab bekaar ho jaata hai.
Woh asuri aur rakshasi prakriti mein fass jaate hain. Jo mahaatma log hote hain, woh meri daivi prakriti ko samajh kar mujhe nishtha se bhajte hain,
Kyuki unhe pata hota hai ki main hi sab ka adi (<span style="color:#77beda;">origin</span>) hoon. Jo bhakt mujhe sada smaran karte hain,
Jap karte hain, bhakti se pranam karte hain,
Aur dridhta se meri seva mein lage rehte hain. Kuch bhakt mujhe gyaan-yagya ke roop mein poojte hain –
Koi mujhe ek roop (<span style="color:#77beda;">advait</span>) mein dekhta hai,
Koi anek roop (<span style="color:#77beda;">vibhinn devtaon</span>) mein –
Aur koi mujhe sab dishao mein vyapak dekh kar poojta hai.
    """
    create_image_text_layout("attached_assets/generated_images/93.jpg", text3, layout="side", image_position="left")

    text5 = """
    <span style="color:#FF5733;">Shloka 9.16 to 9.20 : </span> 
Main hi <span style="color:#77beda;">yagya</span> hoon, <span style="color:#77beda;">mantra</span> hoon, <span style="color:#77beda;">aahuti</span> hoon, <span style="color:#77beda;">agni</span> hoon —
Sab kuch mere hi roop mein ho raha hai. Main is jagat ka <span style="color:#77beda;">pita</span> hoon, <span style="color:#77beda;">mata</span> hoon, palan karne wala hoon, aur <span style="color:#77beda;">pitama</span>h bhi hoon.
Main hi <span style="color:#77beda;">vedon ka gyaan</span>, <span style="color:#77beda;">pavitra Omkaar</span> aur <span style="color:#77beda;">ved-mantra</span> bhi hoon. Main sab jeevon ki gati hoon, <span style="color:#77beda;">palak</span> hoon, <span style="color:#77beda;">saakshi</span> hoon,
Mera hi vaas hai, main hi <span style="color:#77beda;">sharan</span> hoon, <span style="color:#77beda;">mitra</span> hoon,
Srishti ka prarambh, ant aur aadhar hoon — main hi <span style="color:#77beda;">akshar beej</span> hoon. Main hi garmi deta hoon, main hi varsha karta hoon,
Main hi <span style="color:#77beda;">mrit</span> aur <span style="color:#77beda;">amrit</span> hoon,
Main hi sat (<span style="color:#77beda;">visible</span>) aur asat (<span style="color:#77beda;">invisible</span>) hoon. Jo log ved-paathi hain aur devtaon ki pooja karte hain,
Woh swarg ki aasha se yajna karte hain,
Aur swarg mein jaakar devtaon ke sukh bhogte hain.
    """
    create_image_text_layout("attached_assets/generated_images/94.jpg", text5, layout="side", image_position="right")



    text6 = """
    <span style="color:#FF5733;">Shloka 9.21 to 9.25 : </span> 
Swarg ka sukh bhog kar, jab punya samapt ho jaata hai,
To ye log firse mrityulok mein laut aate hain.
Yeh hi hai <span style="color:#77beda;">swarg-ka-chakkar</span> – aana, jaana, fir aana. Jo bhakt sirf mujhe hi smaran karta hai,
Main uska yog (<span style="color:#77beda;">jo chahiye</span>) aur kshema (<span style="color:#77beda;">jo mila hai uski raksha</span>) khud karta hoon. Jo anya devtaon ki bhakti bhi shraddha se karte hain,
Woh bhi mujhe hi poojte hain – lekin galat vidhiyon se. Main sab yagyon ka bhokta hoon, prabhu hoon —
Par jo mujhe tattv se nahi jaante, woh phir gir jaate hain (<span style="color:#77beda;">punarjanm lete hain</span>). Jo devtaon ki bhakti karta hai – devtaon ke paas jaata hai.
Jo pitron ki – unke paas jaata hai.
Par jo <span style="color:#77beda;">Krishna</span> ki bhakti karta hai – mere paas aa jaata hai.
    """
    create_image_text_layout("attached_assets/generated_images/95.jpg", text6, layout="side", image_position="left")



    text7 = """
    <span style="color:#FF5733;">Shloka 9.26 to 9.30 : </span>
Jo bhakt mujhe prem se ek patra (<span style="color:#77beda;">leaf</span>), pushp (<span style="color:#77beda;">flower</span>), phal (<span style="color:#77beda;">fruit</span>) ya toya (<span style="color:#77beda;">water</span>) bhi arpit karta hai —
Main usse prem se svikar karta hoon. Jo bhi tu kare – khaaye, daan de, tapasya kare – sab kuch mujhe arpan kar de. Is bhaav se tu paap-punya ke phalon se pare ho jaayega —
Aur karma-bandhan se mukt hokar mere paas aa jaayega. Main sab mein samaan hoon – na kisi se dvesh karta hoon na prem karta hoon.
Par jo bhakt mujhe prem se bhajta hai – main usme hoon, aur woh mujh mein. Agar koi bhakt bhatak bhi jaaye, lekin ananya bhakti karta ho —
To use sant hi maana jaata hai, kyuki uska mann sahi disha mein hai.
    """
    create_image_text_layout("attached_assets/generated_images/96.jpg", text7, layout="side", image_position="right")


    text8 = """
    <span style="color:#FF5733;">Shloka 9.31 to 9.34 : </span>
Woh bhakt jaldi hi dharmic ban jaata hai, aur ant mein shanti paata hai.
Hey <span style="color:#77beda;">Arjuna</span>! Yeh meri pratigya hai – mera bhakt kabhi nash nahi hota. Hey <span style="color:#77beda;">Arjuna</span>! Chahe koi bhi ho – paapi, stri, vaishya ya shudra —
Agar woh bhakti kare, to woh bhi mujhe prapt kar sakta hai. Agar paapi log bhi mujhe paa sakte hain,
To punyaatma brahman aur rajarshi to aur bhi asaani se mujhe paayenge.
Is dukhmay aur ashashvat jagat mein rehkar — <span style="color:#77beda;">mujhe bhaj</span>! Apna mann mujh mein lagaa, mera bhakt ban, mujhe arpan kar, mujhe pranam kar.
Main tujhe pratigya deta hoon – tu mujhe prapt karega, kyunki tu mujhe priya hai.
    """
    create_image_text_layout("attached_assets/generated_images/97.jpg", text8, layout="side", image_position="left")


    create_image_text_layout("attached_assets/generated_images/9banner.jpg", layout="full")
