import streamlit as st
import google.generativeai as genai

# Pengaturan tampilan agar pas di layar HP
st.set_page_config(page_title="Investigator AI Dashboard", layout="centered")

# CSS khusus agar tombol lebih mudah ditekan di HP
st.markdown("""
    <style>
    .stButton>button { width: 100%; height: 3em; font-size: 18px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Input API Key (Sidebar tersembunyi untuk keamanan)
with st.sidebar:
    st.title("Settings")
    api_key = st.text_input("Gemini API Key:", type="password")
    if api_key:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash') # Versi flash lebih cepat & murah

st.title("🔎 Investigator Produk AI")
st.write("Kelola Nara & Mbah Seno dalam satu genggaman.")

# Pilih Persona dengan Deskripsi yang sudah 'Ter-Lock'
persona = st.radio("Pilih Talent:", ["Nara (Tech Enthusiast)", "Mbah Seno (Bijak/Senior)"], horizontal=True)

# Input Topik
topik = st.text_input("Produk yang akan diinvestigasi:", placeholder="Contoh: iPhone 15 vs Xiaomi 14")

# Pilihan tipe konten
tipe_konten = st.selectbox("Jenis Konten:", ["Ulasan Singkat (Shorts/TikTok)", "Perbandingan Harga", "Hook Video Viral"])

if st.button("Generate Script & Prompt"):
    if not api_key:
        st.error("Masukkan API Key di menu samping!")
    elif not topik:
        st.warning("Isi produknya dulu, Bos!")
    else:
        with st.spinner("AI sedang meriset..."):
            # System Instruction agar konsisten
            if "Nara" in persona:
                instr = "Gaya: Wanita muda, tech-savvy, santai tapi tepat (seperti Gadgetin). Bahasa: Indonesia gaul tapi sopan. Fokus: Estetika dan fungsionalitas."
            else:
                instr = "Gaya: Kakek bijak, bahasa sederhana, jujur, investigator. Bahasa: Indonesia baku tapi hangat. Fokus: Ketahanan dan nilai uang."
            
            prompt = f"{instr}. Buatlah {tipe_konten} untuk produk: {topik}. Sertakan 3 pilihan 'Hook' pembuka yang menarik perhatian dalam 3 detik pertama. Di akhir, berikan 1 prompt gambar AI untuk thumbnail."
            
            response = model.generate_content(prompt)
            
            # Menampilkan hasil dengan fitur 'Copy' yang mudah di HP
            st.subheader("🚀 Hasil Investigasi")
            st.text_area("Copy skrip di sini:", value=response.text, height=400)
            st.success("Tugas Anda: Salin ke CapCut, gunakan suara AI, dan posting!")

st.divider()
st.caption("Target: Konsisten & Viral. Jangan lupa cek trend di TikTok pagi ini!")
