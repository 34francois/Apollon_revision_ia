import streamlit as st

# Configuration de la page
st.title("Générateur de QCM avec Mistral AI")

# Interface utilisateur pour entrer les paramètres du QCM
st.header("Paramètres du QCM")
sujet = st.text_input("Sujet du QCM")
nombre_questions = st.number_input("Nombre de questions", min_value=1, max_value=20, value=5)
difficulte = st.selectbox("Difficulté", ["Facile", "Moyen", "Difficile"])

# Bouton pour générer le QCM
if st.button("Générer le QCM"):
    # Appel à l'API de Mistral (à implémenter)
    # Remplacez ceci par le code réel pour appeler l'API et obtenir les questions
    questions = [
        {"question": "Quelle est la capitale de la France ?", "options": ["Paris", "Londres", "Berlin", "Madrid"], "réponse": "Paris"},
        {"question": "Quel est le plus grand océan du monde ?", "options": ["Atlantique", "Indien", "Arctique", "Pacifique"], "réponse": "Pacifique"},
    ]

    # Affichage des questions générées
    st.header("Questions générées")
    for i, q in enumerate(questions, start=1):
        st.subheader(f"Question {i}: {q['question']}")
        for option in q["options"]:
            st.write(f"- {option}")
        st.write(f"**Réponse:** {q['réponse']}")
