import streamlit as st
from google import genai

# Konfigurasi halaman
st.set_page_config(page_title="Investigator Produk 2026", layout="centered")

# Mengambil API Key dari Secrets secara otomatis (Tidak terlihat di layar)
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=API_KEY)
except Exception:
    st.error("API Key tidak ditemukan! Pastikan sudah memasukkannya di menu 'Secrets' di Streamlit Cloud.")
    st.stop()

st.title("🔎 Investigator Produk AI")
st.write("Aplikasi Aman & Privat (API Key Tersembunyi)")

# Pilihan Talent
persona = st.radio("Pilih Talent:", ["Nara (Tech)", "Mbah Seno (Bijak)"], horizontal=True)

# Input Produk
topik = st.text_input("Produk yang akan diinvestigasi:", placeholder="Contoh: Laptop 2026")
tipe_konten = st.selectbox("Jenis Konten:", ["TikTok/Reels Hook", "Ulasan Jujur", "Perbandingan Worth-it"])

# Tombol Eksekusi
if st.button("🚀 Buat Skrip Sekarang", use_container_width=True):
    if not topik:
        st.warning("Isi dulu nama produknya!")
    else:
        with st.spinner("Menghubungi AI..."):
            try:
                instr = "Nara: influencer tech wanita, santai. Mbah Seno: kakek bijak, jujur."
                prompt = f"{instr}. Karakter: {persona}. Buat {tipe_konten} untuk {topik}."
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash', # Menggunakan versi stabil terbaru
                    contents=prompt
                )
                
                st.subheader("📝 Hasil Skrip:")
                st.write(response.text)
                st.success("Berhasil! API Key Anda tetap rahasia.")
            except Exception as e:
                st.error(f"Gagal memproses: {e}")

st.divider()
st.caption("Investigator AI Dashboard © 2026")
