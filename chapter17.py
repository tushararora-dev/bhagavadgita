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
    create_image_text_layout("attached_assets/generated_images/17main.jpg", layout="full")


    text0 = """
    <h2>Chapter 17: Shraddha Traya Vibhag Yog (Yoga of the Threefold Division of Faith)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <span style="color:#FF5733;">Shloka 17.1 to 17.5 : </span>
<span style="color:#77beda;">Arjuna</span> poochhte hain:
“Hey <span style="color:#77beda;">Krishna</span>!
Jo log Shastra ke niyam nahi jaante, par shraddha se bhakti karte hain,
Unki shraddha kis prakriti mein hoti hai – <span style="color:#77beda;">Sattvik, Rajasik, ya Tamasik?</span>”. Har vyakti ki shraddha uske svabhav ke gunon se banti hai:
<span style="color:#77beda;">Sattvik Shraddha</span> – shuddh, gyaanmayi
<span style="color:#77beda;">Rajasik Shraddha</span> – icchha, phal aur ahankaar se bhari
<span style="color:#77beda;">Tamasik Shraddha</span> – andhvishwas, andhkar aur moorkhta se bhari Vyakti ki soch aur jeevan uski shraddha ke anusaar hota hai. Jo jaisi shraddha rakhta hai, wahi ban jaata hai.
“You become what you believe.” <span style="color:#77beda;">Sattvik log</span> – Devtaon ko poojte hain
<span style="color:#77beda;">Rajasik log</span> – Yaksh aur rakshas (material power) ko
<span style="color:#77beda;">Tamasik log</span> – Bhoot, pret, aur asur ko poojte hain
Shraddha ka gun batata hai ki vyakti kin urjaon se judta hai. Jo log: Shastra ke viruddh, Shareer ko peeda dekar tapasya karte hain, Dikhawa, ahankaar ya siddhi ke liye, Woh asuri svabhav ke hain. Woh na Ishwar ko bhajte hain, na apne aatma ka kalyan karte hain.
    """ 
    create_image_text_layout("attached_assets/generated_images/171.jpg", text1, layout="side", image_position="left")

    text2 = """
    <span style="color:#FF5733;">Shloka 17.6 to 17.10 : </span>
Jaisa vyakti ka gun (<span style="color:#77beda;">sattva, rajas, tamas</span>), Waisa hi uska bhojan bhi hota hai:
<span style="color:#77beda;">Sattvik log</span> – shuddh aur hitkari bhojan
<span style="color:#77beda;">Rajasik log</span> – teekha, oily, spicy, taja urja dene wala
<span style="color:#77beda;">Tamasik log</span> – basi, aswachh, aur paap-prabhavit bhojan. <span style="color:#77beda;">Sattvik bhojan hota hai</span>:
Jise kha kar jeevan, bal, swasthya aur anand badhe. Jaisa ki: rasbhara, ghee-dar, thanda, nirmal aur sukhdayak bhojan. Yeh sattvik logon ko pasand aata hai. <span style="color:#77beda;">Rajasik bhojan hota hai</span>: Zyada teekha, garam, chatpata, tel-masale wala. Jo kuch der to urja deta hai. Par baad mein dukha, rog aur chinta deta hai. <span style="color:#77beda;">Tamasik bhojan hota hai</span>: Basi, gandha wala, be-rasa, Ashuddh ya jhootha khana. Jo moorkhta, alasya, aur andhkaar badhata hai. Tamasik log isse pasand karte hain.
    """ 
    create_image_text_layout("attached_assets/generated_images/172.jpg", text2, layout="side", image_position="right")



    text3 = """
    <span style="color:#FF5733;">Shloka 17.11 to 17.15 : </span>
<span style="color:#77beda;">Sattvik Yagya woh hai</span>: Jo niyam se, bina fal ki ichchha ke kiya jaaye. Jo sirf kartavya samajh ke kiya jaaye. Yeh antar-shuddhi aur bhakti se bhara hota hai. <span style="color:#77beda;">Rajasik Yagya woh hai</span>: Jo fal aur dikhawa ke liye kiya jaata hai. “Logo ko dikhana hai ki main bhakt hoon”. Par bhakti ki gaharai nahi hoti. <span style="color:#77beda;">Tamasik Yagya woh hai jo</span>: Bina mantra, shraddha, niyam ya daan ke kiya gaya ho. Yeh andar se khaali hota hai. Sirf andar ka ego ya confusion hota hai, Ishwar nahi. <span style="color:#77beda;">Sharirik Tapasya mein hota hai</span>: Guru, devtaon, aur gyaani ka samman, Sharir aur man ki shuddhi, Ahimsa, brahmacharya, aur honesty, Yehi hota hai Sattvik Sharirik Tap. <span style="color:#77beda;">Tapasya vani se bhi hoti hai</span>: Satya bolna, Madhur aur upyogi baat kehna, Swadhyaya (<span style="color:#77beda;">shastra paath</span>) bhi vani ka Tap hai. Aisi vani man ko uthati hai, giraati nahi
    """
    create_image_text_layout("attached_assets/generated_images/173.jpg", text3, layout="side", image_position="left")

    text5 = """
    <span style="color:#FF5733;">Shloka 17.16 to 17.20 : </span> 
<span style="color:#77beda;">Manasik Tapasya mein hota hai</span>: Mann ki shanti, Maun aur vinamrata, Apne upar control, Man ki shuddhi hi asli Tapasya hai. Jo Tapasya: Shraddha se, Bina kisi fal ki ichchha ke, Niyamit roop se ki jaaye. Woh <span style="color:#77beda;">Sattvik Tapasya hoti hai</span>. Jo Tap: Naam, izzat, aur fame ke liye kiya jaata hai. “Log mujhe bada sadhak samjhein” <span style="color:#77beda;">Aisi Tapasya Rajasik hai.</span> Woh <span style="color:#77beda;">asthir</span> hoti hai. Jo Tap: Mann ke dvesh, ya shareer ko unnecessary peeda dekar kiya jaaye. <span style="color:#77beda;">Woh Tamasik Tapasya kehlata hai</span>. Na usme buddhi hoti hai, na bhakti. <span style="color:#77beda;">Sattvik Daan</span>: Jo sahi samay, sahi jagah, aur bina kisi badle ki ummeed se diya jaaye. Jo kartavya samajh ke diya gaya ho. Woh <span style="color:#77beda;">Sattvik Daan</span> kehlata hai
    """
    create_image_text_layout("attached_assets/generated_images/174.jpg", text5, layout="side", image_position="right")


    text6 = """
    <span style="color:#FF5733;">Shloka 17.21 to 17.25 : </span> 
Jo daan: Badle mein kuch paane ke liye diya jaaye. Ya daan dekar kisi se izzat, status, ya return ki aasha ho. Woh <span style="color:#77beda;">Rajasik Daan</span> kehlata hai. Jo daan: Galat samay, Galat vyakti, Ya apmaan aur bina shraddha ke diya jaaye. Woh <span style="color:#77beda;">Tamasik Daan</span> hota hai. <span style="color:#77beda;">Krishna</span> kehte hain:
<span style="color:#77beda;">“OM, TAT, aur SAT”</span> – ye Brahman (<span style="color:#77beda;">supreme reality</span>) ke teen naam hain.
Inka uchcharan kiya jaata hai vedon, yagya, daan aur tapasya ke praarambh mein. Jab bhi tum yagya, daan ya tapasya karo, Uska praarambh karo “OM” ke ucharan se – Jo tumhe yaad dilata hai ki tum Ishwar ke liye kar rahe ho, na ki apne liye. “TAT” ka arth hai: “Yeh sab uske liye (<span style="color:#77beda;">Ishwar ke liye</span>)”
Jab tum daan ya tapasya karo bina fal ki ichchha ke,
Aur keval Ishwar arpan ke bhaav se – toh usmein pavitrata hoti hai.
    """
    create_image_text_layout("attached_assets/generated_images/175.jpg", text6, layout="side", image_position="left")


    text7 = """
    <span style="color:#FF5733;">Shloka 17.26 to 17.28 : </span> 
<span style="color:#77beda;">“SAT”</span> ka arth hai: Satya, punyata, aur sadbhav. Jo bhi karm satyata aur bhakti bhav se kiya gaya ho,
Wahi sattvik aur sthayi hota hai. Jab tum yagya, tapasya aur daan mein Shraddha aur nishchay se tike rehte ho,
Toh us sthiti ko bhi <span style="color:#77beda;">“SAT”</span> kaha jaata hai – Yaani tumhara sthir aur pavitra karm. Agar tum yagya, daan, ya tapasya Bina shraddha ke karte ho,
Toh woh: Na toh safal hota hai. Na pavitra. Woh sab <span style="color:#77beda;">‘ASAT’</span> hai – yaani vyarth aur dukh-prad
    """
    create_image_text_layout("attached_assets/generated_images/176.jpg", text7, layout="side", image_position="right")


    create_image_text_layout("attached_assets/generated_images/17banner.jpg", layout="full")
