import pickle
import streamlit as st

# ฟังก์ชันในการโหลดไฟล์ classifier.pkl
def load_classifier():
    file_path = '/Users/ryu21/classifier.pkl'
    with open(file_path, 'rb') as file:
        classifier = pickle.load(file)
    return classifier

# defining the function which will make the prediction using the data which the user inputs
def prediction(Gender, Age, MaritalStatus, Type, BusinessOwner, BusinessExpYear, HaveMobileNo, AppliedAmount, TotalCreditAmount, TotalIncome, TotalDebt, Installment, CollateralFlag, TenorLoan1, Score, FinalRiskLevel):  
    # โหลดโมเดล
    classifier = load_classifier()
    
    # ทำการแปลงข้อมูลเข้าสู่รูปแบบที่ต้องการสำหรับแบบจำลอง
    if Gender == "ชาย":
        Gender = 0  
    elif Gender == "หญิง":
        Gender = 1  
    elif Gender == "ไม่ระบุ":
        Gender = 2  
    else:
        st.error(f"Unhandled Gender value: {Gender}")
        return None

    if MaritalStatus == 'โสด' or MaritalStatus == 'S' or MaritalStatus == 'N':
        MaritalStatus = 0
    elif MaritalStatus == 'สมรส จดทะเบียน' or MaritalStatus == 'สมรส ไม่จดทะเบียน' or MaritalStatus == 'M':
        MaritalStatus = 1
    elif MaritalStatus == 'หย่า' or MaritalStatus == 'D' or MaritalStatus == 'W' or MaritalStatus == 'หม้าย':
        MaritalStatus = 2
    elif MaritalStatus == 'ไม่ระบุ' or MaritalStatus == '-':
        MaritalStatus = 3
    else:
        st.error(f"Unhandled MaritalStatus value: {MaritalStatus}")
        return None

    if Type == "บุคคลธรรมดา":
        Type = 0
    else:
        Type = 1

    if BusinessOwner == "ร้านค้า":
        BusinessOwner = 0  
    elif BusinessOwner == "โรงงาน":
        BusinessOwner = 1  
    elif BusinessOwner == "คณะบุคคล":
        BusinessOwner = 2  
    elif BusinessOwner == "หสม.":
        BusinessOwner = 3  
    elif BusinessOwner == "บจก.":
        BusinessOwner = 4
    elif BusinessOwner == "หจก.":
        BusinessOwner = 5  
    elif BusinessOwner == "หสน.":
        BusinessOwner = 6
    elif BusinessOwner == "บมจ.":
        BusinessOwner = 7  
    elif BusinessOwner == "ไม่ได้จดทะเบียน":
        BusinessOwner = 8      
    else:
        st.error(f"Unhandled BusinessOwner value: {BusinessOwner}")
        return None

    if HaveMobileNo == "มี":
        HaveMobileNo = 1
    else:
        HaveMobileNo = 0

    if Score == "A":
        Score = 1  
    elif Score == "B":
        Score = 2  
    elif Score == "C":
        Score = 3  
    elif Score == "D":
        Score = 4  
    elif Score == "E":
        Score = 5
    else:
        st.error(f"Unhandled Score value: {Score}")
        return None

    if FinalRiskLevel == "0":
        FinalRiskLevel = 0  
    elif FinalRiskLevel == "1":
        FinalRiskLevel = 1  
    elif FinalRiskLevel == "2":
        FinalRiskLevel = 2  
    elif FinalRiskLevel == "3":
        FinalRiskLevel = 3
    else:
        st.error(f"Unhandled FinalRiskLevel value: {FinalRiskLevel}")
        return None

    # Making predictions
    prediction = classifier.predict(
        [[Gender, Age, MaritalStatus, Type, BusinessOwner, BusinessExpYear, HaveMobileNo, AppliedAmount, TotalCreditAmount, TotalIncome, TotalDebt, Installment, CollateralFlag, TenorLoan1, Score, FinalRiskLevel]])

    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'

    return pred

# the main function in webpage
def main():      
    # ส่วนต่าง ๆ ของหน้าเว็บ
    html_temp = """
    <div style ="background-color:blue;padding:13px">
    <h1 style ="color:orange;text-align:center;">Loan Origination Realtime Approval System</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    # กล่องใส่ข้อมูลที่ต้องการให้ผู้ใช้กรอก
    Gender = st.selectbox('Gender',["ชาย","หญิง","ไม่ระบุ"])
    Age = st.number_input('Age')
    MaritalStatus = st.selectbox('MaritalStatus',["โสด","สมรส จดทะเบียน","สมรส ไม่จดทะเบียน","หย่า","ไม่ระบุ"])
    Type = st.selectbox('Type',["บุคคลธรรมดา","นิติบุคคล"])
    BusinessOwner = st.selectbox('BusinessOwner',["ร้านค้า","โรงงาน","คณะบุคคล","หสม.","บจก.","หจก.","หสน.","บมจ.","ไม่ได้จดทะเบียน"])
    BusinessExpYear = st.number_input('BusinessExpYear')
    HaveMobileNo = st.selectbox('HaveMobileNo',["1","0"])
    AppliedAmount = st.number_input('AppliedAmount')
    TotalCreditAmount = st.number_input('TotalCreditAmount')
    TotalIncome = st.number_input('TotalIncome')
    TotalDebt = st.number_input('TotalDebt')
    Installment = st.number_input('Installment')
    CollateralFlag = st.selectbox('CollateralFlag',["1","0"])
    TenorLoan1 = st.number_input('TenorLoan1')
    Score = st.selectbox('Score',["A","B","C","D","E"])
    FinalRiskLevel = st.selectbox('FinalRiskLevel',["0","1","2","3"])

    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(Gender, Age, MaritalStatus, Type, BusinessOwner, BusinessExpYear, HaveMobileNo, AppliedAmount, TotalCreditAmount, TotalIncome, TotalDebt, Installment, CollateralFlag, TenorLoan1, Score, FinalRiskLevel)
       
        if result == 'Rejected':
            st.error('Your loan is {}'.format(result))
        else:
            st.success('Your loan is {}'.format(result))

if __name__=='__main__':
    main()
