import streamlit as st
import pandas as pd
from db_fxns import *


# Data Viz Pkgs
import plotly.express as px

st.set_page_config(page_title="Werkzaamheden", page_icon=":hammer:", layout="wide")

def main():
    menu = ["Create", "Read", "Update", "Delete", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    task_kind = ["Electra", "Slopen", "Timmerwerk", "Stucwerk", "Schilderwerk", "Betonvloer", "Loodgieter", "Metselwerk", "Isoleren", "Keuken bouwen", "Badkamer bouwen"]
    task_kind = sorted(task_kind)
    task_kind_all = task_kind #ik heb hier een tweede variabele gemaakt om in regel 94 nog iets van een semicoherent resultaat te krijgen
    create_tabel()


    if choice == "Create":
        st.subheader("Add Items")

        #LAYOUT
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            task = st.text_area("Klus")
            task_kind = st.selectbox("Soort werk", task_kind)
            task_material = st.text_area("Materiaalkeuze", placeholder="NVT", height=8)
        with col2:
            task_square = st.number_input("M2")
            task_due_date = st.date_input("Deadline")
        with col3:
            task_status = st.selectbox("Status", ["To do", "Doing", "Done"])
            task_bill_date = st.date_input("Datum rekening")
            task_special = st.text_area("Bijzonderheden")
        with col4:
            task_budget = st.number_input("Begroot in Euro excl. BTW")
            task_bill = st.number_input("Rekening in Euro excl. BTW")

        if st.button("Toevoegen"):
            add_data(task, task_kind, task_material, task_square, task_status, task_due_date, task_bill_date, task_special, task_budget, task_bill)
            st.success("Klus toegevoegd!: {}".format(task))


    elif choice == "Read":
        st.subheader("View Items")
        result = view_all_data()
        df = pd.DataFrame(result, columns=['Klus', 'Soort werk', 'Materiaalkeuze', 'M2', 'Status', 'Deadline',
                                           'Datum Rekening', 'Bijzonderheden', 'Begroot in Euro excl. BTW',
                                           'Rekening in Euro exl. BTW'])
        #st.write(result)
        with st.expander("Alles bekijken"):
            st.dataframe(df)
        with st.expander("Vooruitgang"):
            task_df = df['Status'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            p1 = px.pie(task_df, names="index", values="Status")
            st.plotly_chart(p1)


    elif choice == "Update":
        st.subheader("Edit/ Update Items")
        result = view_all_data()
        df = pd.DataFrame(result, columns=['Klus', 'Soort werk', 'Materiaalkeuze', 'M2', 'Status', 'Deadline',
                                           'Datum Rekening', 'Bijzonderheden', 'Begroot in Euro excl. BTW',
                                           'Rekening in Euro exl. BTW'])

        with st.expander("Huidige klussen bekijken"):
            st.dataframe(df)


        list_of_tasks = [i[0] for i in view_unique_tasks()] #hiermee maak je een lijst van de klussen op klusnaam
        #st.write(list_of_tasks)
        selected_task = st.selectbox("Klus om aan te passen", sorted(list_of_tasks))
        selected_result = get_task(selected_task)
        st.write(selected_result)

        if selected_result:
            task = selected_result[0][0]
            task_kind = selected_result[0][1]
            task_material = selected_result[0][2]
            task_square = selected_result[0][3]
            task_status = selected_result[0][4]
            task_due_date = selected_result[0][5]
            task_bill_date = selected_result[0][6]
            task_special = selected_result[0][7]
            task_budget = selected_result[0][8]
            task_bill = selected_result[0][9]

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                new_task = st.text_area("Klus", task)
                new_task_kind = st.selectbox("Soort werk: " + str(task_kind), task_kind_all) #hier wil ik dus de reeds gekozen optie ingevuld zien
                new_task_material = st.text_area("Gekozen materiaal: "+ str(task_material), task_material, placeholder=task_material, height=8)
            with col2:
                new_task_square = st.number_input("Oppervlakte: "+str(task_square))
                new_task_status = st.selectbox("Status: " + str(task_status), ["To do", "Doing", "Done"])

            with col3:
                new_task_due_date = st.date_input("Deadline")
                new_task_bill_date = st.date_input("Datum rekening")
                new_task_special = st.text_area("Bijzonderheden")
            with col4:
                new_task_budget = st.number_input("Begroot in Euro excl. BTW")
                new_task_bill = st.number_input("Rekening in Euro excl. BTW")

            if st.button("Klus aanpassen"):
                edit_task_data(new_task, new_task_kind, new_task_material, new_task_square, new_task_status,
                               new_task_due_date, new_task_bill_date, new_task_special, new_task_budget, new_task_bill,
                               task, task_kind, task_material, task_square, task_status, task_due_date, task_bill_date,
                               task_special, task_budget, task_bill)
                st.success("{} aangepast naar {}.".format(task, new_task))

        result2 = view_all_data()
        df2 = pd.DataFrame(result2, columns=['Klus', 'Soort werk', 'Materiaalkeuze', 'M2', 'Status', 'Deadline',
                                           'Datum Rekening', 'Bijzonderheden', 'Begroot in Euro excl. BTW',
                                           'Rekening in Euro exl. BTW'])

        with st.expander("Updated"):
            st.dataframe(df2)

    elif choice == 'Delete':
        st.subheader("Delete Item")

    else:
        st.subheader("About")

main()