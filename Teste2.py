
import streamlit as st

st.title("Dedicado à Gabriella Mussi Massoni:")

st.markdown(
    """
    <style>
    /* Fundo com corações */
    body {
        background-color: #ffdde1;
        background-image: url('https://www.transparenttextures.com/patterns/hearts.png');
        background-size: cover;
    }

    /* Fonte romântica */
    h1, h2, h3 {
        font-family: 'Cursive', sans-serif;
        color: #d63384;
        text-align: center;
    }

    /* Botões estilizados */
    div.stButton > button {
        background-color: #ff69b4;
        color: white;
        font-size: 20px;
        padding: 12px 24px;
        border-radius: 30px;
        border: none;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #ff1493;
        transform: scale(1.1);
    }

    /* Animação de corações flutuando */
    @keyframes floating {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }

    .hearts {
        font-size: 50px;
        display: block;
        text-align: center;
        animation: floating 2s ease-in-out infinite;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <iframe width="400" height="200" 
    src="https://www.youtube.com/embed/nUSh1KuKU7c" 
    frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """ 
    <p style="font-size:24px;">
    Reparei esses dias que nunca te fiz algo romântico, por mais que você mereça demais!
    </p>
    
    <p style="font-size:20px;"><b>Esse site ta em fase de teste, peço perdão por qualquer coisa programada errada...
    além de que, cartinhas físicas estão fora de moda.</b></p>

    <p style="font-size:24px;">
    A ideia do nome "Gabriella" vem do hebraico Gavri'el.  
    No âmbito romântico, seria algo como "aquela que traz mensagens de amor".
    </p>

    <p style="font-size:24px;">
    Te olhar é sempre assim.
    </p>
    
    <p style="font-size:20px;"><b>Nem todas as músicas são capazes de expressar o que eu quero dizer...</b></p>
    
      <style>
    div.stButton > button {
        font-size: 24px !important;
        padding: 15px 30px;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)  # Criando duas colunas para os botões

with col1:
    if st.button("Me mostre mais"):
        st.page_link("https://open.spotify.com/playlist/37i9dQZF1EJEm2SFxSxvQ3?si=f63051c6bdbe4194", label="Link para a nossa playlist no Spotify.") 
        st.success("Tem tudo o que você precisa saber")
        
with col2:
    if st.button("Não quero saber, seu otário!"):
        st.error("Poxa, que pena!")
        st.snow()  # Efeito de neve para variar um pouco
        st.image("https://pbs.twimg.com/media/FMFEuJVWYAYtq9E.jpg", width=800)  

st.markdown(
    """ 
    <p style="font-size:19px;">
    E talvez nem todos os buquês do mundo sejam o suficiente.
    Mas sou feliz em como a gente se entende.
    </p>""",    
unsafe_allow_html=True
)
st.image ("https://images.pexels.com/photos/250716/pexels-photo-250716.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", width=900)
