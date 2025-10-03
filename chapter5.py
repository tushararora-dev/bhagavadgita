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
    create_image_text_layout("attached_assets/generated_images/5.jpg", layout="full")


    text0 = """
    <h2>Chapter 5: Karma sanyasa Yoga (Yoga of Renunciation of Action)</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <span style="color:#FF5733;">Shloka 5.1 to 5.5 : </span>
Hey <span style="color:#77beda;">Arjuna</span>! Sannyas (<span style="color:#77beda;">tyag</span>) aur Karma Yog – dono mukti ke path hain.
Lekin in dono mein, Karma Yog sannyas se bhi uttam hai. Jo na kisi se dvesh karta hai, na hi kisi chiz ki ichchha karta hai –
Wahi nitya sanyasi hai. Jo har duality se pare hai, wahi bandhan se mukta hota hai. Jo dvesh aur ichchha se mukt hai – wahi yogi bhi hai aur sanyasi bhi.
Sirf kriya na karna, ya agni na jalana (<span style="color:#77beda;">sacrifice na karna</span>) sanyas nahi hai. Jo log kehte hain ki karma yog aur sannyas alag hain – wo bachche hain.
Gyani log jaante hain ki dono ka phal ek hi hai – jo kisi ek ko bhi sahi se pakadta hai, usse mukti milti hai. Jo sthiti Sankhya (<span style="color:#77beda;">gyaan yog</span>) se milti hai, wohi Karma Yog se bhi milti hai.
Jo dono mein ekta dekhta hai – wahi sach mein dekh raha hai.
    """ 
    create_image_text_layout("attached_assets/generated_images/51.jpg", text1, layout="side", image_position="left")


    text2 = """
    <span style="color:#FF5733;">Shloka 5.6 to 5.10 : </span>
Hey <span style="color:#77beda;">Arjuna</span>! Bina yog ke sirf sannyas lene se dukh hi milta hai.
Lekin yog se yukta muni jaldi hi <span style="color:#77beda;">Brahma</span> ko prapt karta hai. Jo yog mein sthir hai, jiska mann shuddh hai, jiska jeevan niyantrit hai –
Aur jo sab mein apne aap ko dekhta hai –
Woh karm karte hue bhi karm se lipta nahi. Yogi sochta hai: “<span style="color:#77beda;">Main kuch bhi nahi karta.</span>”
Chahe dekhna ho, sunna, chhuna, khaana, chalna, sona ya saans lena –
Sab usse hota hai, main karta nahi hoon. Chahe bolna ho, dena ho, lena ho, aankhon ka khulna-band hona ho –
Yogi jaanta hai ki sab indriya apne viṣayon mein vyast hain.
Main inka karta nahi hoon. Jo vyakti karm ko <span style="color:#77beda;">Brahman</span> ko arpan karta hai, aur asakti tyag kar ke karta hai –
Uska karm paap se kabhi chipakta nahi, jaise kamal ka patta paani se alag rehta hai.
    """ 
    create_image_text_layout("attached_assets/generated_images/52.jpg", text2, layout="side", image_position="right")



    text3 = """
    <span style="color:#FF5733;">Shloka 5.11 to 5.15 : </span>
Yogi apne sharir, mann, buddhi, aur indriyon se karm karta hai —
Lekin asakti tyag kar deta hai, aur sab kuch Bhagwan ke liye karta hai —
Is prakriya se uska mann shuddh ho jaata hai. Jo yog mein sthit hai, wo phal ki chinta chhod kar shaanti paata hai.
Jo yog mein sthit nahi hai, wo phal ke liye kaam karta hai – aur bandhan mein pad jaata hai. Jo yogi sab karm ko mann se tyag deta hai,
Woh apne “<span style="color:#77beda;">nau dwaar wale shareer</span>” mein rahta hua – kuch karta bhi nahi, karwata bhi nahi. Bhagwan kisi ko karm karne ya karane wala nahi banata –
Yeh sab vyakti ke svabhav (<span style="color:#77beda;">vasana</span>) se hota hai. Bhagwan kisi ka paap ya punya apne upar nahi leta.
Log ajnaani hone ke kaaran moh mein pad jaate hain.
(<span style="color:#77beda;">na ego karta hai, na doosron ko blame</span>)
    """
    create_image_text_layout("attached_assets/generated_images/53.jpg", text3, layout="side", image_position="left")

    text5 = """
    <span style="color:#FF5733;">Shloka 5.16 to 5.20 : </span> 
Jinka agyaan gyaan se nashth ho gaya hai,
Unka mann gyaan ke surya jaise prakash se chamak uthta hai. Jinki buddhi, jeev, shraddha, aur nishtha sab Bhagwan mein sthit hai –
Woh gyaan se paap mukt ho jaate hain aur punar janm se chhut jaate hain. Jo gyani hota hai, wo brahman, gau, haathi, kutta, ya chandala sab mein ek hi Atma ko dekhta hai. Jinka mann sama bhaav mein sthit hai –
Woh jeevan mein hi srishti chakra se mukt ho jaate hain.
Kyuki <span style="color:#77beda;">Brahma</span> sama hai – aur wahi Brahma mein sthit hote hain. Gyani na to priya vastu milne par prasannta se jhoomta hai,
na apriya milne par dukhi hota hai.
Woh sthir buddhi wala, moha se mukt <span style="color:#77beda;">Brahma</span> mein sthit hota hai.
    """
    create_image_text_layout("attached_assets/generated_images/54.jpg", text5, layout="side", image_position="right")



    text6 = """
    <span style="color:#FF5733;">Shloka 5.21 to 5.25 : </span> 
Jo yogi bahari vishayon mein asakt nahi hai,
Aur jo apne aap mein sukh paata hai –
Woh akshaya (<span style="color:#77beda;">nash na hone wale</span>) sukh ko prapt karta hai. Jo sukh indriyon ke sparsh se milta hai – woh dikhne mein madhur,
lekin asli mein dukh ka beej hota hai, aur ant mein khatam ho jaata hai.
Gyani vyakti unmein ruchi nahi leta. Jo vyakti marne se pehle – kaam aur krodh ke vega ko rok leta hai,
Wahi yog mein yukta aur sukhmay jeevan jeene wala hota hai. Jo vyakti andar se hi sukhit hai, andar se hi ramta hai,
aur jiska prakash bhi andar se hi hai –
Wahi yogi Brahman mein vilin hota hai. Jo paap se shuddh ho gaye hain, jo samta mein sthit hain,
aur jo sabhi praniyon ke kalyan mein lage hain –
Wahi <span style="color:#77beda;">Brahma</span> Nirvana prapt karte hain.
    """
    create_image_text_layout("attached_assets/generated_images/55.jpg", text6, layout="side", image_position="left")



    text7 = """
    <span style="color:#FF5733;">Shloka 5.26 to 4.29 : </span>
Jo yogi kaam-krodh se mukt hai, jiska mann niyantrit hai,
aur jinhone apne aap ko jaan liya hai –
Unke liye Brahman ka sukh har taraf hai. Jo yogi bahari vishayon se mukh mod leta hai,
apni drishti ko bhrukuti ke beech lagata hai,
aur apni saans ke aav-gaman ko niyantrit karta hai –
Wahi dhyaan mein sthir hota hai. Jiska mann, buddhi aur indriyaan niyantrit hain,
jo ichchha, bhay aur krodh se mukt hai –
Wahi sadev mukt hota hai. Jo mujhe (<span style="color:#77beda;">Krishna</span>) – sabhi yagya-tapasya ka bhokta,
poore sansaar ka swami, aur sab praniyon ka suhrid (<span style="color:#77beda;">mitra</span>) maan leta hai –
Wahi param shanti prapt karta hai.
    """
    create_image_text_layout("attached_assets/generated_images/56.jpg", text7, layout="side", image_position="right")





    create_image_text_layout("attached_assets/generated_images/5banner.jpg", layout="full")
