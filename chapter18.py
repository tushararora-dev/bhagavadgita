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
    create_image_text_layout("attached_assets/generated_images/18main.jpg", layout="full")


    text0 = """
    <h2>Chapter 18: Moksha-Sannyasa Yoga (Yoga of Liberation and Renunciation)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <span style="color:#FF5733;">Shloka 18.1 to 18.5 : </span>
<span style="color:#77beda;">Arjuna</span> kehte hain:
“<span style="color:#77beda;">Krishna</span>! Aap kabhi kehte ho karm tyag do (<span style="color:#77beda;">Sannyas</span>),
Aur kabhi kehte ho karm karo (<span style="color:#77beda;">Yoga</span>)…
Toh in dono mein kaun sa behtar hai? Kripya mujhe spasht roop se batayein.” <span style="color:#77beda;">Krishna</span> kehte hain:
<span style="color:#77beda;">“Sannyas”</span> ka matlab hai – fal ki ichchhaon ka tyaag. <span style="color:#77beda;">“Tyaag”</span> ka matlab hai – asakti chhodkar karma karna. Lekin dono mein karma-yog (<span style="color:#77beda;">karma karte hue asakti ka tyaag</span>) shreshth hai. Kuch log kehte hain: “Sab karma tyag do, woh bandhan deta hai” Kuch log kehte hain: “Yagya, daan aur tapasya jaisa karma kabhi tyagne yogya nahi hota” <span style="color:#77beda;">Krishna</span> kehte hain:
“<span style="color:#77beda;">Arjuna</span>! Main tumhe tyag ke teen prakaar spasht roop se bataata hoon — <span style="color:#77beda;">Sattvik Tyag, Rajasik Tyag, Tamasik Tyag</span>” <span style="color:#77beda;">Krishna</span> kehte hain:
Yagya (<span style="color:#77beda;">Pooja</span>), Daan, aur Tapasya. Inhe kabhi tyagna nahi chahiye — Yeh jeevan ko shuddh aur sattvik banaate hain.
    """ 
    create_image_text_layout("attached_assets/generated_images/181.jpg", text1, layout="side", image_position="left")

    text2 = """
    <span style="color:#FF5733;">Shloka 18.6 to 18.10 : </span>
Chahe pooja ho, tapasya ho ya daan — Karo, par asakti aur fal ki chinta chhod kar. Yehi hai <span style="color:#77beda;">Sattvik Tyaag</span>. Jo vyakti kehta hai: “Main kaam nahi karunga, main sanyasi hoon” – par asal mein kartavya se bhaagta hai. Woh <span style="color:#77beda;">Tamasik Tyag</span> hai — agyaan se bhara. Jo vyakti kehta hai: “Yeh kaam toh muskil hai, dukh deta hai – chhodo isse”
Woh <span style="color:#77beda;">rajasik tyag</span> hai – usmein bhi fal ki chinta chhupi hoti hai. Jo kehta hai:
“Yeh mera kartavya hai – bas isse poora man se karna hai” Woh <span style="color:#77beda;">Sattvik Tyag</span> karta hai. Karm karta hai – par bandhan mein nahi aata. <span style="color:#77beda;">Sattvik Tyagi</span>: Na toh bure kaam se ghabraata hai, Na achhe kaam se chipakta hai. Woh har kaam karta hai sam-bhav aur sam-buddhi se
    """ 
    create_image_text_layout("attached_assets/generated_images/182.jpg", text2, layout="side", image_position="right")



    text3 = """
    <span style="color:#FF5733;">Shloka 18.11 to 18.15 : </span>
<span style="color:#77beda;">Krishna</span> kehte hain: Jab tak tumhara sharir hai, Tum karma se mukti nahi pa sakte. Par tum fal aur asakti ka tyaag kar sakte ho – yehi hai <span style="color:#77beda;">Sattvik Tyag</span>. Jo karm asakti se bhara hota hai. Uska fal hota hai:
Sukh (<span style="color:#77beda;">reward</span>), Dukh (<span style="color:#77beda;">loss</span>), Moha (<span style="color:#77beda;">attachment/confusion</span>). Par tyagi vyakti in teenon se pare rehta hai. Hey <span style="color:#77beda;">Arjuna</span>!
Samajh lo – har karma ke peeche 5 tattva hote hain:. Adhiṣṭhāna – Sharir (<span style="color:#77beda;">jisme karm ho raha hai</span>),
Kartā – Vyakti (<span style="color:#77beda;">jo karma karta hai</span>)
Karaṇam – Indriyaan, man aur buddhi (<span style="color:#77beda;">tools</span>)
Cheṣṭā – Vyakti ke prayatna aur movement
Daivam – Bhagya/Daiva – higher will, jo tumhara control nahi. 
Koi bhi karma in 5 ke bina nahi hota. Jo karm sharir, vani, ya man se hota hai – Woh tabhi hota hai jab ye 5 tattva milkar kaam karte hain
Par ahankaari vyakti ye sab nahi maanta. Woh kehta hai: "<span style="color:#77beda;">Sab kuch maine kiya!</span>"
    """
    create_image_text_layout("attached_assets/generated_images/183.jpg", text3, layout="side", image_position="left")

    text5 = """
    <span style="color:#FF5733;">Shloka 18.16 to 18.20 : </span> 
Jo vyakti kehta hai:
"<span style="color:#77beda;">Main hi karta hoon sab kuch</span>" Woh prakriti aur daiva ke gyaan se anjaan hai. Woh sach ko nahi samajhta
Uski buddhi durmati (bhramit) hai. Jo vyakti: Karma karte waqt ahankaar se mukt ho. Aur uski buddhi asang rahe. Woh karm karta hai, par paap mein bandhta nahi. Har karm ke peeche 3 cheezen hoti hain:
<span style="color:#77beda;">Gyaan</span> – Jo tum jaante ho
<span style="color:#77beda;">Gyaeya</span> – Jo jaanna chahte ho
<span style="color:#77beda;">Gyaata</span> – Jo jaanta hai (<span style="color:#77beda;">tum</span>)
Yehi 3 karma ki trigger hoti hain. Ab <span style="color:#77beda;">Krishna</span> kehte hain:
Tumhara: Gyaan, Karma, Aur Karta
Ye Sattvik, Rajasik ya Tamasik ho sakte hain. Sattvik Gyaan – Jo vyakti sabhi jeevon mein ek Atma (<span style="color:#77beda;">paramatma</span>) ko dekhta hai. Woh samajhta hai: “Sab alag sharir hain, par ek hi chetna (<span style="color:#77beda;">soul</span>) hai” Yehi Gyaan mukti deta hai.
    """
    create_image_text_layout("attached_assets/generated_images/154.jpg", text5, layout="side", image_position="right")


    text6 = """
    <span style="color:#FF5733;">Shloka 18.21 to 18.25 : </span> 
<span style="color:#77beda;">Rajasik Gyaan</span>: Jo har cheez mein bhed aur alagapan dekhta hai. “Yeh main hoon, yeh tu hai”, “Yeh Hindu, yeh Muslim, yeh ameer, yeh gareeb”. Aisi drishti bandhan ban jaati hai. <span style="color:#77beda;">Tamasik Gyaan</span>: Jo asatya ko satya samajhta hai, Bina soche-samjhe kisi ek baat ya aadmi se chipak jaata hai. Andhvishwas, fanaticism, ya extreme bias. Yeh gyaan nahi, gyaan ka bhram hai. <span style="color:#77beda;">Sattvik Karma</span>: Kartavya samajh ke kiya gaya kaam, Bina raag-dvesh, Bina kisi fal ki aasha. Karma ke madhyam se atmic vikas hota hai. <span style="color:#77beda;">Rajasik Karma</span>: Jo ichchha, ego aur naam ke liye kiya gaya ho. “Main kar raha hoon” aisi bhavna. Aisi karm-seva bandhan ban jaati hai. <span style="color:#77beda;">Tamasik Karma</span>: Jo agyaan se, bina soche samjhe hota hai. Jisme hinsa, vinash ya doosron ko dukh ho. Yeh karm paap ban jaata hai.
    """
    create_image_text_layout("attached_assets/generated_images/185.jpg", text6, layout="side", image_position="left")


    text7 = """
    <span style="color:#FF5733;">Shloka 18.26 to 18.30 : </span> 
<span style="color:#77beda;">Sattvik Karta</span> (<span style="color:#77beda;">doer</span>): Asakti se mukt, “Main karta hoon” ke ahankaar se mukt, Dhairyavaan, lagan se bhara. Aise log hi asli yogi hote hain. <span style="color:#77beda;">Rajasik Karta</span>: Jo sirf result chase karta hai. Jo gusse mein, ya swarth se kaam karta hai. Aisi karta-bhavna bandhan deti hai. <span style="color:#77beda;">Tamasik Karta</span>: Jisme samajh nahi, motivation nahi. Kaam mein moorkhta aur jhooth ho. Yeh karta na apne kaam ka hai, na samaj ke kaam ka. <span style="color:#77beda;">Krishna</span> kehte hain:
Tumhari buddhi (<span style="color:#77beda;">intellect</span>) aur dhriti (<span style="color:#77beda;">willpower</span>) bhi Sattvik, Rajasik ya Tamasik hoti hai. Ab main unka vibhajan batata hoon. <span style="color:#77beda;">Sattvik Buddhi</span>: Jo clearly jaanti hai: Kya karna hai (<span style="color:#77beda;">kartavya</span>), Kya nahi karna (<span style="color:#77beda;">tyagya</span>), Kya dharma hai, kya adharm, Yeh buddhi jeevan mein prakash deti hai
    """
    create_image_text_layout("attached_assets/generated_images/186.jpg", text7, layout="side", image_position="right")

    text8 = """
    <span style="color:#FF5733;">Shloka 18.31 to 18.35 : </span> 
<span style="color:#77beda;">Rajasik Buddhi</span>: Jo dharma ko adharm samjhe. Kartavya ko nakarne yogya samjhe. Uljhanon bhari soch, jo fal aur swarth mein atki hoti hai. <span style="color:#77beda;">Tamasik Buddhi</span>: Jo asaty ko satya samjhe, Jo apne kaam, vichar, aur faisle andhkaar mein leta hai. Agyani aur moorkh buddhi – jeevan ko vinash ki aur le jaati hai. <span style="color:#77beda;">Sattvik Dhriti</span> (<span style="color:#77beda;">Willpower</span>): Jo man, praan aur indriyon ko niyantrit rakhe, Jo sankalp aur sadhana mein sthir rahe. Yeh dhriti tumhe moksha aur shanti ki aur le jaati hai. <span style="color:#77beda;">Rajasik Dhriti</span>: Jo sirf safalta, paisa, ya kaamvasna ke liye dhairya banaye rakhta hai. Jo chinta, lalach, aur ego se paida hota hai. Yeh kabhi tumhe shuddh mukti nahi deta. <span style="color:#77beda;">Tamasik Dhriti</span>: Jo vyakti ka dhairya sirf bhay, gussa, alasya ya depression mein tikta hai. Na woh sudhar chahta hai, na badlav. Aisi dhriti tumhe dukh aur vinash ke raaste par le jaati hai.
    """
    create_image_text_layout("attached_assets/generated_images/187.jpg", text8, layout="side", image_position="left")


    text9 = """
    <span style="color:#FF5733;">Shloka 18.36 to 18.40 : </span> 
<span style="color:#77beda;">Krishna</span> kehte hain:
“<span style="color:#77beda;">Arjuna</span>! Jaise buddhi aur dhriti teen prakaar ke hote hain
Waise hi sukh bhi teen prakaar ka hota hai: Sattvik, Rajasik, Tamasik”. <span style="color:#77beda;">Sattvik Sukh</span>: Shuruaat mein ho sakta hai mushkil (<span style="color:#77beda;">mehnat, tyaag, self-control</span>). Par ant mein deta hai antah-shanti, gyaan aur amrit samaan anand. Jaise sadhana, satvik jeevan, dhyan. <span style="color:#77beda;">Rajasik Sukh</span>: Jo shuruaat mein sukhprad lage (<span style="color:#77beda;">indriya-sukh, vasna, bhog</span>). Par baad mein deta hai dukh, guilt aur rog. Jaise junk food, vasna, addiction. <span style="color:#77beda;">Tamasik Sukh</span>: Jo sukh deta hai par andhkaar, bhram aur alasya mein dubo deta hai. Jaise neend mein bhaagna, nasha, ya aparadh ka sukh. Aisa sukh atma-vinash ka raasta hai. <span style="color:#77beda;">Krishna</span> kehte hain: Sattva, Rajas aur Tamas – ye teen gun sab jagah hain. Prithvi pe, Devtaon mein, Har jeev mein/ Tumhara kartavya hai – Sattvik guno ko badhawa dena.
    """
    create_image_text_layout("attached_assets/generated_images/188.jpg", text9, layout="side", image_position="right")

    text10 = """
    <span style="color:#FF5733;">Shloka 18.41 to 18.45 : </span> 
<span style="color:#77beda;">Krishna</span> kehte hain: Brahmin, Kshatriya, Vaishya, aur Shudra —
Yeh sab janm se nahi, balki gun (<span style="color:#77beda;">qualities</span>) aur karma (<span style="color:#77beda;">actions</span>) se bante hain. <span style="color:#77beda;">Brahmin qualities</span>: Shant swabhav (<span style="color:#77beda;">śham</span>), Indriyon par niyantran, Tapasya, shuddhata, dharm mein nishtha, Kshama aur satya mein jeevan. Aisa vyakti adhyatmik marg ka adhar hota hai. <span style="color:#77beda;">Kshatriya qualities</span>: Bahaduri, utsah, dhairya, Neeti aur nyay mein nipunta, Apna kartavya pura karne mein nishtha Rashtra aur dharma ki raksha karta hai. <span style="color:#77beda;">Vaishya ka karma</span>: Krishi, gaay raksha, vyapar, dhan ka vikas
Shudra ka karma: Seva aur samarpan, Dono samajik chakra ke mool adhaar hain. Jo vyakti apne gun aur prakriti ke anusaar karm karta hai,
Usse hi jeevan mein safalta aur shuddhi milti hai
Yeh hi hai svadharma ka rahasya
    """
    create_image_text_layout("attached_assets/generated_images/189.jpg", text10, layout="side", image_position="left")

    text11 = """
    <span style="color:#FF5733;">Shloka 18.46 to 18.50 : </span> 
Jis Ishwar se sab kuch utpann hua hai, Agar tum apna karm usko arpan karo, Toh tum param siddhi – yani mukti – prapt kar sakte ho. Apna dharma, chahe perfect na ho, Par dusre ke dharma ko achhi tarah nibhaane se bhi behtar hai. Kyunki apne swabhav ke viruddh jeevan jeena = asantulan = dukh. <span style="color:#77beda;">Krishna</span> kehte hain: Har karm mein kuch na kuch asuddhi hoti hai. Lekin isliye karm chhodna uchit nahi. Tumhara kaam hai: karm karo, Ishwar ko arpan karke. Jo vyakti: Sab asaktiyon ko chhod chuka hai. Apne man ko jeet chuka hai. Wah sanyasi hokar bhi karm karta hai. Aur param shuddhi (<span style="color:#77beda;">moksha</span>) prapt karta hai. Hey <span style="color:#77beda;">Arjuna</span>! Ab suno – jo vyakti apna karm sahi dhang se karta hai, Wah kaise param Brahman (<span style="color:#77beda;">Ishwar ke saath ek-roopta</span>) ko prapt karta hai. Main tumhe yeh rahasya batane ja raha hoon…
    """
    create_image_text_layout("attached_assets/generated_images/1810.jpg", text11, layout="side", image_position="right")


    text12 = """
    <span style="color:#FF5733;">Shloka 18.51 to 18.55 : </span> 
Jisne Apni buddhi ko pavitra kiya. Indriyon, vasnaon, gusse aur bhay par vijay paayi. Wah Brahman mein sthit hota hai – jeevan-mukt yogi. Jo vyakti Brahma-bhoot ho jata hai (<span style="color:#77beda;">Ishwar mein sthit</span>): Na kisi ki chinta karta hai. Na kisi vasna mein jeeta hai. Sab jeevon mein ek Atma ko dekhta hai. Wahi Bhakti yog ka adhikari hota hai. Sirf Bhakti ke madhyam se hi
Tum mujhe vyaapak roop mein jaan sakte ho aur tabhi tum mujh mein poorn roop se ek-roop ho sakte ho.
    """
    create_image_text_layout("attached_assets/generated_images/1811.jpg", text12, layout="side", image_position="left")

    text12 = """
    <span style="color:#FF5733;">Shloka 18.56 to 18.60 : </span> 
Jo mujhe ashrit karke karm karta hai. ska har karm bandhan todta hai. Na ki bandhan banata hai. Ishwar mein samarppit karma hi karma yog hai. Apni buddhi, soch, aur karm sab mujhme samarpit karo. Tabhi tum nirbhay aur safal banoge. <span style="color:#77beda;">Krishna</span> ka yeh shuddh Bhakti Yoga ka rahasya hai. Agar tumhara man mujhme lagega toh tum sab sankaton ko paar kar loge. Main tumhara rakshak ban jaunga. Agar tum sochoge: <span style="color:#77beda;">“Main nahi karoonga”</span>. Toh prakriti tumse waise bhi apna kaam karwaegi. Tumhari ichchha se nahi, prakriti ke gunon se.
    """
    create_image_text_layout("attached_assets/generated_images/1812.jpg", text12, layout="side", image_position="right")


    text13 = """
    <span style="color:#FF5733;">Shloka 18.61 to 18.66 : </span> 
Ishwar har jeev ke hriday mein antaryami roop se virajmaan hai. Tumhara jeevan uski ichchha se ghoomta hai. Tum soch rahe ho – par asli karta toh Wah hai. <span style="color:#77beda;">Krishna</span> kehte hain: Tum sab kuch chhodkar meri sharan mein aao. Main tumhara bandh-bhool-bhram sab kaat dunga. <span style="color:#77beda;">Krishna</span> kehte hain: “Maine tumhe sabse gupt gyaan de diya hai”
Ab soch samajhkar faisla tumhara hai — kya tum meri sharan loge?. <span style="color:#77beda;">Krishna</span> kehte hain: Mujhme man lagao, Mera bhakt bano, Mujhe namaskar karo. Main tumse prem karunga aur tumhe apna bana lunga. “Tum sab dharmon (<span style="color:#77beda;">duties, doubts, fears</span>) ko tyag do”. Sirf meri sharan mein aao. Main tumhara har paap, har bandhan khud dhoyunga. “Mujh par poora vishwas rakho – aur mukti pao”
    """
    create_image_text_layout("attached_assets/generated_images/1813.jpg", text13, layout="side", image_position="left")


    create_image_text_layout("attached_assets/generated_images/18banner.jpg", layout="full")
