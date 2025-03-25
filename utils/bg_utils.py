import streamlit as st
import numpy as np

def choose_image():
    """
    Randomly selects the image links from the given set of links
    """
    bg_images = [
        'https://avatars.mds.yandex.net/i?id=63047fda2ad15dec8a1825160ac9b74c_l-4298597-images-thumbs&ref=rim&n=13&w=3000&h=1875',
        'https://external-preview.redd.it/_lbeK9GtCRA7wRPO0j7jKHhLXah5f_xAd6rL0F0vK80.jpg?s=804d2a124b2ff40514e98627726566aec7db0d15',
        'https://i.pinimg.com/originals/ec/c0/75/ecc075e833edb16994ce4eff576adb16.jpg',
        'https://a-static.besthdwallpaper.com/starry-sky-stars-scenery-wallpaper-2736x1824-99589_41.jpg',
        'https://www.sunhome.ru/i/wallpapers/228/asteroid.orig.jpg',
        'https://www.webtekno.com/images/editor/default/0002/45/495ae3918231e25bddfa4fb86789a65023e922c5.jpeg',
        'https://i.playground.ru/i/pix/714949/image.jpg',
        'https://cdn.mos.cms.futurecdn.net/C3HEg797tNRGFWcWxkHXmn-1920-80.jpg',
        'https://live.staticflickr.com/454/20226599891_e2cf9861ff_h.jpg',
        'https://i.pinimg.com/originals/f1/6c/f0/f16cf008a9e70b94e78e6c0661169407.jpg',
        'https://www.cloudynights.com/uploads/monthly_01_2018/post-221543-0-46663500-1515622552.jpg',
        'https://altinoz.com.tr/wp-content/uploads/2020/10/dunya-disi-yasam.jpg',
        'https://images.astronet.ru/pubd/2016/05/10/0001362367/OphiuchusPlanets_Fairbairn_1824.jpg',
        'https://s0.rbk.ru/v6_top_pics/media/img/3/21/756709979126213.jpg',
        'https://news-img.gismeteo.st/ru/2020/09/119665493_3360028984055402_4192909183204559668_n.jpg',
        'https://static.mk.ru/upload/entities/2019/07/01/15/articles/facebookPicture/ad/98/44/c5/fd6640e35163f93a2fccbfbfc9e043af.jpg'
    ]
    return np.random.choice(bg_images)

def set_background(image_url):
    """
    Sets a background image for the Streamlit app.
    """
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url({image_url}) no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )