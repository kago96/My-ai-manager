import streamlit as st
import google.generativeai as genai

# Konfigurasi Tampilan Mobile 2026
st.set_page_config(page_title="Investigator AI 2.5", layout="centered")

# CSS khusus agar tombol lebih 'tap-able' di jempol HP
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 15px; height: 4em; background: linear-gradient(45deg, #007BFF, #00C6FF); color: white; font-weight: bold; border: none; }
    .stRadio > label { font-weight: bold; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

# 1. Koneksi Aman ke Brankas Secrets
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception:
    st.error("❌ API Key tidak ditemukan! Pastikan sudah input di menu Secrets Streamlit.")
    st.stop()

st.title("🔎 Investigator Produk AI")
st.write("Powering by **Gemini 2.5 Flash** | Versi 2026")

# 2. Pilihan Karakter (Persona Selector)
persona = st.radio("Pilih Talent Utama:", ["Nara (Tech Enthusiast)", "Mbah Seno (Bijak/Senior)"], horizontal=True)

# 3. Input Investigasi
topik = st.text_input("Produk/Gadget yang diinvestigasi:", placeholder="Contoh: HP Gaming 2026 Murah")
tipe_konten = st.selectbox("Jenis Konten:", ["Hook Viral TikTok", "Ulasan 'Worth-to-Buy'", "Investigasi Kejujuran Produk"])

# 4. Engine Generator 2.5
if st.button("🚀 GENERATE SKRIP 2.5", use_container_width=True):
    if not topik:
        st.warning("Input produknya dulu, Bos!")
    else:
        with st.spinner(f"Gemini 2.5 sedang memproses karakter {persona}..."):
            try:
                # Mengaktifkan model Gemini 2.5 Flash terbaru
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                # --- ISOLASI KARAKTER TOTAL ---
                if "Nara" in persona:
                    context = (
                        "IDENTITAS: Kamu adalah Nara. Influencer teknologi wanita muda. Gaya bicara: santai, cerdas, "
                        "sedikit sarkas tapi jujur, persis seperti gaya Gadgetin. Fokus pada estetika dan 'vibe' produk. "
                        "LARANGAN: Jangan pernah menyebut Mbah Seno. Jangan menggunakan bahasa kaku."
                    )
                else:
                    context = (
                        "IDENTITAS: Kamu adalah Mbah Seno. Kakek investigator produk yang sangat bijak dan teliti. "
                        "Gaya bicara: tenang, hangat, jujur, menggunakan analogi hidup sederhana. Fokus pada keawetan "
                        "dan harga yang masuk akal. LARANGAN: Jangan pernah menyebut Nara. Gunakan sapaan 'Cucu' atau 'Nak'."
                    )
                
                prompt_final = f"{context}\n\nTUGAS: Buatlah skrip {tipe_konten} tentang {topik}. " \
                               f"Sertakan 3 pilihan Hook Viral dan 1 Prompt Gambar AI yang spesifik di akhir."
                
                response = model.generate_content(prompt_final)
                
                # Tampilan Hasil
                st.subheader(f"📝 Output Skrip {persona.split()[0]}:")
                st.write(response.text)
                st.success("✅ Generasi 2.5 Berhasil!")
                
            except Exception as e:
                st.error(f"Gagal memanggil Gemini 2.5: {e}")
                st.info("Catatan: Jika model 2.5 belum tersedia di region Anda, coba ganti kodenya ke 'gemini-2.0-flash'.")

st.divider()
st.caption("Investigator AI Dashboard © 2026 - Optimized for Mobile")
