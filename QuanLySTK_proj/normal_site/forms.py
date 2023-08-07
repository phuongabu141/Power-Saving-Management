from django import forms

class PhieuTietKiemForm (forms.Form):
    tenkh = forms.CharField(label='Tên Khách Hàng',max_length=50,required=True)
    CMND = forms.CharField(label='CMND',max_length=12,required=True)
    diachi = forms.CharField(label='Địa Chỉ',max_length=50,required=True)
    sotiengoi =forms.DecimalField(label='Số Tiền Gởi',max_digits=13,decimal_places=2,required=True)
    loaitietkiem =forms.ChoiceField(label='Loại Tiết Kiệm',choices=[('Option 1','Không Kỳ Hạn'),('Option 2','Kỳ Hạn 3 Tháng'),('Option 3','Kỳ Hạn 6 Tháng')],required=True) # chưa đúng lắm

class TimKiemPhieuTietKiemForm (forms.Form):
    tenkh = forms.CharField(label='Tên Khách Hàng',max_length=50,required=True)
    maptk = forms.CharField(label='Mã Phiếu Tiết Kiệm', max_length=10,required=True)
