import streamlit as st
import google.generativeai as genai
from urllib.parse import quote

# Konfigurasi Tampilan
st.set_page_config(page_title="Mbah Seno Prod v2", layout="centered")

# 1. Koneksi Gemini dari Secrets
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("❌ API Key Gemini tidak ditemukan di Secrets!")
    st.stop()

st.title("👴 Mbah Seno Production")
st.write("Skrip & Visual Generator (Mode Hemat Modal)")

# 2. Input
topik = st.text_input("Produk apa yang mau Mbah bahas?", placeholder="Contoh: Rice Cooker Hemat Listrik")
tipe_konten = st.selectbox("Jenis Konten:", ["Video TikTok", "Carousel Edukasi"])

if st.button("🚀 MULAI PRODUKSI", use_container_width=True):
    if not topik:
        st.warning("Tulis dulu produknya, Cu!")
    else:
        with st.spinner("Mbah sedang merancang skrip dan foto..."):
            try:
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                # Prompt yang sangat detail untuk hasil gambar maksimal
                prompt_logic = (
                    f"Kamu adalah Mbah Seno, kakek Indonesia yang bijak. Buat skrip {tipe_konten} tentang {topik}. "
                    "Setelah skrip, buatkan 1 baris 'Visual Description' dalam bahasa Inggris untuk foto Mbah Seno. "
                    "Deskripsi harus mengandung: 'Indonesian old man, white hair, realistic skin, wearing batik, "
                    "holding the product, soft natural sunlight, professional photography, blurred background'."
                )
                
                response = model.generate_content(prompt_logic)
                full_text = response.text
                
                # Ambil prompt visual singkat untuk API gratis Pollinations
                # Kita buat otomatis agar gambarnya konsisten
                visual_prompt = f"Professional photography of Mbah Seno, Indonesian old man, white hair, realistic face, wearing batik, holding {topik}, cinematic lighting, high resolution, 8k"
                encoded_prompt = quote(visual_prompt)
                image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1080&height=1350&nologo=true&seed=42"

                # 3. Tampilan Hasil
                st.subheader("📸 Konsep Visual Mbah Seno:")
                st.image(image_url, caption=f"Preview Foto Mbah Seno - {topik}", use_container_width=True)
                
                st.subheader("📝 Skrip Video:")
                st.markdown(full_text)
                
                st.success("✅ Konten Selesai! Foto bisa di-save (tekan lama di HP).")

            except Exception as e:
                st.error(f"Maaf Cu, ada kendala: {e}")

st.divider()
st.caption("Investigator Mbah Seno © 2026")
