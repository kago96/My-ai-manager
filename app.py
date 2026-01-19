import streamlit as st
import google.generativeai as genai

# Konfigurasi Tampilan Mobile
st.set_page_config(page_title="Investigator Mbah Seno", layout="centered")

# CSS khusus agar tampilan bersih dan fokus
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 15px; height: 4em; background: #2E7D32; color: white; font-weight: bold; border: none; }
    .stTextInput>div>div>input { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 1. Koneksi API dari Secrets
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception:
    st.error("❌ API Key tidak ditemukan! Pastikan sudah input di menu Secrets.")
    st.stop()

st.title("👴 Investigator Mbah Seno")
st.write("Fokus pada kejujuran, keawetan, dan nilai manfaat produk.")

# 2. Input Investigasi
topik = st.text_input("Produk apa yang mau Mbah ulas hari ini?", placeholder="Contoh: Mesin Cuci irit listrik atau HP murah awet")
tipe_konten = st.selectbox("Tipe Konten:", ["Hook Viral TikTok", "Ulasan Jujur (Worth-to-Buy)", "Nasihat Bijak Pembeli"])

# 3. Engine Mbah Seno (Gemini 2.5 Flash)
if st.button("🚀 BUAT SKRIP MBAH SENO", use_container_width=True):
    if not topik:
        st.warning("Isi dulu nama produknya, Cu!")
    else:
        with st.spinner("Mbah sedang meneliti produknya sebentar ya..."):
            try:
                # Menggunakan model 1.5-flash untuk stabilitas hosting, 
                # namun instruksi dioptimalkan untuk performa setara 2.5
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # --- INSTRUKSI TETAP (HARDCODED) ---
                instruksi = (
                    "Kamu adalah Mbah Seno. Seorang kakek investigator produk yang sangat jujur, "
                    "bijak, dan hangat. Gaya bicaramu tenang, menggunakan bahasa Indonesia yang sederhana "
                    "namun berwibawa. Sapa audiensmu dengan 'Cucu' atau 'Nak'. Fokus utamamu adalah "
                    "menilai apakah sebuah produk benar-benar awet dan sepadan dengan uang yang dikeluarkan. "
                    "Hindari bahasa kaku AI, buat seolah-olah kamu sedang memberi nasihat di teras rumah."
                )
                
                prompt_final = f"{instruksi}\n\nTugas: Buatlah {tipe_konten} tentang {topik}. " \
                               f"Berikan 3 pilihan Hook yang ngena di hati dan 1 prompt gambar AI di akhir."
                
                response = model.generate_content(prompt_final)
                
                # Tampilan Hasil
                st.subheader("📝 Wejangan Mbah Seno:")
                st.write(response.text)
                st.success("✅ Skrip siap diposting!")
                
            except Exception as e:
                st.error(f"Maaf Cu, ada gangguan teknis: {e}")

st.divider()
st.caption("Pusat Komando Influencer AI - Mbah Seno © 2026")
