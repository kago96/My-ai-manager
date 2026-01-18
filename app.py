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
st.write("Target: Konten Viral & Konsisten")

# 2. Pilihan Karakter
persona = st.radio("Pilih Talent:", ["Nara (Tech Enthusiast)", "Mbah Seno (Bijak/Senior)"], horizontal=True)

# 3. Input Konten
topik = st.text_input("Produk yang akan diinvestigasi:", placeholder="Contoh: HP 2 Jutaan Terbaik")
tipe_konten = st.selectbox("Jenis Konten:", ["TikTok/Reels Hook", "Ulasan Jujur", "Perbandingan Worth-it"])

# 4. Proses Pembuatan Skrip
if st.button("🚀 Buat Skrip Sekarang", use_container_width=True):
    if not topik:
        st.warning("Isi dulu nama produknya!")
    else:
        with st.spinner(f"AI sedang merasuki jiwa {persona}..."):
            try:
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                # --- LOGIKA PEMISAHAN KARAKTER (UPDATE) ---
                if "Nara" in persona:
                    instruksi_karakter = (
                        "Kamu ADALAH Nara. Seorang tech enthusiast wanita muda yang santai, cerdas, "
                        "dan to-the-point seperti gaya Gadgetin. Gunakan bahasa Indonesia yang modern dan ringan. "
                        "JANGAN menyebutkan Mbah Seno atau karakter lain. Fokuslah pada estetika dan fungsionalitas gadget."
                    )
                else:
                    instruksi_karakter = (
                        "Kamu ADALAH Mbah Seno. Seorang kakek bijak yang jujur, teliti, dan berpengalaman "
                        "dalam menginvestigasi kualitas produk. Gunakan bahasa Indonesia yang sederhana, hangat, "
                        "dan berwibawa. JANGAN menyebutkan Nara atau karakter lain. Fokuslah pada ketahanan dan nilai uang (value for money)."
                    )
                
                # Gabungkan instruksi dengan permintaan konten
                prompt_akhir = f"{instruksi_karakter}\n\nTugas: Buatlah {tipe_konten} tentang {topik}. Sertakan 3 pilihan hook viral di awal dan 1 prompt gambar AI di akhir."
                
                response = model.generate_content(prompt_akhir)
                
                st.subheader(f"📝 Skrip untuk {persona}:")
                st.write(response.text)
                st.success(f"✅ Berhasil! Skrip ini murni gaya {persona.split()[0]}.")
                
            except Exception as e:
                st.error(f"Terjadi kesalahan teknis: {e}")

st.divider()
st.caption("Investigator AI Dashboard © 2026")
