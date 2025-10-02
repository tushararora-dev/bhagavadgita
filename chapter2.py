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
    create_image_text_layout("attached_assets/generated_images/2.jpg", layout="full")


    text0 = """
    <h2>Chapter 2: Sankhya Yoga (Yoga of Knowledge)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <span style="color:#FF5733;">Shloka 2.1 to 2.5 : </span>
    <span style="color:#77beda;">Sanjay</span> kehta hai — <span style="color:#77beda;">Arjuna</span> kripaa mein dooba hua tha, aankhon mein aansu the, pura shok se hil chuka tha. Tab <span style="color:#77beda;">Krishna</span> ne usse sambodhit kiya. Hey <span style="color:#77beda;">Arjuna</span>! Yeh kaun si kamzori tum mein aa gayi hai?
    Yeh na toh Arya (<span style="color:#77beda;">uttam purush</span>) ke laayak hai, na hi swarg lane wali hai, aur na hi tumhari kirti banayegi. <span style="color:#77beda;">Arjuna</span>! Na to kamzori dikhana tere liye uchit hai, na dar ke aage jhukna.
    Chhoti soch aur hriday ki daurbalya (<span style="color:#77beda;">emotional weakness</span>) ko chhod kar uth ja! Hey <span style="color:#77beda;">Krishna</span>! Main <span style="color:#77beda;">Bheeshma</span> aur <span style="color:#77beda;">Drona</span> jaise guruon par baan kaise chala sakta hoon?
    Jo mere poojya hain, unhe main dushman ki tarah kaise dekhun? Aise mahaan logon ko maarne se achha toh bhiksha maang kar jeevan bitana hai.
    Kya main unka rakht lagaa bhog bhogun?
    """ 
    create_image_text_layout("attached_assets/generated_images/21.jpg", text1, layout="side", image_position="left")


    text2 = """
    <span style="color:#FF5733;">Shloka 2.6 to 2.10 : </span>
    Mujhe samajh nahi aa raha ki jeetna zyada achha hoga ya haarna.
    Jinko maarne se mujhe sankoch ho raha hai, wohi toh saamne khade hain.
    Main dayaa ke rog se peedit ho chuka hoon. Dharma ke mamle mein <span style="color:#77beda;">confused</span> hoon.
    Main aapka shishya ban raha hoon — mujhe jo uttam ho, woh bataiye. Main jis dukh mein hoon, usse na rajya, na dhan, na hi devtaon ki power mita sakti hai. <span style="color:#77beda;">Sanjaya</span> kehta hai — <span style="color:#77beda;">Arjuna</span> ne <span style="color:#77beda;">Krishna</span> se kaha:
    “<span style="color:#77beda;">Main nahi ladunga.</span>” Aur woh chup ho gaya. <span style="color:#77beda;">Krishna</span> muskuraate hue <span style="color:#77beda;">Arjuna</span> se bolte hain, battlefield ke beech mein —
    us <span style="color:#77beda;">Arjuna</span> se jo toot gaya hai.
    """ 
    create_image_text_layout("attached_assets/generated_images/22.jpg", text2, layout="side", image_position="right")



    text3 = """
    <span style="color:#FF5733;">Shloka 2.11 to 2.15 : </span>
<span style="color:#77beda;">Krishna</span> kehte hain – “Tu jo shok kar raha hai, woh na samajhdari hai, na gyaan.
Jo mar chuke hain ya jo abhi jeevit hain — dono ke liye shok karna gyani ka kaam nahi hota.”
Main kabhi nahi tha aisa nahi, na tu, na ye raja.
Hum sab hamesha se the, aur aage bhi rahenge.
Jaise iss jeev ke shareer mein bachpan, jawani aur budhapa aata hai, waise hi yeh atma ek shareer se doosre mein jaati hai.
Jo gyani hai, woh iss par vichlit nahi hota.
Hey <span style="color:#77beda;">Arjuna</span>! Thand-garmi, sukh-dukh sab indriyon ke sparsh se aate hain — ye sab aanewaale jaane waale hai, isiliye inhe sehna seekho.
Hey <span style="color:#77beda;">Arjuna</span>! Jo sukh-dukh mein samaan rehta hai, jo stable hai — wahi amar-pad (<span style="color:#77beda;">moksha</span>) ka yogya banta hai.
    """
    create_image_text_layout("attached_assets/generated_images/23.jpg", text3, layout="side", image_position="left")

    text5 = """
    <span style="color:#FF5733;">Shloka 2.16 to 2.20 : </span>
Jhooth (<span style="color:#77beda;">asatya</span>) ka koi sthayi astitva nahi hai.
Satya (<span style="color:#77beda;">jo hai hi</span>) – woh kabhi khatam nahi hota.
Gyani is antar ko samajh lete hain.
Jis atma se poora jagat vyaapt hai, woh avinaashi hai. Uska koi vinaash nahi kar sakta.
Yeh shareer nashwar hai, par jo shareer ke andar (<span style="color:#77beda;">atma</span>) hai, woh anant hai, amulya hai.
Isliye <span style="color:#77beda;">Arjuna</span>! Tum apna karm karo.
Jo kehta hai ki “<span style="color:#77beda;">main kisi ko maar raha hoon</span>” ya “<span style="color:#77beda;">woh mar gaya</span>”, dono ko atma ka gyaan nahi hai.
Atma na kisi ko maarta hai, na khud marta hai.
Atma na kabhi janm leti hai, na kabhi merti hai.
Woh kabhi bani nahi, banegi nahi, woh hamesha thi, hai, aur rahegi.
Shareer ke marne par bhi woh nahi merti.
    """
    create_image_text_layout("attached_assets/generated_images/24.jpg", text5, layout="side", image_position="right")



    text6 = """
    <span style="color:#FF5733;">Shloka 2.21 to 2.25 : </span>
Hey <span style="color:#77beda;">Arjuna</span>! Jo jaanta hai ki atma naash nahi hoti, janm nahi leti, aur hamesha se hai — woh kisi ko kaise maar sakta hai, ya marne ki chinta kaise kar sakta hai? Jaise purane kapde utar kar insaan naye kapde pehenta hai, waise hi atma purane shareer chhod kar naye shareer le leti hai.
Atma ko na shastra kaat sakte hain, na aag jala sakti hai, na paani bhigo sakta hai, na hawa sukhha sakti hai.
Atma ko kaata nahi ja sakta, jalaya nahi ja sakta, sukhaya nahi ja sakta.
Woh hamesha rehti hai, har jagah hoti hai, sthir hai, achal hai, anadi hai.
Atma na dikhai deti hai, na sochi ja sakti hai, na badalti hai.
Isiliye, ise jaanne ke baad, tu ise le kar <span style="color:#77beda;">shok mat kar.</span>
    """
    create_image_text_layout("attached_assets/generated_images/25.jpg", text6, layout="side", image_position="left")



    text7 = """
    <span style="color:#FF5733;">Shloka 2.26 to 2.30 : </span>
Agar tu yeh maan bhi le ki atma baar-baar janm leti hai ya baar-baar marti hai — tab bhi tujhe shok nahi karna chahiye.Jo paida hua hai, uska marna nishchit hai.
Jo mar gaya hai, uska phir se janm bhi <span style="color:#77beda;">nishchit</span> hai.
Isiliye, jo badalne se nahi rok sakte, uske liye shok mat kar. Sab jeev avyakta (<span style="color:#77beda;">invisible</span>) roop mein aate hain, beech mein kuch samay dikhte hain, fir phir se avyakta ho jaate hain.
Toh fir iss <span style="color:#77beda;">natural process</span> par shok kyu?Kuch log atma ko chamatkar samajhkar dekhte hain, kuch chamatkar samajhkar bolte hain, kuch sunte hain – par bahut kam log hote hain jo use samajh paate hain. Yeh deh mein rehne wali atma sab jagah nitya aur amar hai.
Isliye <span style="color:#77beda;">Arjuna</span>! Kisi bhi jeev ke liye tu shok mat kar.
    """
    create_image_text_layout("attached_assets/generated_images/26.jpg", text7, layout="side", image_position="right")


    text9 = """
    <span style="color:#FF5733;">Shloka 2.31 to 2.35</span> <br>
Apna swadharma dekhkar tumhe ghabraana nahi chahiye.
Ek <span style="color:#77beda;">kshatriya</span> ke liye dharm yudh se bada koi karma nahi hota. Hey <span style="color:#77beda;">Arjuna</span>! Aisa yudh to swarg ka dwar kholta hai.
Kshatriya ke liye aise yudh milna khushkismati hai. Agar tumne yeh dharm-yudh nahi kiya, toh tum apna farz bhi chhoge aur naam bhi.
Aur paap ka bhaag bhi banoge. Log tumhara naam badnam karenge – aur ek maan-samman waale veer ke liye badnaami, mrityu se bhi zyada dardnaak hoti hai. Tumhare dushman bhi kahenge ki <span style="color:#77beda;">Arjuna battlefield</span> se bhay ke kaaran bhaag gaya.
Ek maha-veer ka yeh kaam nahi hota.
    """
    create_image_text_layout("attached_assets/generated_images/27.jpg", text9, layout="side", image_position="left")


    text10 = """
    <span style="color:#FF5733;">Shloka 2.36 to 2.40 : </span>
Log tumhare viruddh anuchit baatein bolenge, tumhari ninda karenge – aur yeh sab tumhe aur bhi zyada dukh degi. Ya toh tum mar kar swarg jaoge, ya jeet kar prithvi par raajya karoge.
Isliye, <span style="color:#77beda;">Arjuna</span>! Utho aur nishchay ke saath yudh karo. Sukh-dukha, jeet-haar, laabh-haani – sabko samaan samajhkar yudh karo.
Tabhi tum paap ke patra nahi banoge. Ab tak maine tumhe Sankhya (<span style="color:#77beda;">gyan yog</span>) bataya, ab yog (<span style="color:#77beda;">karma yog</span>) suno.
Is buddhi ke dwara tum karma-bandhan se mukt ho jaoge. Is yog (<span style="color:#77beda;">karma yog</span>) mein kabhi koi nuksaan nahi hota, koi vipatti nahi aati.
Ismein thoda bhi kiya gaya dharm, bade se bade bhay se bacha leta hai.
    """
    create_image_text_layout("attached_assets/generated_images/28.jpg", text10, layout="side", image_position="right")

    text11 = """
    <span style="color:#FF5733;">Shloka 2.41 to 2.45 : </span>
Hey <span style="color:#77beda;">Arjuna</span>! Yogi ki buddhi ek lakshya par kendrit hoti hai.
Parantu nirnayheen logon ki buddhi anek shakhaon mein bhatakti hai. Jo log gyaan se pare hote hain, woh vedon ke sundar shabdon mein hi atke rahte hain.
Unka kehna hai – ved ke alawa kuch nahi. Aise log jo swarg, sukh aur bhog ke liye kaam karte hain, unka dhyaan bas karam ke phal par hota hai.
Woh shabd aur kriyaon mein atak jaate hain. Jo log bhog-vilās aur aishwarya mein atke hote hain, unka man chanchal ho jaata hai.
Aise log ekagrata (<span style="color:#77beda;">samādhi</span>) nahi laa paate. Ved gunon (<span style="color:#77beda;">sattva, rajas, tamas</span>) mein le jaate hain.
Par tu un teenon se upar uth ja, <span style="color:#77beda;">Arjuna</span>.
Dwandvatit (<span style="color:#77beda;">joy-sorrow se pare</span>), sthir aur atmasth ban.
    """
    create_image_text_layout("attached_assets/generated_images/29.jpg", text11, layout="side", image_position="left")



    text12 = """
    <span style="color:#FF5733;">Shloka 2.46 to 2.50 : </span>
    Jis tarah ek talaab ka paani samundar ke samne chhota lagta hai, waise hi ek gyani ke liye sab ved bhi seemit lagte hain.
    Tera adhikaar sirf karm karne tak hai, uske phal par nahi.
Karm ka phal chahna mat, par karm se door bhi mat ho.
Hey <span style="color:#77beda;">Dhananjay</span>! (<span style="color:#77beda;">Arjuna</span>)
Karma ko yog mein sthit ho kar kar – asakt hokar.
Safalta-viaphalata mein samaan rehna – yehi yog hai. Hey <span style="color:#77beda;">Arjuna</span>! Buddhi yog se kiya gaya karm, moha se kiye gaye karm se bahut uncha hai.
Jo sirf phal ke liye kaam karte hain, woh kripana (<span style="color:#77beda;">deen</span>) hain.
Jo buddhi yog se karm karta hai, woh safalta aur asafalta – dono ke doshon se mukt ho jaata hai.
Isliye yog mein sthit ho kar karm karo – yog ka arth hai: karm mein kaushal.
    """
    create_image_text_layout("attached_assets/generated_images/210.jpg", text12, layout="side", image_position="right")


    text13 = """
    <span style="color:#FF5733;">Shloka 2.51 to 2.55 : </span>
Jo karm yogi gyaan ke saath karm karta hai, aur phal bhagwan ko arpit karta hai – woh janm ke bandhan se mukt ho jaata hai, aur dukh-rahit param-pada ko prapt karta hai.
Jab tumhara gyaan moh (<span style="color:#77beda;">illusion</span>) ke jungle se paar nikal jaata hai, tab tum shrut aur ashrut (<span style="color:#77beda;">sunna, padhna, dharm-granth</span>) sabse upar uth jaate ho.
Jab tumhara mann har taraf se sunayee dene wale <span style="color:#77beda;">confusion</span> se bahar aa kar ek jagah tik jaata hai – tab tum yogi ban jaate ho.
<span style="color:#77beda;">Arjuna</span> poochta hai – Hey <span style="color:#77beda;">Keshav</span>! Ek sthit-pragya yogi ka vyavhaar kaisa hota hai?
Woh bolta kaise hai, baithta kaise hai, chalta kaise hai?
Jab insaan mann ke sabhi ichchhaon ka tyag kar deta hai, aur atma mein hi tript rehta hai, tab use sthitpragya (<span style="color:#77beda;">stable-intellect</span>) kehte hain.
    """
    create_image_text_layout("attached_assets/generated_images/211.jpg", text13, layout="side", image_position="left")


    text14 = """
    <span style="color:#FF5733;">Shloka 2.56 to 2.60 : </span>
Jo dukh mein ghabrata nahi, sukh mein lobh nahi karta, raga-bhay-krodh se mukt ho jaata hai – woh sthit-dhi yogi hai. Jo kisi bhi cheez mein asakti nahi rakhta – na shubh par harsh, na ashubh par ghrina – uski buddhi sthir hai. Jaise <span style="color:#77beda;">kachhua</span> apne haath-pair samet leta hai, waise hi yogi apni indriyon ko vishayon se hata leta hai. Insaan indriyon se vishay to hata leta hai, lekin uska ras (<span style="color:#77beda;">taste</span>) chhuta nahi.
Woh tabhi chhoot-ta hai jab woh usse uchchatar anubhav (<span style="color:#77beda;">atma-gyaan</span>) prapt karta hai. Hey <span style="color:#77beda;">Arjuna</span>! Yog mein sthit vyakti bhi agar saavdhan na rahe, to uski indriyaan uska mann kheench leti hain.
    """
    create_image_text_layout("attached_assets/generated_images/212.jpg", text14, layout="side", image_position="right")


    text15 = """
    <span style="color:#FF5733;">Shloka 2.61 to 2.65 : </span>
Jo vyakti sabhi indriyon ko vash mein karke, apna man mujhme (<span style="color:#77beda;">Krishna mein</span>) sthir karta hai – uski buddhi sthit hoti hai. Jab manushya vishayon ke baare mein baar-baar sochta hai, toh usmein asakti hoti hai.
Asakti se ichchha (<span style="color:#77beda;">kaam</span>) paida hoti hai, aur ichchha se krodh. Krodh se moh hota hai, moh se smriti bhram, smriti bhram se buddhi ka nash hota hai.
Aur jab buddhi nash ho jaaye, to manushya ka vinash nishchit hai. Jo manushya raga (<span style="color:#77beda;">asakti</span>) aur dvesh (<span style="color:#77beda;">ghrina</span>) se pare hoke indriyon se vishay ka upyog karta hai, woh prasannata (<span style="color:#77beda;">shanti</span>) paata hai. Jab mann shant aur prasanna hota hai, tab sabhi dukh mitne lagte hain.
Aur aise yogi ki buddhi mein sthirata aati hai.
    """
    create_image_text_layout("attached_assets/generated_images/213.jpg", text15, layout="side", image_position="left")


    text16 = """
    <span style="color:#FF5733;">Shloka 2.66 to 2.72 : </span>
Jo vyakti asanyamit hai, uske paas na to buddhi hoti hai, na bhakti.
Aur jisme bhakti nahi, usme shanti nahi. Jisme shanti nahi, usme sukh kaise? Jab mann indriyon ke peeche bhaagta hai, toh uska gyaan waisa hi ghoom jaata hai jaise paani mein <span style="color:#77beda;">tufaaan se naav</span>. Isliye hey <span style="color:#77beda;">Arjuna</span>! Jis vyakti ne apni sabhi indriyon ko vash mein kiya hai – wahi <span style="color:#77beda;">sthit-pragya</span> hai. Jo jagat ke liye raat hai (<span style="color:#77beda;">antar-mukh sthiti</span>), woh yogi ke liye din hai.
Aur jo jagat ke liye din hai (<span style="color:#77beda;">bhog, maya</span>), woh yogi ke liye andhkaar hai. Jaise samudra mein nadiyan girti rehti hain, par woh kabhi ubhalta nahi –
Waise hi yogi ke paas icchhaayein aati hain, par uska mann kabhi hilta nahi. Jo vyakti sabhi ichchhaon ka tyag karke, asakti, mamta aur ahankaar se mukt ho kar jeeta hai – wahi param shanti paata hai. Jo vyakti sabhi ichchhaon ka tyag karke, asakti, mamta aur ahankaar se mukt ho kar jeeta hai – wahi <span style="color:#77beda;">param shanti</span> paata hai.
    """
    create_image_text_layout("attached_assets/generated_images/214.jpg", text16, layout="side", image_position="right")



    create_image_text_layout("attached_assets/generated_images/2banner.jpg", layout="full")


