import streamlit as st
import google.generativeai as genai

# Konfigurasi halaman untuk HP
st.set_page_config(page_title="Investigator Produk AI", layout="centered")

# CSS agar tampilan lebih bersih di layar kecil
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; height: 3.5em; background-color: #FF4B4B; color: white; }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.title("⚙️ Pengaturan")
    # .strip() akan menghapus spasi dan .replace() menghapus titik dua jika tidak sengaja ter-copy
    raw_key = st.text_input("Tempel Gemini API Key:", type="password")
    api_key = raw_key.strip().replace(":", "") 

st.title("🔎 Investigator Produk AI")
st.write("Target: Konten Viral & Konsisten.")

persona = st.radio("Pilih Talent:", ["Nara (Tech Enthusiast)", "Mbah Seno (Bijak/Senior)"], horizontal=True)
topik = st.text_input("Produk yang akan diinvestigasi:", placeholder="Contoh: Headphone Sony vs Bose")
tipe_konten = st.selectbox("Jenis Konten:", ["Ulasan Singkat (TikTok)", "Perbandingan Harga", "Hook Video Viral"])

if st.button("🚀 Buat Skrip Sekarang"):
    if not api_key:
        st.error("Silakan masukkan API Key di menu samping (klik > di kiri atas HP).")
    elif not topik:
        st.warning("Produknya diisi dulu ya!")
    else:
        try:
            # Mengatur API
            genai.configure(api_key=AIzaSyBqHERInpihiwddT5DYPoSeh2ZzFXiY5Dw)
            # Menggunakan model 'gemini-1.5-flash' yang paling cepat
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            with st.spinner("Sedang meriset produk..."):
                if "Nara" in persona:
                    gaya = "Gaya: Wanita muda, tech-savvy, santai tapi tepat seperti Gadgetin. Bahasa: Indonesia santai."
                else:
                    gaya = "Gaya: Pria tua bijak, investigator jujur, bahasa sederhana namun hangat."
                
                prompt = f"{gaya}. Buatlah {tipe_konten} tentang {topik}. Sertakan Hook pembuka 3 detik yang viral dan 1 prompt gambar AI di akhir."
                
                response = model.generate_content(prompt)
                
                st.subheader("📝 Hasil Skrip:")
                st.write(response.text)
                st.success("Berhasil! Tinggal salin ke CapCut.")
                
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
            st.info("Tips: Pastikan API Key Anda sudah benar dan tidak ada spasi di awal/akhir.")

st.divider()
st.caption("Dibuat untuk mempermudah aset digital Anda.")
