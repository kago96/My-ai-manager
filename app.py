import streamlit as st
import google.generativeai as genai

# Tampilan khusus HP
st.set_page_config(page_title="Investigator Produk 2026", layout="centered")

# 1. Koneksi Aman ke Secrets
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception:
    st.error("❌ API Key tidak ditemukan di Secrets!")
    st.stop()

st.title("🔎 Investigator Produk AI")
st.write("Versi Stabil 2026 - Koneksi Aman")

# 2. Pilihan Karakter
persona = st.radio("Pilih Talent:", ["Nara (Tech)", "Mbah Seno (Bijak)"], horizontal=True)

# 3. Input Konten
topik = st.text_input("Produk yang akan diinvestigasi:", placeholder="Contoh: Gadget terbaru 2026")
tipe_konten = st.selectbox("Jenis Konten:", ["TikTok/Reels Hook", "Ulasan Jujur", "Perbandingan Worth-it"])

# 4. Proses Pembuatan Skrip
if st.button("🚀 Buat Skrip Sekarang", use_container_width=True):
    if not topik:
        st.warning("Isi dulu nama produknya!")
    else:
        with st.spinner("Menghubungi AI..."):
            try:
                # Menggunakan Gemini 1.5 Flash (Model paling stabil & cepat di 2026)
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                instr = f"Karakter: {persona}. Gaya Nara: santai/tech-savvy. Gaya Mbah Seno: bijak/jujur."
                prompt = f"{instr}. Buatlah {tipe_konten} tentang {topik}. Sertakan hook viral dan prompt gambar AI."
                
                response = model.generate_content(prompt)
                
                st.subheader("📝 Hasil Skrip:")
                st.write(response.text)
                st.success("✅ Berhasil! API Key Anda tetap tersembunyi.")
            except Exception as e:
                st.error(f"Terjadi kesalahan teknis: {e}")

st.divider()
st.caption("Investigator AI Dashboard © 2026")
