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
    create_image_text_layout("attached_assets/generated_images/3.jpg", layout="full")


    text0 = """
    <h2>Chapter 3: Karma Yoga (Yoga of Action)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <span style="color:#FF5733;">Shloka 3.1 to 3.5 : </span>
    <span style="color:#77beda;">Arjuna</span> kehta hai – Hey <span style="color:#77beda;">Krishna</span>! Agar buddhi (<span style="color:#77beda;">gyaan</span>) karm se uttam hai, toh phir mujhe yeh bhayanak karm (<span style="color:#77beda;">yudh</span>) mein kyun laga rahe ho? <span style="color:#77beda;">Arjuna</span> bolta hai – Aapki baatein mujhe uljhan mein daal rahi hain.
Kripya karke ek nischit marg batayein jo mere liye shreyaskari ho. Hey <span style="color:#77beda;">Arjuna</span>! Yeh sansaar mein maine do marg bataye hain —
<span style="color:#77beda;">Gyaan Yog</span> (<span style="color:#77beda;">inner wisdom, contemplation</span>) un logon ke liye jo vivek mein sthir hain,
Aur <span style="color:#77beda;">Karma Yog</span> (<span style="color:#77beda;">selfless action</span>) unke liye jo karm ke madhyam se mukti chahte hain. Karm na karne se koi insaan karm-rahit (<span style="color:#77beda;">naishkarmya</span>) nahi ho jaata.
Sirf sannyas (kaam chhod dena) se bhi siddhi (<span style="color:#77beda;">moksha</span>) nahi milti. Koi bhi jeev ek kshan bhi bina karm ke nahi reh sakta.
Prakriti ke gunon ke prabhav se sabhi log avashya karm karte hain.
    """ 
    create_image_text_layout("attached_assets/generated_images/31.jpg", text1, layout="side", image_position="left")


    text2 = """
    <span style="color:#FF5733;">Shloka 3.6 to 3.10 : </span>
Jo vyakti karm ke indriyon ko roke rakhta hai, par mann se vishayon ka smaran karta hai – <span style="color:#77beda;">woh moorkh hai</span>, aur uska acharan mithya hai. Hey <span style="color:#77beda;">Arjuna</span>! Jo vyakti indriyon ko niyantrit karke, asakti rahit hokar karm karta hai – wahi karma yogi hai, aur <span style="color:#77beda;">wahi shrēṣṭh hai</span>. Tum apna niyamit karm karo, kyunki karm na karne se achha hai karm karna.
Bina karm ke to tum apne sharir ka gujara bhi nahi kar sakte. Hey <span style="color:#77beda;">Arjuna</span>! Yagya bhav (<span style="color:#77beda;">bhagwan ke liye</span>), seva bhav se kiya gaya karm hi bandhan se mukt karta hai.
Jo karm apne liye hota hai, woh bandhan ban jaata hai. Srushti ke prarambh mein Prajapati (<span style="color:#77beda;">Brahma</span>) ne manushyon ke saath hi yagya (seva-bhav) ka niyam bhi sthapit kiya.
Usi se tumhara jeevan safal hoga, aur tumhari ichchhayein poori hongi.
    """ 
    create_image_text_layout("attached_assets/generated_images/32.jpg", text2, layout="side", image_position="right")



    text3 = """
    <span style="color:#FF5733;">Shloka 3.11 to 3.15 : </span>
Tum <span style="color:#77beda;">yagya bhav</span> se devtaon ko samarpit karm karo, ve bhi tumhara palan karenge.
Ek doosre ko sahyog karke, tum shreya (<span style="color:#77beda;">uttam fal</span>) prapt karoge. Yagya bhav se santusht devta tumhe bhog dete hain.
Par jo insaan un bhogon ko devta ko bina arpit kiye bhogta hai – <span style="color:#77beda;">woh chor hai</span>. Jo log yagya bhav se arpit karke bacha hua ann khaate hain, woh paapon se mukta hote hain.
Par jo apne liye hi pakate hain, <span style="color:#77beda;">woh paapi hain</span>. Sab prani ann se palte hain, ann barish se hota hai, barish yagya se hoti hai, aur yagya karm se. Karm ka janm Brahma (<span style="color:#77beda;">Veda</span>) se hua hai, aur Veda ka mool Akshar Brahma (<span style="color:#77beda;">Ishwar</span>) hai.
Isliye Brahma (<span style="color:#77beda;">divine essence</span>) hamesha yagya mein sthit hai.
    """
    create_image_text_layout("attached_assets/generated_images/33.jpg", text3, layout="side", image_position="left")

    text5 = """
    <span style="color:#FF5733;">Shloka 3.16 to 3.20 : </span> 
Jo vyakti is <span style="color:#77beda;">yagya-chakra</span> ka paalan nahi karta, aur sirf indriyon ka sukh chaahta hai – uska jeevan vyarth hai. Jo vyakti apne aap mein tript hai, aur swayam mein hi santusht hai – uske liye koi bhi kartavya bacha nahi hota. Jo vyakti atmarati hai (<span style="color:#77beda;">atma mein hi anandit</span>), uska na karm se koi matlab hota hai, na akarm se.
Woh kisi aur par depend nahi hota. Isliye tum <span style="color:#77beda;">asakti rahit</span> hokar apna kartavya karm nirantar karo,
kyunki aise hi vyakti param gati (<span style="color:#77beda;">moksha</span>) ko prapt karta hai. <span style="color:#77beda;">Raja Janak</span> jaise mahan log bhi karm karke siddhi ko prapt hue the.
Tumhe bhi, <span style="color:#77beda;">Arjuna</span>, lok-sangrah (<span style="color:#77beda;">logon ke hit)</span>) ke liye karm karna chahiye.
    """
    create_image_text_layout("attached_assets/generated_images/34.jpg", text5, layout="side", image_position="right")



    text6 = """
    <span style="color:#FF5733;">Shloka 3.21 to 3.25 : </span> 
Jo vyakti shrēṣṭh hai, jaisa karm karta hai, samaanya log uska <span style="color:#77beda;">anukaran</span> karte hain.
Jo vyakti standard set karta hai, samaaj usi raaste par chalta hai. Hey <span style="color:#77beda;">Arjuna</span>! Mujhe teenon lok mein kuch bhi prapt karna baaki nahi hai.
Phir bhi main karm karta hoon. Hey <span style="color:#77beda;">Arjuna</span>! Agar main karm mein lagaatar na rahun, toh log mere marg ka anukaran kaise karenge? Agar main karm na karun, toh yeh sabhi lok vinaash ko prapt honge.
Main kul-vyavastha ka vinaash karne wala ban jaunga. Hey <span style="color:#77beda;">Arjuna</span>! Agyani vyakti mohit hoke karm karta hai,
lekin gyaani bhi karm karta hai – bina asakti ke, samaj ke hit ke liye.
    """
    create_image_text_layout("attached_assets/generated_images/35.jpg", text6, layout="side", image_position="left")



    text7 = """
    <span style="color:#FF5733;">Shloka 3.26 to 3.30 : </span>
Gyaani log agyani logon ki buddhi mein bhranti na daalein.
Wo unhe unke karm ke marg par hi shuddh bhavna se chalayein. Prakriti ke gun (<span style="color:#77beda;">sattva, rajas, tamas</span>) hi sab karm karte hain.
Lekin ahankaar mein mohit vyakti kehta hai: “<span style="color:#77beda;">Main hi karta hoon.</span>” Jo tattva-darshi (<span style="color:#77beda;">gyaani</span>) hai, woh jaanta hai ki prakriti ke gunon se karm ho raha hai,
isliye woh usmein asakt nahi hota. Jo log moh mein uljhe hain, woh prakriti ke karm mein hi asakti rakhte hain.
Tum unhe confuse na karo, unka dhire-dhire margdarshan karo. Hey <span style="color:#77beda;">Arjuna</span>! Apna poora man mujhme lagao, karm mujhe samarpit karo,
nirasha aur nirmam hokar, aur chinta-mukt hokar yudh karo.
    """
    create_image_text_layout("attached_assets/generated_images/36.jpg", text7, layout="side", image_position="right")


    text9 = """
    <span style="color:#FF5733;">Shloka 3.31 to 3.35 : </span>
Jo log meri is Gita ki baaton ko shraddha se, bina ninda ke <span style="color:#77beda;">follow</span> karte hain,
Woh bhi sabhi <span style="color:#77beda;">karm-bandhanon</span> se mukta ho jaate hain. Jo log mere is gyaan mein dosh dekhte hain, aur usse nahi maante —
Samjho wo moorkh hain, aur apna vinash kar rahe hain. <span style="color:#77beda;">Gyaani vyakti</span> bhi apni prakriti ke anusaar hi kaam karta hai.
Sab prani prakriti ke hi adheen hote hain — bas <span style="color:#77beda;">repression</span> se kuch nahi hota. Har indriya apne vishay mein raga (<span style="color:#77beda;">aakarshan</span>) aur dvesh (<span style="color:#77beda;">ghrina</span>) rakhti hai.
Insaan ko unke vas mein nahi aana chahiye — ye hi uske marg ke dushman hain. Apna dharm (<span style="color:#77beda;">kartavya</span>), chahe usmein kami ho, fir bhi doosron ke dharm se uttam hai.
Apne dharm mein mar jaana bhi shreyaskari hai — doosron ka dharm bhayankar hota hai.
    """
    create_image_text_layout("attached_assets/generated_images/37.jpg", text9, layout="side", image_position="left")


    text10 = """
    <span style="color:#FF5733;">Shloka 3.36 to 3.43 : </span>
<span style="color:#77beda;">Arjuna</span> puchta hai – Hey <span style="color:#77beda;">Krishna</span>! Insaan ichcha na hone par bhi paap kyun karta hai?
Kaunsi shakti usse balpurvak paap karwata hai? <span style="color:#77beda;">Krishna</span> kehte hain – Ye kaam (<span style="color:#77beda;">ichchha</span>) aur usse utpann krodh, rajo-gun se paida hote hain.
Ye atyant lobhi, maha-paapi aur tumhara <span style="color:#77beda;">sabse bada shatru</span> hai. Jaise agni ko dhuaan chhupa leta hai, jaise darpan ko mail dhundhla kar deta hai,
waise hi kaam gyaan ko chhupa deta hai. Hey <span style="color:#77beda;">Arjuna</span>! Ye kaam-roopi agni gyaani ke bhi gyaan ko chhupa leta hai.
Ye asantusht rehne wali agni jaisa hai — jo kabhi nahi bharta. Kaam ka sthaan indriyaon, mann aur buddhi mein hai.
Ye wahin se gyaan ko chhupata hai, aur manushya ko mohit karta hai. Isliye, hey <span style="color:#77beda;">Arjuna</span>! Sabse pehle indriyon ko niyantrit karo.
Tabhi is gyaan-vighna paapi kaam par vijay paayi ja sakti hai. Indriyon se mann shreshth hai, mann se buddhi, aur buddhi se bhi <span style="color:#77beda;">paramaatma</span> uttam hai. Is prakaar buddhi se upar Atma ko samajhkar, Atma se apne aap ko sthir karo.
Aur phir is dushman <span style="color:#77beda;">kaam roopi</span> durjey shatru ko maar daalo.
    """
    create_image_text_layout("attached_assets/generated_images/38.jpg", text10, layout="side", image_position="right")



    create_image_text_layout("attached_assets/generated_images/3banner.jpg", layout="full")
