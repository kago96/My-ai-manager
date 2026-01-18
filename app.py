import streamlit as st
import google.generativeai as genai

# Konfigurasi Tampilan Mobile-Friendly
st.set_page_config(page_title="AI Influencer Manager", layout="centered")

# Masukkan API Key Gemini di sini (Nanti bisa disembunyikan di Secrets)
# Untuk coba-coba, Anda bisa input manual di UI
api_key = st.sidebar.text_input("Masukkan Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
else:
    st.warning("Silakan masukkan API Key di menu samping (sidebar) untuk memulai.")

st.title("📱 Manager Influencer AI")
st.write("Kelola konten Nara & Mbah Seno dari HP.")

# Pilih Karakter
persona = st.selectbox("Pilih Karakter:", ["Nara (Tech Enthusiast - Santai)", "Mbah Seno (Bijak - Senior)"])

# Input Topik
topik = st.text_input("Produk/Gadget apa yang mau dibahas?", placeholder="Contoh: HP Gaming 2 Jutaan")

# Tombol Eksekusi (Dibuat lebar untuk jempol HP)
if st.button("Buat Konten Sekarang", use_container_width=True):
    if not api_key:
        st.error("Isi API Key dulu ya!")
    elif not topik:
        st.error("Isi topiknya dulu!")
    else:
        with st.spinner("Sedang berpikir..."):
            # Prompt Khusus
            if "Nara" in persona:
                prompt = f"Berperanlah sebagai Nara, influencer tech wanita yang santai dan to-the-point seperti Gadgetin. Buat skrip video pendek TikTok/Shopee Video tentang {topik}. Fokus pada worth it atau tidaknya. Berikan juga prompt gambar AI untuk konten ini."
            else:
                prompt = f"Berperanlah sebagai Mbah Seno, pria tua bijak yang paham teknologi tapi menjelaskan dengan bahasa sederhana. Buat skrip video pendek tentang {topik}. Berikan nasihat apakah ini pemborosan atau kebutuhan. Berikan juga prompt gambar AI-nya."

            response = model.generate_content(prompt)
            
            # Tampilan Hasil
            st.subheader("📝 Skrip Video")
            st.write(response.text)
            
            st.info("Tips: Salin skrip di atas ke CapCut atau aplikasi Text-to-Speech.")

# Footer
st.divider()
st.caption("Dibuat untuk pengelolaan Influencer AI mandiri via HP.")

