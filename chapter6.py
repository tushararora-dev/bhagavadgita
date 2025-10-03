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
    create_image_text_layout("attached_assets/generated_images/6.jpg", layout="full")


    text0 = """
    <h2>Chapter 6: Dhyāna Yoga (The Yoga of Meditation)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <span style="color:#FF5733;">Shloka 6.1 to 6.5 : </span>
Jo vyakti karm ke phal par asakti na rakhte hue apna kartavya karm karta hai –
Wahi sacha sanyasi aur yogi hai.
Jo sirf kriya tyag de (<span style="color:#77beda;">agni na jalaaye</span>) – woh sannyasi nahi. Hey <span style="color:#77beda;">Arjuna</span>! Jo log sanyas kehte hain – wohi asli mein yog hai.
Jo vyakti abhi bhi ichchhaon aur sankalp se juda hai – woh yogi nahi ho sakta. Jo vyakti yog ke liye abhi-abhi prarambh kar raha hai,
Uske liye karm jaruri hai.
Lekin jo siddh yogi hai – uske liye shama (<span style="color:#77beda;">maan ki shanti</span>) jaruri hai. Jab vyakti indriyaon ke vishayon aur karmo se asakti tyag deta hai,
Aur har sankalp (<span style="color:#77beda;">ichchha</span>) chhod deta hai –
Tabhi usse yog mein sthit maana jaata hai. Apne aap ko upar uthao, neeche mat girao –
Kyunki tumhara sabse bada dost bhi tum ho, aur dushman bhi tum khud.
    """ 
    create_image_text_layout("attached_assets/generated_images/61.jpg", text1, layout="side", image_position="left")


    text2 = """
    <span style="color:#FF5733;">Shloka 6.6 to 6.10 : </span>
Jisne apne mann ko jeet liya – uske liye mann mitra ban jaata hai.
Par jiska mann vash mein nahi – uske liye wahi mann dushman ban jaata hai. Jis yogi ka mann jeeta gaya hai,
Aur jo <span style="color:#77beda;">antaratma</span> mein sthit hai –
Uske liye sardi-garmi, sukh-dukha, maan-apmaan sab ek samaan hai. Jiska mann gyaan aur anubhav se tript hai,
Jisne apni indriyon par vijay paayi hai –
Woh yogi mitti, pathar aur sone ko ek saman dekhta hai. Jo apne mitra, dushman, madhyastha, paapi ya sadhu – sab par ek saman drishti rakhta hai –
Wahi sabse uttam yogi maana jaata hai. Yogi hamesha ekant mein rehkar dhyaan mein sthit rehta hai –
Akela, vashibhut mann aur ashaheen, bina sangrah ke.
    """ 
    create_image_text_layout("attached_assets/generated_images/62.jpg", text2, layout="side", image_position="right")



    text3 = """
    <span style="color:#FF5733;">Shloka 6.11 to 6.15 : </span>
Yogi ek pavitra jagah par, ek sthir aasan par baithe —
Na zyada ooncha ho, na zyada neecha.
Aasan pe pehla layer ho kusha-grass (<span style="color:#77beda;">durva</span>), fir mriga-charm (<span style="color:#77beda;">blanket</span>), fir kapda. Us sthir aasan par baith kar,
Yogi apne mann, indriyon aur kriyaon ko niyantrit karta hai,
Aur dhyaan karta hai — mann ki shuddhi ke liye. Yogi apne sharir, gardan aur sir ko ek rekha mein sthir rakhta hai,
Aur naak ke aage ki disha mein dekhta hai — idhar-udhar nahi dekhta. Yogi apne mann ko shaant rakhta hai, bhay se mukt hota hai,
brahmacharya mein sthit rehta hai,
Aur apne chitt ko mere (<span style="color:#77beda;">Krishna</span>) mein lagaata hai. Is prakaar jo yogi apne mann ko niyantrit karke dhyaan karta hai,
Woh mere (<span style="color:#77beda;">Krishna</span>) mein sthit hokar —
Param shaanti aur nirvana prapt karta hai.
    """
    create_image_text_layout("attached_assets/generated_images/64.jpg", text3, layout="side", image_position="left")

    text5 = """
    <span style="color:#FF5733;">Shloka 6.16 to 6.20 : </span> 
Na to bahut adhik khane wale, aur na bilkul upvaas karne wale ke liye yog sambhav hai.
Na hi jo hamesha sota hai ya hamesha jaagta hai – uske liye yog sambhav hai. Jiska aahaar (<span style="color:#77beda;">diet</span>), vihaar (<span style="color:#77beda;">lifestyle</span>), karm (kaam), sone-jaagne ka samay – sab mein santulan hai –
Wahi yogi dukhon se mukta hota hai. Jab vyakti ka chitt (mann) poori tarah niyantrit hokar keval Atma mein sthir ho jaata hai,
Aur sab ichchhao se mukta ho jaata hai —
Tab use sacha yogi maana jaata hai. Jese ek deepak hawa na hone par hilta nahi –
Waisa hi yogi ka mann hota hai jab woh apne aap mein yog lagaata hai. Jab yogi ka chitta yog ke dwara poori tarah niyantrit ho jaata hai,
Aur us chitt mein yogi apne aap mein Atma ka anubhav karta hai –
Tab woh tript ho jaata hai.
    """
    create_image_text_layout("attached_assets/generated_images/65.jpg", text5, layout="side", image_position="right")



    text6 = """
    <span style="color:#FF5733;">Shloka 6.21 to 6.25 : </span> 
Jo sukh buddhi se anubhav hota hai, indriyon se nahi –
Woh sukh atyantik hai (<span style="color:#77beda;">param sukh hai</span>).
Jab yogi usmein sthir ho jaata hai, to kabhi chanchal nahi hota. Jab ek yogi is sukh ko paata hai –
To use kisi aur vastu ka lobh nahi rehta.
Aur tab uska mann kisi bhi bade dukh se bhi hila nahi sakta. Jo yogi dukhon ke yog se mukti ko paata hai –
Usi ko <span style="color:#77beda;">‘yog’</span> kehte hain.
Yeh yog dridh sankalp aur ashraddha-mukt mann se hi prapt hota hai. Yogi har sankalp se utpann ichchhaon ko poori tarah tyag de,
Indriyon ko mann ke dwara vash mein kare –
Tab yog ka aarambh hota hai. Thoda-thoda kar ke, <span style="color:#77beda;">dhairy aur buddhi</span> se yogi apne mann ko Atma mein sthir karta hai.
Phir kisi aur vastu ke baare mein chintan nahi karta.
    """
    create_image_text_layout("attached_assets/generated_images/66.jpg", text6, layout="side", image_position="left")



    text7 = """
    <span style="color:#FF5733;">Shloka 6.26 to 6.30 : </span>
Jab-jab mann bhatak jaaye,
Tab-tab use wapas kheenchkar Atma mein sthir karo. Jiska mann shaant ho gaya hai,
Jo yogi rajogun se mukt aur paap se nirmal ho gaya hai —
Woh  <span style="color:#77beda;">param sukh aur Brahman</span> mein sthiti ko prapt karta hai. Jo yogi sadaiv yog mein laga rehta hai,
Woh sab paapon se mukt ho jaata hai,
Aur <span style="color:#77beda;">Brahman</span> ke sparsh se atyantik sukh paata hai. Yogi sabhi jeevon mein apne aap ko dekhta hai,
Aur apne aap mein sabhi jeevon ko dekhta hai —
Wahi sacha yogi hai jiska drishtikon samaan hai. Jo mujhe ( <span style="color:#77beda;">Krishna</span>) sab jagah dekhta hai,
Aur sab kuch mujhme dekhta hai —
Main kabhi uske liye chhup nahi hota, aur wo bhi mere liye nahi chhupta.
    """
    create_image_text_layout("attached_assets/generated_images/67.jpg", text7, layout="side", image_position="right")


    text9 = """
    <span style="color:#FF5733;">Shloka 6.31 to 6.35 : </span>
Jo yogi sab praniyon mein mujhe dekhta hai, aur ekta mein sthit ho kar mujhe bhajta hai –
Woh chahe jaise bhi jeevan jeeye, hamesha mujhmein hi rehta hai. Jo vyakti har jeev ko apne saman dekhta hai,
Unke sukh aur dukh ko apne sukh-dukha jaisa maante hai –
Wahi sabse uttam yogi hai. <span style="color:#77beda;">Arjuna</span> kehta hai: Hey <span style="color:#77beda;">Krishna</span>! Aapne jo yog kaha –
Woh mujhe kathin lagta hai, kyunki mera mann chanchal hai. <span style="color:#77beda;">Arjuna</span> kehta hai: Mann chanchal hai, balwaan hai, ziddi hai –
Main ise niyantrit karna hawa ko pakadne jaisa mushkil maanta hoon. Hey <span style="color:#77beda;">Arjuna</span>! Nissandeh mann chanchal aur kathin hai –
Lekin abhyas aur vairagya se ise vash mein kiya ja sakta hai.
    """
    create_image_text_layout("attached_assets/generated_images/68.jpg", text9, layout="side", image_position="left")


    text10 = """
    <span style="color:#FF5733;">Shloka 6.36 to 6.40 : </span>
Jiska mann niyantrit nahi hai, uske liye yog kathin hai.
Lekin jo purusharthi hai aur mann ko vash mein rakhta hai –
Woh yog ko zarur prapt karta hai. <span style="color:#77beda;">Arjuna</span> poochta hai: Jo yogi shraddha to rakhta hai,
Par mann bhatak jaata hai, aur safalta ke pehle sharir chhod deta hai –
Uska kya hota hai? <span style="color:#77beda;">Arjuna</span> kehta hai: Kya aisa yogi bhog bhi nahi le pata aur yog bhi nahi prapt karta –
Jaise baadal ka tukda toot kar kahin ka nahi rehta? <span style="color:#77beda;">Arjuna</span> kehta hai: Hey <span style="color:#77beda;">Krishna</span>! Aap hi mera yeh sandeh door kar sakte ho –
Is prashna ka uttar aapke bina aur koi nahi de sakta. Hey <span style="color:#77beda;">Arjuna</span>! Jo kalyan ka karm karta hai,
Uska na is janm mein na agle mein nash hota hai.
Woh kabhi durgati ko prapt nahi karta.
    """
    create_image_text_layout("attached_assets/generated_images/69.jpg", text10, layout="side", image_position="right")

    text11 = """
    <span style="color:#FF5733;">Shloka 6.41 to 6.47 : </span>
Jo yog mein asafal rahe, unhe punya logon ke lok milte hain –
Aur fir unka janm ek shuddh, dharmik aur samruddh ghar mein hota hai. Kabhi-kabhi aise yogi ka janm unke hi jaise gyani yogi parivaar mein hota hai –
Jo bahut hi <span style="color:#77beda;">durlabh</span> hota hai. Woh yogi apne purv janm ke gyaan ko paakar –
Is janm mein wapas yog ki sadhana mein lag jaata hai. Apne purv abhyas ke bal par, chahe mann bhatka ho –
Woh yogi wapas kheech liya jaata hai, aur shabdon ke gyaan ko paar kar jaata hai. Jo yogi <span style="color:#77beda;">lagataar prayatna</span> karta hai,
Woh paap se shuddh hokar, kai janmon ke baad – moksha prapt karta hai. Hey <span style="color:#77beda;">Arjuna</span>! Yogi tapasviyon, gyaniyon aur karmiyon se bhi shresth hai.
Isliye tum yogi bano! Sabhi yogiyon mein bhi,
Jo mujhe bhakti bhav se smaran karta hai, aur mujhme antar-aatma se sthit hai –
Woh sabse uttam yogi hai.
    """
    create_image_text_layout("attached_assets/generated_images/610.jpg", text11, layout="side", image_position="left")

    create_image_text_layout("attached_assets/generated_images/6banner.jpg", layout="full")
