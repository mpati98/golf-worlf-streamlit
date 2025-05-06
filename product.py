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

# Get Airtable key and base id
AIRTABLE_API_KEY = st.secrets.AIRTABLE_API_KEY
AIRTABLE_BASE_ID=st.secrets.AIRTABLE_BASE_ID

# Get AT data
api = Api(AIRTABLE_API_KEY)
# Cargamos las tablas
tblprofile = api.table(AIRTABLE_BASE_ID, 'Profile')
tblprojects = api.table(AIRTABLE_BASE_ID, 'Project')
tblAllProduct = api.table(AIRTABLE_BASE_ID, 'Product_All')
tblGayProduct = api.table(AIRTABLE_BASE_ID, 'Product_Gay')
tblOtherProduct = api.table(AIRTABLE_BASE_ID, 'Product_Other')

brandHTML=f"""
<div class="row">
<h1>Love Golf <span class="blue-text text-darken-3">Shop</span> </h1>
</div>
"""
# html generate
st.html(brandHTML)

# Tab product list
tabAllProduct,tabGayProduct, tabOtherProduct =st.tabs(['Tất cả sản phẩn','Gậy Golf', "Phụ kiện Golf"])

# Mostramos el tab de Skills
with tabAllProduct:
    products=""
    # Hacemos el ciclo creando las plantillas de Skills
    for product in tblAllProduct.all():
        # st.write(skill['fields'])
        product=product['fields']
        productName = product['Name']
        productDescription = product['Notes']    
        productRate = product['Rating']
        productImg = product['Img'][0]['url']
        productStars=""
        # Creación de rating con estrellas
        for i in range(1,6):
            if i<=productRate:
                # Estrella completa
                productStars=productStars+'<i class="material-icons">star</i>'
            else:
                # Estrella vacía
                productStars=productStars+'<i class="material-icons">star_border</i>'
                
        productCost = product['Cost']   
        # Plantilla del card de skill
        productHTML = f"""                    
                <div class="col s12 m4">
                    <div class="card large">
                        <div class="card-image" style="height:200px">
                            <a href="#"><img src="{productImg}"></a>
                        </div> 
                        <div class="card-content">
                            <span class="card-title">{productName}</span>
                            <p>{productDescription}</p>
                        </div>
                        <div class="card-action">
                            <div class="col s12 m6">
                                <p>Rating:<br/> {productStars}</p>
                            </div>
                            <div class="col s12 m6">
                                <p fon>Giá:<br/> {productCost}</p>
                            </div>
                        </div>
                    </div>
                </div>
                    """
        products=products+productHTML
    productHTML=f"""
            <div class="row">            
                {products}       
            </div>       
        """     
    # render product HTML
    st.html(productHTML)
with tabGayProduct:
    gayProducts=""
    # Hacemos el ciclo creando las plantillas de Skills
    for gayProduct in tblGayProduct.all():
        # st.write(skill['fields'])
        gayProduct=gayProduct['fields']
        gayProductName = gayProduct['Name']
        gayProductDescription = gayProduct['Notes']    
        gayProductRate = gayProduct['Rating']
        gayProductImg = gayProduct['Img'][0]['url']
        gayProductStars=""
        # Creación de rating con estrellas
        for i in range(1,6):
            if i<=gayProductRate:
                # Estrella completa
                gayProductStars=gayProductStars+'<i class="material-icons">star</i>'
            else:
                # Estrella vacía
                gayProductStars=gayProductStars+'<i class="material-icons">star_border</i>'
                
        gayProductCost = gayProduct['Cost']   
        # Plantilla del card de skill
        gayProductHTML = f"""                    
                <div class="col s12 m4">
                    <div class="card large">
                        <div class="card-image" style="height:200px">
                            <a href="#"><img src="{gayProductImg}"></a>
                        </div> 
                        <div class="card-content">
                            <span class="card-title">{gayProductName}</span>
                            <p>{gayProductDescription}</p>
                        </div>
                        <div class="card-action">
                            <div class="col s12 m6">
                                <p>Rating:<br/> {gayProductStars}</p>
                            </div>
                            <div class="col s12 m6">
                                <p fon>Giá:<br/> {gayProductCost}</p>
                            </div>
                        </div>
                    </div>
                </div>
                    """
        gayProducts=gayProducts+gayProductHTML
    gayProductHTML=f"""
            <div class="row">            
                {gayProducts}       
            </div>       
        """     
    # render product HTML
    st.html(gayProductHTML)
