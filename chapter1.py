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
    create_image_text_layout("attached_assets/generated_images/1.jpg", layout="full")


    text0 = """
    <h2>Chapter 1: Arjuna Vishada Yoga (Arjuna's Distress)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <span style="color:#FF5733;">Shloka 1.1 to 1.5 : </span>
    Kurukshetra ek battlefield hai — lekin Geeta usse kehti hai “Dharmakshetra” — jahan yudh sirf talwaron se nahi, andar ke sach aur bahar ke farz ke beech hota hai.
    Pandavon ki army ko perfect formation mein dekhkar <span style="color:#77beda;">Duryodhan</span> ghabrata hai aur Guru <span style="color:#77beda">Dronacharya</span> ke paas jaata hai.
    <span style="color:#77beda;">Duryodhan</span> apne Guru se kehta hai — dekhiye, aapke hi student (Drupadputra) ne yeh sena sajayi hai!
    Yeh sena <span style="color:#77beda;">Bhima</span> aur <span style="color:#77beda;">Arjuna</span> jaise warriors se bhari hai — yeh sab maha-shaktishaali hai.
    Aur bhi kai brave fighters hain — <span style="color:#77beda;">Kashi Raja, Dhrishtaketu, Chekitana, Purujit…</span>
    """ 
    create_image_text_layout("attached_assets/generated_images/11.jpg", text1, layout="side", image_position="left")


    text2 = """
    <span style="color:#FF5733;">Shloka 1.6 to 1.10 : </span>
    Yeh army nayi generation se bhi strong hai — <span style="color:#77beda;">Abhimanyu</span>, Draupadi ke putra — sab maharathi. 
    Ab main aapko apni sena ke best fighters batata hoon…
    Hamare paas bhi <span style="color:#77beda;">Bhishma, Karna, Kripacharya</span>  jaise mahaan warriors hain.
    Aur bhi kai warriors hain jo mere liye apni jaan tak dene ko ready hain.
    Hamari sena <span style="color:#77beda;">Bheeshma</span>  ke hote hue bhi thodi kamzor lagti hai; unki sena <span style="color:#77beda;">Bhima</span> ke sahare bhi strong hai.
    """ 
    create_image_text_layout("attached_assets/generated_images/12.jpg", text2, layout="side", image_position="right")



    text3 = """
    <span style="color:#FF5733;">Shloka 1.11 to 1.15 : </span>
    <span style="color:#77beda;">Duryodhan</span> bolta hai: “Sabhi yoddha apne-apne moorchha sthano par khade ho jaayein — aur sabse pehle <span style="color:#77beda;">Bheeshma Pitamah</span> ki raksha karein!”
    <span style="color:#77beda;">Bheeshma Pitamah</span> ne sher ki ghoṣh jaise garaj kar apna shankh bajaya — isse sabhi ka utsaah badh gaya.
    Shankh, bheri, dhol, turahi — sab ek saath baj uthe. Poora maidan shabd se goonj utha.
    <span style="color:#77beda;">Krishna</span> (Madhav) aur <span style="color:#77beda;">Arjuna</span> apne safed ghodon wale rath mein khade hote hain, aur dono apne divya shankh bajate hain.
    <span style="color:#77beda;">Krishna</span> ne Panchajanya shankh bajaya, <span style="color:#77beda;">Arjuna</span> ne Devadatta bajaya, <span style="color:#77beda;">Bhima</span> ne maha shankh Paundra bajaya.
    """
    create_image_text_layout("attached_assets/generated_images/13.jpg", text3, layout="side", image_position="left")

    text5 = """
    <span style="color:#FF5733;">Shloka 1.16 to 1.20 : </span>
    Poore Pandav paksh se har yoddha apne-apne shankh bajata hai. Ye unity aur ready hone ka sanket hai.
    Shankhon ki goonj itni zordaar thi ki <span style="color:#77beda;">Duryodhan</span> ke logon ke dil kaanp gaye. Dharti aur aakash bhi goonj uthe.
    Kapidhwaj (<span style="color:#77beda;">Arjuna</span>) ne <span style="color:#77beda;">Duryodhan</span> ke sainikon ko vyavasthit dekha, aur usne apna dhanush utha liya.
    """
    create_image_text_layout("attached_assets/generated_images/14.jpg", text5, layout="side", image_position="right")



    text6 = """
    <span style="color:#FF5733;">Shloka 1.21 to 1.25 : </span>
    <span style="color:#77beda;">Arjuna</span> kehta hai — “Hey <span style="color:#77beda;">Krishna</span>! Mera rath dono senaon ke beech le chalo, taaki main dekh sakun ki mujhe kinse yudh karna hai.
    <span style="color:#77beda;">Arjuna</span> kehta hai — “Main dekhna chahta hoon in logon ko jo <span style="color:#77beda;">Duryodhan</span> ke paksh mein khade hain aur is anyaay ke yudh mein uske liye lad rahe hain.
    <span style="color:#77beda;">Sanjay</span> kehta hai — Arjuna ke kehne par Krishna ne rath dono senaon ke beech khada kar diya.
    <span style="color:#77beda;">Krishna</span> ne rath ko <span style="color:#77beda;">Bheeshma</span> aur <span style="color:#77beda;">Dronacharya</span> ke saamne roka, aur kaha:
    “Hey <span style="color:#77beda;">Arjuna</span>, dekho in Kuru yoddhaon ko.”
    """
    create_image_text_layout("attached_assets/generated_images/15.jpg", text6, layout="side", image_position="left")



    text7 = """
    <span style="color:#FF5733;">Shloka 1.26 to 1.30 : </span>
    <span style="color:#77beda;">Arjuna</span> dekhta hai — mere pita, dada, guru, mama, bhai, putra, dost… sabhi saamne yudh ke liye khade hain!
    <span style="color:#77beda;">Arjuna</span> dono pakshon mein apne rishte ke logon ko dekh kar hil jaata hai.
    <span style="color:#77beda;">Arjuna</span> kehta hai — “Hey <span style="color:#77beda;">Krishna</span>, in apno ko yudh ke liye tayyar dekhkar mera hriday dukh se bhar gaya hai.”
    Mera Gandiva dhanush haath se chhoot raha hai, meri twacha jal rahi hai, main khada bhi nahi reh pa raha hoon. Mera mann ghoom raha hai.
    “Hey <span style="color:#77beda;">Krishna</span>, main har taraf ashubh sanket dekh raha hoon. Apne hi logon ko maarna mujhe theek nahi lagta.”
    """
    create_image_text_layout("attached_assets/generated_images/16.jpg", text7, layout="side", image_position="right")


    text9 = """
    <span style="color:#FF5733;">Shloka 1.31 to 1.35 : </span>
    Hey <span style="color:#77beda;">Krishna</span>! Mera mann ghoom raha hai, main khada tak nahi reh paa raha. Mujhe har taraf ashubh sanket dikh rahe hain.
    Hey <span style="color:#77beda;">Krishna</span>! Mujhe na jeet chahiye, na rajya, na sukh. Jin ke liye yeh sab chahiye tha, wohi toh yehan mere saamne khade hain — apna pran aur dhan tyag karne ke liye!
    Hey <span style="color:#77beda;">Krishna</span>! Apne guru, pita, pitaamah, beta, rishtedaar… in sab ko maarna main nahi chahta — chahe mujhe teenon lokon ka rajya hi kyun na mil jaaye.
    """
    create_image_text_layout("attached_assets/generated_images/17.jpg", text9, layout="side", image_position="left")


    text10 = """
    <span style="color:#FF5733;">Shloka 1.36 to 1.40 : </span>
    Hey <span style="color:#77beda;">Krishna</span>! <span style="color:#77beda;">Duryodhan</span> aur uske bhaiyon ko maar kar mujhe kya milega? Mujhe lagta hai ki usse toh sirf paap hi milega.
    Hey <span style="color:#77beda;">Krishna</span>! Chahe <span style="color:#77beda;">Duryodhan</span> log lalach mein andhe ho gaye ho, par hum toh samajhdar hain — fir hum apno ko kaise maar sakte hain?
    Jab ek kul (vansh/parivaar) ka vinaash hota hai, tab uske saare dharm (parampara aur sanskaar) bhi mit jaate hain. Aur jab dharm nahi hota, tab adharm badhta hai.
    Hey <span style="color:#77beda;">Krishna</span>! Jab adharm badhta hai, to kul ki striyan bhi durgati ko prapt hoti hain, aur usse samajik vyavastha (varna sankar) bigad jaata hai.
    """
    create_image_text_layout("attached_assets/generated_images/18.jpg", text10, layout="side", image_position="right")

    text11 = """
    <span style="color:#FF5733;">Shloka 1.41 to 1.47 : </span>
    <span style="color:#77beda;">Arjuna</span> kehta hai — jab kul ki striyan patit hoti hain, to unse paida hone wali peedhiyan bigad jaati hain. Aur aise log narak ke patra bante hain. Pitraon ke liye kriya bhi band ho jaati hai.
    Jab varna sankar badhta hai (sanskaar bigad jaate hain), tab samaj ke jati-dharma aur kul-dharma bhi khatam ho jaate hain.
    Hey <span style="color:#77beda;">Krishna</span>! Maine suna hai ki jinka kul-dharm nasht ho jaata hai, unka sthayi vaas narak mein hota hai.
    <span style="color:#77beda;">Arjuna</span> kehta hai — kitna bada paap hai yeh! Hum rajya aur sukh ke lobh mein apne hi logon ko maarne ja rahe hain!
    <span style="color:#77beda;">Arjuna</span> kehta hai — agar <span style="color:#77beda;">Duryodhan</span> mujhe bina hathiyar uthaye hi maar de battlefield mein, toh mujhe woh zyada shanti dega.
    <span style="color:#77beda;">Sanjaya</span> kehta hai — yeh sab kehkar <span style="color:#77beda;">Arjuna</span> ne apna dhanush-baan chhod diya, rath ke upar baith gaya. Uska mann shok se bhara tha.
    """
    create_image_text_layout("attached_assets/generated_images/19.jpg", text11, layout="side", image_position="left")

    create_image_text_layout("attached_assets/generated_images/1banner.jpg", layout="full")

