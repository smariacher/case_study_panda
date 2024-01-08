import streamlit as st

st.set_page_config(page_title="Maintenance List")

st.write("# Maintenance List")
st.write("Sum of all Maintenance Costs per quarter: 60€")

st.write("## Next Maintenance")

lst = ["Device 1", "Device 2", "Device 3"]
lst_time = ["10:00", "11:00", "12:00"]
lst_date = ["2021-01-01", "2021-01-02", "2021-01-03"]
lst_maintainer = ["Max Mustermann", "Max Mustermann", "Max Mustermann"]
lst_costs = ["10€", "20€", "30€"]

for i in range(len(lst)):
    st.write(f"### {lst[i]}")
    st.write(f"Date: {lst_date[i]}")
    st.write(f"Time: {lst_time[i]}")
    st.write(f"Costs: {lst_costs[i]}")
    st.write(f"Maintainer: {lst_maintainer[i]}")
    st.write("---")
