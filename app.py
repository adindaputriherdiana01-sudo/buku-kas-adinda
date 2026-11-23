import streamlit as st

st.set_page_config(page_title="Buku Kas Dinda ")

st.title("Buku Kas Dinda")
st.write("aplikasi pencatatan keuangan sederhana")

st.subheader("tambah transaksi")

tanggal = st.date_input("tanggal")
jenis = st.selectbox("jenis transaksi", ["masuk", "keluar"])
kategori = st.text_input("kategori")
jumlah = st.number_input("jumlah(Rp)", min_value=0, step=1000)

if "transaksi" not in st.session_state:

    st.session_state.transaksi = []

if st.button("simpan transaksi"):
    if kategori and jumlah > 0:

        st.session_state.transaksi.append({
                "tanggal": str(tanggal),
                "jenis": jenis,
                "kategori": kategori,
                "jumlah": jumlah
        
        })
        st.success("transaksi berhasil disimpan!") 
    else:
        st.warning("isi kategori dan jumlah terlebih dahulu")

st.subheader("riwayat transaksi")

if st.session_state.transaksi:
    st.dataframe(st.session_state.transaksi)

    masuk = sum(t["jumlah"] for t in st.session_state.transaksi if t["jenis"] == "masuk")
    keluar = sum(t["jumlah"] for t in st.session_state.transaksi if t["jenis"] == "keluar")

    st.metric("total pemasukan", f"Rp {masuk:,}")
    st.metric("total pengeluaran", f"Rp {keluar:,}")
    saldo = masuk - keluar
    st.metric("saldo akhir", "Rp " + format(saldo, ","))
else:
    st.info("belum ada transaksi.")    