with tabOtherProduct:
    otherProducts=""
    # Hacemos el ciclo creando las plantillas de Skills
    for otherProduct in tblOtherProduct.all():
        # st.write(skill['fields'])
        otherProduct=otherProduct['fields']
        otherProductName = otherProduct['Name']
        otherProductDescription = otherProduct['Notes']    
        otherProductRate = otherProduct['Rating']
        otherProductImg = otherProduct['Img'][0]['url']
        otherProductStars=""
        # Creación de rating con estrellas
        for i in range(1,6):
            if i<=otherProductRate:
                # Estrella completa
                otherProductStars=otherProductStars+'<i class="material-icons">star</i>'
            else:
                # Estrella vacía
                otherProductStars=otherProductStars+'<i class="material-icons">star_border</i>'
                
        otherProductCost = otherProduct['Cost']   
        # Plantilla del card de skill
        otherProductHTML = f"""                    
                <div class="col s12 m4">
                    <div class="card large">
                        <div class="card-image" style="height:200px">
                            <a href="#"><img src="{otherProductImg}"></a>
                        </div> 
                        <div class="card-content">
                            <span class="card-title">{otherProductName}</span>
                            <p>{otherProductDescription}</p>
                        </div>
                        <div class="card-action">
                            <div class="col s12 m6">
                                <p>Rating:<br/> {otherProductStars}</p>
                            </div>
                            <div class="col s12 m6">
                                <p fon>Giá:<br/> {otherProductCost}</p>
                            </div>
                        </div>
                    </div>
                </div>
                    """
        otherProducts=otherProducts+otherProductHTML
    otherProductHTML=f"""
            <div class="row">            
                {otherProducts}       
            </div>       
        """     
    # render product HTML
    st.html(otherProductHTML) 
# with tabPortfolio:       
#     projects=""
#     skillsHTML=""
#     knowledgeHTML=""
#     # Hacemos el ciclo creando las plantillas de proyectos
#     for project in tblprojects.all():
#         # st.write(skill['fields'])
#         projectid= project['id']
#         project=project["fields"]
#         projectName = project['Name']        
#         projectDescription = project['Description']    
#         # Creamos la lista de Skills y Knowledge
#         projectSkils = project['Skills']
#         skillsHTML=[f'<div class="chip green lighten-4">{p}</div>' for p in projectSkils]
#         skillsHTML="".join(skillsHTML)
#         projectKnowledge = project['Knowledge']        
#         knowledgeHTML=[f'<div class="chip blue lighten-4">{p}</div>' for p in projectKnowledge]
#         knowledgeHTML="".join(knowledgeHTML)
        
#         projectLink = project['Link'] 
#         projectImageUrl = project['Image'][0]['url']        
#         # Plantilla de proyectos
#         projectHTML = f"""                    
#                 <div class="col s12 m6">
#                     <div class="card large">                    
#                         <div class="card-image" style="height:200px">
#                             <a href="{projectLink}"><img src="{projectImageUrl}"></a>
#                         </div>                        
#                         <div class="card-content">
#                             <span class="card-title">{projectName}</span>                                                        
#                             <p>{projectDescription}</p>
#                             <div class="row hide-on-small-only">
#                             <div class="col s12 m6">
#                             <h6>Knowledge:</h6>
#                             {knowledgeHTML}
#                             </div>
#                             <div class="col s12 m6">
#                             <h6>Skills:</h6>
#                             {skillsHTML}
#                             </div>
#                             </div>
#                         </div>  
#                         <div class="card-action right-align">
#                         <a href="{projectLink}" class="waves-effect waves-light btn-large white-text blue darken-3"><i class="material-icons left">open_in_new</i>View</a>                        
#                         </div>                                               
#                     </div>
#                 </div>
#                     """
#         projects=projects+projectHTML
#     projectsHTML=f"""
#             <div class="row">            
#                 {projects}       
#             </div>       
#         """     
#     # Mostramos los proyectos
#     st.html(projectsHTML)        
# with tabContact:
#     st.info("If you think I can help you with some of your projects or entrepreneurships, send me a message I'll contact you as soon as I can. I'm always glad to help")
#     with st.container(border=True):
#         parName = st.text_input("Your name")
#         parEmail = st.text_input("Your email")
#         parPhoneNumber = st.text_input("WhatsApp phone number, with country code")
#         parNotes = st.text_area("What can I do for you")
#         btnEnviar = st.button("Send",type="primary")
#     if btnEnviar:
#         # Creamos el registro de contactos
#         tblContacts.create({"Name":parName,"email":parEmail,"phoneNumber":parPhoneNumber,"Notes":parNotes})
#         st.toast("Message sent")

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