import streamlit as st 
import PyPDF2

# Définition d'une fonction pour extraire le texte d'un fichier PDF
def extract_text_from_pdf(uploaded_file):
    text = ""  # Initialisation d'une variable texte extrait
    with uploaded_file as f:  # Utilisation d'un context manager pour ouvrir le fichier PDF temporaire
        reader = PyPDF2.PdfFileReader(f)  # Création d'un objet de lecture PDF
        for page_num in range(reader.numPages):  # Boucle à travers chaque page du PDF
            page = reader.getPage(page_num)  # Récupération de la page courante
            text += page.extractText()  # Extraction du texte de la page et ajout à la variable de texte
    return text  # Renvoie le texte extrait

# Fonction principale de l'application Streamlit
def main():
    st.title("Application de préparation de données SFCR pour fiche de synthèse")

    # Section latérale pour l'upload des fichiers PDF
    st.sidebar.title("SFCR année N")
    uploaded_file_n = st.sidebar.file_uploader("Uploader le SFCR année N", type=["pdf"])

    st.sidebar.title("SFCR année N-1")
    uploaded_file_n_minus_1 = st.sidebar.file_uploader("Uploader le SFCR année N-1", type=["pdf"])

    # Vérification de l'existence des deux fichiers PDF
    if uploaded_file_n is not None and uploaded_file_n_minus_1 is not None:
        # Bouton pour déclencher l'extraction du texte
        if st.button("Extraire le texte"):
            # Extraction du texte des deux fichiers PDF en utilisant la fonction définie précédemment
            text_n = extract_text_from_pdf(uploaded_file_n)
            text_n_minus_1 = extract_text_from_pdf(uploaded_file_n_minus_1)
            
            # Affichage du texte extrait dans deux encarts distincts
            st.subheader("Texte extrait du SFCR année N:")
            st.write(text_n)

            st.subheader("Texte extrait du SFCR année N-1:")
            st.write(text_n_minus_1)

# Exécution de la fonction principale lorsque le script est lancé
if __name__ == "__main__":
    main()
