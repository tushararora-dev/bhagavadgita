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
    create_image_text_layout("attached_assets/generated_images/11main.jpg", layout="full")


    text0 = """
    <h2>Chapter 11: Vishwarupa Darshana Yoga (Vision of the Cosmic Form)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <span style="color:#FF5733;">Shloka 11.1 to 11.5 : </span>
Hey <span style="color:#77beda;">Krishna</span>! Aapne jo mujhe adhyatma gyaan diya — usse mera moha (<span style="color:#77beda;">bhram</span>) chala gaya hai.
Main ab samajh gaya hoon ki aap sabke mool ho. Hey <span style="color:#77beda;">Kamalnayan</span>! Aapne jo mujhe jeevon ke utpatti (<span style="color:#77beda;">creation</span>), lay (<span style="color:#77beda;">destruction</span>) aur vibhooti batayi hai —
usko sun kar main chakit hoon. Hey <span style="color:#77beda;">Purushottam</span>! Mujhe aapka woh divya roop dekhna hai
— jismein aap sab kuch mein vyapak ho — <span style="color:#77beda;">“Vishwaroop”</span>. Hey <span style="color:#77beda;">Yogeshwar</span>! Agar aap mujhe yogy samajhte ho,
to kripya mujhe apne avyay roop ka darshan dijiye. Hey <span style="color:#77beda;">Arjuna</span>! Ab mere anek roopon ko dekh —
Hazaron divya, rang-birange, roop-roop wale svaroop.
    """ 
    create_image_text_layout("attached_assets/generated_images/111.jpg", text1, layout="side", image_position="left")

    text2 = """
    <span style="color:#FF5733;">Shloka 11.6 to 11.10 : </span>
Main tujhe aise roop dikhaunga jo tune kabhi dekhe hi nahi —
<span style="color:#77beda;">Aditya, Vasu, Rudra, Marut, Ashwini Kumars</span> — sab kuch ek saath! Hey <span style="color:#77beda;">Arjuna</span>! Is mere sharir mein hi tu poora jagat dekh sakta hai —
Chal (<span style="color:#77beda;">moving</span>), achal (<span style="color:#77beda;">on-moving</span>n), sab kuch ek sath. Is Vishwaroop ko aam aankhon se dekhna asambhav hai —
Main tujhe ab divya drishti deta hoon, jisse tu meri yog-shakti ka anubhav kar sake. Hey Raja (<span style="color:#77beda;">Dhritarashtra</span>)! Tab <span style="color:#77beda;">Yogeshwar Hari</span> ne <span style="color:#77beda;">Arjuna</span> ko apna param divya roop dikhaya —
Jo sabse adhik adbhut tha. Us roop mein anek mukh, anek aankhen,
Anek adbhut roop, anek astr-shastron se bhara hua tha.
    """ 
    create_image_text_layout("attached_assets/generated_images/112.jpg", text2, layout="side", image_position="right")



    text3 = """
    <span style="color:#FF5733;">Shloka 11.11 to 11.15 : </span>
Main dekh raha hoon ek aisa roop jo
divya vastra, divya pushp, divya sugandh se sughandhit hai –
Har disha mein mukh (<span style="color:#77beda;">faces</span>) hain, har roop adbhut hai.
Woh Anant roop hai! Agar ek hi samay mein hazaar surya ek saath chamakne lagein,
Tab bhi us tej se <span style="color:#77beda;">Krishna</span> ke Vishwarup ka tej adhik hai. <span style="color:#77beda;">Arjuna</span> ne <span style="color:#77beda;">Krishna</span> ke sharir mein sab kuch dekha —
Poora jagat, sab log, sab dishaayein, sab roop — ek sath! <span style="color:#77beda;">Arjuna</span> romanch se bhara hua tha,
Usne haath jodkar Krishna ke samne pranaam kiya
Aur kampit swar mein bola. Hey <span style="color:#77beda;">Krishna</span>! Main tumhare sharir mein sab devta, praniyon ke samuh,
Brahmaji (<span style="color:#77beda;">kamal pe virajmaan</span>), sab rishi, aur divya naagon ko dekh raha hoon.
    """
    create_image_text_layout("attached_assets/generated_images/113.jpg", text3, layout="side", image_position="left")

    text5 = """
    <span style="color:#FF5733;">Shloka 11.16 to 11.20 : </span> 
Hey <span style="color:#77beda;">Vishweshwar</span>! Tumhara na aadi hai, na madhya, na ant.
Har disha mein main tumhara anant roop dekh raha hoon. Main tumhe mukut, chakra aur gada ke saath dekh raha hoon.
Tumhara tej agni aur surya ke saman hai —
Itna chamakdaar ki aankhon se dekhna kathin hai. Mere liye tum akshar (<span style="color:#77beda;">avinashi</span>), gyaan ka mool, sabka aadhar,
Sanatan dharm ke rakshak, aur sab mein vyaapak Purush ho. Tumhara koi aadi-madhya-ant nahi hai,
Tumhara shaktirup anant hai, aankhen surya-chandrama jaisi hain,
Tumhare mukh se agni jaise tej nikal raha hai,
Aur poore vishwa ko tapaa raha hai. Hey <span style="color:#77beda;">Mahatma</span>! Tumne poori dharti, aakash, aur dishaon ko gher liya hai.
Tumhara roop dekhkar teenon lok (<span style="color:#77beda;">swarg, mrityulok, paatal</span>) kaanp uthe hain.
    """
    create_image_text_layout("attached_assets/generated_images/114.jpg", text5, layout="side", image_position="right")



    text6 = """
    <span style="color:#FF5733;">Shloka 11.21 to 11.25 : </span> 
Sab devta tummein pravesh kar rahe hain.
Kuch bhay se haath jod rahe hain, kuch maharshi tumhari stuti kar rahe hain.
Sab log tumhare roop se ghabraye hue hain. Sab dev, yaksh, gandharv, siddh log –
Tumhe dekhkar vismit aur bhaybhit hain.
Sab jaane pehchaane roop tummein hi dikhayi de rahe hain. Main tumhara anek mukha, aankhon, haathon, pairon, daanton se bhara hua roop dekh raha hoon —
Aur yeh <span style="color:#77beda;">bhayankar aur mahaprakampan</span> roop mujhe kaanpa raha hai! Tumhara aakaash ko chhoone wala, tejomayi, roop-roop mein anek rangon wala roop
mujhe dara raha hai.
Meri man ki shanti aur sahas chali gayi hai. Tumhare daant aur agni jaisi jeebhayein mujhe kaal ke agni jaise lag rahe hain.
Main disha nahi samajh pa raha hoon.
Kripya kar ke mujhe shanti do, hey <span style="color:#77beda;">Jagannivasa</span>!
    """
    create_image_text_layout("attached_assets/generated_images/115.jpg", text6, layout="side", image_position="left")



    text7 = """
    <span style="color:#FF5733;">Shloka 11.26 to 11.30 : </span>
Main sab kuru ke putron ko – <span style="color:#77beda;">Bhishma, Drona, Karna aur anya</span> yoddhaon ke saath
tumhare bhayanak daant wale mukh mein daudte hue dekh raha hoon.
Kuch to crushed ho rahe hain tumhare daanton ke beech mein. Jese nadion ka jal samudra mein sama jaata hai,
Waise hi ye sab mahaan yoddha tumhare roop mein sama ja rahe hain. Jaise patang (<span style="color:#77beda;">keede</span>) aag mein girkar jal jaate hain,
Waise hi sab yoddha tumhare vaktra mein nash hone ke liye ja rahe hain. Tumhare agni se bhare mukh sab kuch nigalte ja rahe hain.
Sab kuch jal raha hai, aur yeh roop mujhe Kaal dikhayi deta hai.
    """
    create_image_text_layout("attached_assets/generated_images/116.jpg", text7, layout="side", image_position="right")


    text8 = """
    <span style="color:#FF5733;">Shloka 11.31 to 11.35 : </span>
Hey <span style="color:#77beda;">Dev</span>! Kripya mujhe batayein ki aap kaun hain?
Aapka roop to bhayankar hai.
Main samajh nahi pa raha — aapka uddeshya kya hai? Main Kaal hoon – samay roop se sab kuch khatam karne aaya hoon.
Ye sab yoddha, chahe tum yudh karo ya na karo, marne wale hain.
Main to bas niyati ka <span style="color:#77beda;">kaaryakari hoon</span>. Isliye <span style="color:#77beda;">Arjuna</span>! Utho, vijay aur yash prapt karo.
Shatruon ko main pehle hi maar chuka hoon —
Tum to bas ek zariya ho, ek nimitta. <span style="color:#77beda;">Dronacharya, Bhishma, Karna, Jayadrath</span> – sab mere dwara pehle hi samapt ho chuke hain.
Tum to bas apna karm karo, jeet tumhari hi hogi. <span style="color:#77beda;">Sanjay</span> kehta hai – <span style="color:#77beda;">Krishna</span> ke yeh vachan sun kar <span style="color:#77beda;">Arjuna</span> ne
kaampte haathon se pranaam kiya, aur kampit swar mein bola.
    """
    create_image_text_layout("attached_assets/generated_images/117.jpg", text8, layout="side", image_position="left")

    text9 = """
    <span style="color:#FF5733;">Shloka 11.36 to 11.40 : </span>
Hey <span style="color:#77beda;">Krishna</span>! Tumhara naam sun kar kuch log pramudit hote hain,
Aur kuch bhoot-pret aur rakshas disha chhod kar bhaag jaate hain. Hey <span style="color:#77beda;">Mahatma</span>! Jab tum Brahma ke bhi aadi ho,
Tab koi tumhe pranam kyun na kare?
Tum anant, akshar, jagat ka niwasi aur parama tattva ho. Tum aadi dev ho, puratan purush ho,
Sab kuch tum mein vyapak hai —
Tum hi gyaata bhi ho aur gyaeya bhi. Tum Vayu, Yama, Agni, Varun, Chandra, <span style="color:#77beda;">Brahma</span> – sab kuch ho!
Main tumhe hazaar baar pranam karta hoon, aur phir se karta hoon. Tum aage, peechhe, upar, neeche, sab dishaon mein ho.
Tum sab kuch ho, aur sab kuch tum mein hai.
Tumhe anant baar pranam karta hoon.
    """
    create_image_text_layout("attached_assets/generated_images/118.jpg", text9, layout="side", image_position="right")


    text10 = """
    <span style="color:#FF5733;">Shloka 11.41 to 11.45 : </span>
Hey <span style="color:#77beda;">Krishna</span>! Main tumhe mitra samajhkar “<span style="color:#77beda;">Hey Krishna, Hey Yadav, Hey Sakha</span>” kehkar jo bhi bola –
Woh ya to prem mein, ya anjaan hokar, ya bina soch samajh ke kaha.
Mujhe maaf karo. Chahe mazaak mein, ya sath baithne, sone, khane ke samay,
Mainne jo bhi tumhara apmaan kiya ho —
Hey <span style="color:#77beda;">Achyut</span>! Uske liye main kshama maangta hoon. Tum is poore jagat ke pita ho — chal aur achal sab tumhare roop mein hai.
Tumse bada koi guru, koi dev, koi prabhaav nahi ho sakta.
Teenon lokon mein tumhara tulya koi nahi! Main tumse vinti karta hoon — jaise pita apne putr ke aparadh ko maaf karta hai,
Waise hi mujhe bhi maaf karo, hey <span style="color:#77beda;">Devesh</span>! Tumhara vishwarup dekhkar main ek taraf romanchit hoon,
Par doosri taraf bhay se kaamp raha hoon.
Ab kripya apna woh shaant roop dikhao.
    """
    create_image_text_layout("attached_assets/generated_images/119.jpg", text10, layout="side", image_position="left")

    text11 = """
    <span style="color:#FF5733;">Shloka 11.46 to 11.50 : </span>
Hey <span style="color:#77beda;">Krishna</span>! Main tumhe mukut-dhari, chakra-gada-dhari, muskurata hua roop mein dekhna chahta hoon.
Wahi chaar bhujaon wala roop dikhao. Hey <span style="color:#77beda;">Arjuna</span>! Tumne jo roop dekha hai — woh sirf meri kripa se hi sambhav hai.
Yeh roop kisi aur ne kabhi nahi dekha. Na ved paath, na yajna, na daan, na kathin tapasya —
Is roop ko dekhna sirf bhakti se hi sambhav hai. <span style="color:#77beda;">Arjuna</span>! Ab daro mat. Main tumhara priya mitra hoon.
Main apna wahi purana roop phir se prakat kar raha hoon. <span style="color:#77beda;">Krishna</span> ne apna shaant, madhur, manav roop phir se dikhaya.
<span style="color:#77beda;">Arjuna</span> ko dar se mukti di, aur use aashwasan diya.
    """
    create_image_text_layout("attached_assets/generated_images/1110.jpg", text11, layout="side", image_position="right")

    text12 = """
    <span style="color:#FF5733;">Shloka 11.51 to 11.55 : </span>
Ab jab main tumhara manav roop dekh raha hoon,
To mera mann shaant ho gaya hai. Ab main punah apne swaroop mein aa gaya hoon. Tumne jo roop dekha, woh devta bhi dekhne ko taraste hain.
Yeh roop bahut durlabh hai. Main na to ved se, na tapasya se, na daan se milta hoon —
Sirf bhakti se mujhe is roop mein dekha ja sakta hai. Hey <span style="color:#77beda;">Arjuna</span>! Mujhe ananya bhakti se hi jaana, dekha, aur prapt kiya ja sakta hai. Jo vyakti <span style="color:#77beda;">Krishna</span> ke liye karm karta hai, jo mujhse ananya prem karta hai,
Jo sabse nishkaam aur nirvaira ho – wahi mujhe prapt karta hai.
    """
    create_image_text_layout("attached_assets/generated_images/1111.jpg", text12, layout="side", image_position="left")


    create_image_text_layout("attached_assets/generated_images/11banner.jpg", layout="full")
