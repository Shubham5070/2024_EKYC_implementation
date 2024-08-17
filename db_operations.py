import streamlit as st
from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
import pandas as pd

# Define SQLAlchemy engine
DATABASE_URL = 'mysql+mysqlconnector://Shubham:Shubham123@127.0.0.1:3306/ekyc'
engine = create_engine(DATABASE_URL)

# Define SQLAlchemy metadata
metadata = MetaData()

# Define SQLAlchemy table
users = Table(
    'users', metadata,
    Column('id', String(50), primary_key=True),
    Column('name', String(100)),
    Column('father_name', String(100)),
    Column('dob', Date),
    Column('id_type', String(20)),
    Column('embedding', String(500))
)

# Create session maker
Session = sessionmaker(bind=engine)

# Function to insert records into MySQL
def insert_record(text_info):
    with engine.connect() as conn:
        insert_stmt = users.insert().values(
            id=text_info['ID'],
            name=text_info['Name'],
            father_name=text_info["Father's Name"],
            dob=text_info['DOB'],
            id_type=text_info['ID Type'],
            embedding=str(text_info['Embedding'])
        )
        conn.execute(insert_stmt)

# Function to fetch records from MySQL
def fetch_records():
    with engine.connect() as conn:
        select_stmt = users.select()
        result = conn.execute(select_stmt)
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        return df

# Function to check duplicacy based on ID
def check_duplicacy(text_info):
    df = fetch_records()
    df_filtered = df[df['id'] == text_info['ID']]
    return not df_filtered.empty

# Streamlit main function
def main():
    st.title('Streamlit MySQL Example')
    
    # Insert record section
    st.header('Insert Record')
    id_input = st.text_input('ID')
    name_input = st.text_input('Name')
    father_name_input = st.text_input("Father's Name")
    dob_input = st.date_input('DOB')
    id_type_input = st.text_input('ID Type')
    embedding_input = st.text_area('Embedding')

    if st.button('Insert'):
        text_info = {
            'ID': id_input,
            'Name': name_input,
            "Father's Name": father_name_input,
            'DOB': dob_input,
            'ID Type': id_type_input,
            'Embedding': embedding_input
        }
        insert_record(text_info)
        st.success('Record inserted successfully!')

    # Fetch records section
    st.header('Fetch Records')
    if st.button('Fetch All Records'):
        df = fetch_records()
        st.dataframe(df)

    # Check duplicacy section
    st.header('Check Duplicacy')
    check_id = st.text_input('Enter ID to check duplicacy')
    if st.button('Check'):
        if check_duplicacy({'ID': check_id}):
            st.warning('Duplicate found!')
        else:
            st.success('No duplicate found!')

if __name__ == '__main__':
    main()
