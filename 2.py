import streamlit as st  
import cv2  
import numpy as np  

st.set_page_config(page_title="Ứng dụng Y tế", layout="wide")  

st.title("Ứng dụng Y tế")  

# Hàm để chụp ảnh  
def capture_image(key):  
    img_file = st.camera_input(f"Chụp ảnh cho {key}", key=f"camera_{key}")  
    if img_file is not None:  
        # Đọc ảnh và chuyển đổi sang định dạng OpenCV  
        bytes_data = img_file.getvalue()  
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)  
        return cv2_img  
    return None  

# Tạo các tab  
tab1, tab2, tab3 = st.tabs(["Lâm sàng", "Tiền căn", "Công thức máu"])  

with tab1:  
    st.header("Lâm sàng")  
    lam_sang_img = capture_image("lam_sang")  
    if lam_sang_img is not None:  
        st.image(lam_sang_img, caption="Ảnh Lâm sàng", use_column_width=True)  

with tab2:  
    st.header("Tiền căn")  
    tien_can_img = capture_image("tien_can")  
    if tien_can_img is not None:  
        st.image(tien_can_img, caption="Ảnh Tiền căn", use_column_width=True)  

with tab3:  
    st.header("Công thức máu")  
    cong_thuc_mau_img = capture_image("cong_thuc_mau")  
    if cong_thuc_mau_img is not None:  
        st.image(cong_thuc_mau_img, caption="Ảnh Công thức máu", use_column_width=True)  

# Thêm các trường nhập liệu khác nếu cần  
st.text_input("Ghi chú bổ sung")  

# Nút gửi  
if st.button("Gửi"):  
    st.success("Đã gửi thành công!")