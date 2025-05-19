import streamlit as st
import pandas as pd
from pyairtable import Api # https://pyairtable.readthedocs.io/en/stable/getting-started.html
from datetime import datetime

from myFunc.reactSimpleChatBot import render_chat_bot

st.set_page_config(
    page_title="Love Golf - Shop",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargamos fecha actual
today = datetime.today().strftime("%Y")

# https://materializecss.com/
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">', unsafe_allow_html=True)
# https://materializecss.com/icons.html
st.markdown('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">', unsafe_allow_html=True)
# https://fontawesome.com/start
st.markdown('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" rel="stylesheet">', unsafe_allow_html=True)

# Audit personalization style
customStyle ="""
            <style type="text/css">
            /*Aumenta el tamaño de las cards*/
            .card.large{
                height:550px!important;
            }
            /*Aumenta el contenido disponible*/
            .card.large .card-content{
                max-height:fit-content!important;
            }
            /* Aumenta la fuente de los tabs de Streamlit*/
            button[data-baseweb="tab"] p{
                font-size:20px!important;
            }
            /* Remueve el espacio en el encabezado por defecto de las apps de Streamlit */
            div[data-testid="stAppViewBlockContainer"]{
                padding-top:0px;
            }
            </style>
            """
st.html(customStyle)

brandHTML=f"""
<div class="row">
<h1>Love Golf <span class="blue-text text-darken-3">đưa tin</span> </h1>
</div>
"""
# html generate
st.html(brandHTML)

# Get Airtable key and base id
AIRTABLE_API_KEY = st.secrets.AIRTABLE_API_KEY
AIRTABLE_BASE_ID=st.secrets.AIRTABLE_BASE_ID

# Get AT data
api = Api(AIRTABLE_API_KEY)
# Cargamos las tablas
tblnews = api.table(AIRTABLE_BASE_ID, 'News')
tblprofile = api.table(AIRTABLE_BASE_ID, 'Profile')

news=""
    # Hacemos el ciclo creando las plantillas de Skills
for new in tblnews.all():
        # st.write(skill['fields'])
        new=new['fields']
        newTitle = new['Title']
        newContent = new['Content']    
        newURL = new['Url']
        newSource = new['Source link']
        newCover = new['Cover'][0]['url']

        # HTML
        newHTML = f"""                    
                <div class="col s12 m4">
                    <div class="card large">
                        <div class="card-image" style="height:200px">
                            <a href={newURL}><img src="{newCover}"></a>
                        </div> 
                        <div class="card-content">
                            <span class="card-title">{newTitle}</span>
                            <p>{newContent}</p>
                        </div>
                        <div class="card-action">
                            <div class="col s12 m6">
                                <p>Source:<br/> {newSource}</p>
                            </div>
                        </div>
                    </div>
                </div>
                    """
        news=news+newHTML
newHTML=f"""
            <div class="row">            
                {news}       
            </div>       
        """     
    # render product HTML
st.html(newHTML)
# Profile table data
profile = tblprofile.all()[0]['fields']
name=profile['Name']
profileDescription=profile['Description']
Youtube=profile['Youtube']
Facebook=profile['Facebook']
Gmail=profile['Gmail']
picture=profile['Picture'][0]['url']


footerHTML=f"""
        <footer class="page-footer">
          <div class="container">
            <div class="row">
              <div class="col l6 s12">
                <h5 class="white-text">{name}</h5>
                <p class="grey-text text-lighten-4">{profileDescription}</p>
              </div>
              <div class="col l4 offset-l2 s12">
                <h5 class="white-text">Kênh</h5>
                <ul>
                  <li><a class="grey-text text-lighten-3" href={Facebook}>Fanpage</a></li>
                  <li><a class="grey-text text-lighten-3" href={Youtube}>Youtube</a></li>
                  <li><a class="grey-text text-lighten-3" href={Gmail}>Gmail</a></li>
                </ul>
              </div>
            </div>
          </div>
          <div class="footer-copyright">
            <div class="container">
            © 2025 Copyright
            </div>
          </div>
        </footer>
            """
# html generate
st.html(footerHTML)
st.markdown('<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>', unsafe_allow_html=True)