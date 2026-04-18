import io

import streamlit as st

from merge_excel import merge_uploaded_excel

st.set_page_config(page_title="Tổng hợp Excel", page_icon="📊", layout="centered")

st.title("Tổng hợp nhiều file Excel")
st.caption(
    "Chọn nhiều file `.xlsx` / `.xls`. Cột **Source_File** ghi tên file nguồn của từng dòng."
)

uploaded = st.file_uploader(
    "Chọn file Excel",
    type=["xlsx", "xls"],
    accept_multiple_files=True,
)

if not uploaded:
    st.info("Vui lòng chọn ít nhất một file Excel.")
else:
    st.success(f"Đã chọn {len(uploaded)} file.")

    if st.button("Tổng hợp", type="primary"):
        with st.spinner("Đang đọc và gộp dữ liệu..."):
            try:
                merged = merge_uploaded_excel(uploaded)
            except Exception as e:
                st.error(f"Lỗi khi xử lý file: {e}")
            else:
                st.subheader("Xem trước kết quả")
                st.dataframe(merged.head(100), use_container_width=True)
                if len(merged) > 100:
                    st.caption(f"Hiển thị 100 / {len(merged)} dòng.")

                buf = io.BytesIO()
                merged.to_excel(buf, index=False, engine="openpyxl")
                buf.seek(0)

                st.download_button(
                    label="Tải xuống file tổng hợp (.xlsx)",
                    data=buf,
                    file_name="tong_hop_du_lieu.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )
