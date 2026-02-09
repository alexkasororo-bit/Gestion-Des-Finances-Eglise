import streamlit as st

# -----------------------------
# Initialisation des données
# -----------------------------
st.set_page_config(page_title="GESTION FINANCIERE DE L'EGLISE DUFAY", page_icon="💒")

st.title("GESTION DES FINANCES DE L'EGLISE DUFAY")
st.write("Cette application permet de gérer les différents comptes financiers de l'église DUFAY.","\nElle permet à l'utilisateur d'entrer et de sortir le montant dans le compte","\nL'utilisateur peut également vérifier la situation financière d'un compte")
          
types_comptes = ["Construction", "Offrandes ordinaires", "Dimes", "Musique"]

# Initialiser les soldes dans la session
if "comptes" not in st.session_state:
    st.session_state.comptes = {compte: 0.0 for compte in types_comptes}

# -----------------------------
# Sélection du compte
# -----------------------------
st.subheader("CHOIX DU COMPTE")
compte_selectionne = st.selectbox(
    "Veuillez sélectionner le compte",
    types_comptes
)

# -----------------------------
# Choix de l'opération
# -----------------------------
st.subheader("OPERATIONS DISPONIBLES")
operation = st.radio(
    "Quelle opération voulez-vous effectuer ?",
    ("Consulter le compte", "Entrée dans le compte", "Sortie du compte")
)

# -----------------------------
# Traitement des opérations
# -----------------------------
if operation == "Consulter le compte":
    st.info(
        f"💰 Le solde du compte **{compte_selectionne}** est de "
        f"**{st.session_state.comptes[compte_selectionne]:.2f} $**"
    )

elif operation == "Entrée dans le compte":
    montant = st.number_input(
        "Veuillez entrer le montant à ajouter dans le compte en ($)",
        min_value=0.0,
        step=10.0
    )
    if st.button("Ajouter"):
        st.session_state.comptes[compte_selectionne] += montant
        st.success(
            f"{montant:.2f} $ ajoutés au compte **{compte_selectionne}**"
        )

elif operation == "Sortie du compte":
    montant = st.number_input(
        "Veuillez entrer le montant à retirer ($)",
        min_value=0.0,
        step=10.0
    )
    if st.button("Retirer"):
        if montant <= st.session_state.comptes[compte_selectionne]:
            st.session_state.comptes[compte_selectionne] -= montant
            st.success(
                f"{montant:.2f} $ retirés du compte **{compte_selectionne}**"
            )
        else:
            st.error(" Le solde est insuffisant.")

# -----------------------------
# Affichage du récapitulatif
# -----------------------------
st.subheader(" RECAPITULATIF DES COMPTES")
st.table(st.session_state.comptes)
st.caption("Cette application a été dévelopée par l'Ingénieur Alexandre KASORORO E.")
