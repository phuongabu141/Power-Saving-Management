-- DATABASES = {
--     'default': {
--         'ENGINE': 'django.db.backends.mysql',
--         'NAME': 'quan_ly_phieu_tiet_kiem',
--         'USER': 'banking_dev',
--         'PASSWORD': 'asdfghjkl01',
--         'HOST': '127.0.0.1',
--         'PORT': '3306',
--         'OPTIONS': {  
--             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
--         }  
--     }
-- }

use quan_ly_phieu_tiet_kiem;

# Create tables
create table KhachHang 
( makh varchar(10) not null,
tenkh varchar(50) not null,
diachi varchar (50) not null,
cccd varchar (12) not null,
primary key (makh)) ;

create table Phieutietkiem 
( maptk varchar(10) not null,
makh varchar(10) not null,
maltk varchar (10) not null,
sotiengoi decimal(13,2) not null,
ngaymophieu date not null,
ngaydongphieu date,
sodu decimal(13,2) not null,
tinhtrang bool not null,
primary key (maptk)) ;

create table loaitietkiem 
( maltk varchar(10) not null,
ltk varchar(20) not null,
kyhan int not null,
sotiengoitoithieu decimal(13,2) not null,
thoigiangoitoithieu int not  null,
laisuat float not null,
primary key (maltk)) ;

create table Phieuruttien 
( maprt varchar(10) not null,
makh varchar(10) not null,
maptk varchar (10) not null,
ngayrut date,
sotienrut decimal(13,2) not null,
primary key (maprt)) ;

create table  Baocaothang
( ngaythang date not null,
maltk varchar(10) not null,
phieugoi int not null,
phieudong int not null,
chenhlechdonggoi int not null,
primary key (ngaythang,maltk)) ;

create table  Baocaongay
( ngay date not null,
maltk varchar(10) not null,
tongthu decimal(13,2) not null,
tongchi decimal(13,2) not null,
chechlechthuchi decimal(13,2) not null,
primary key (ngay,maltk)) ;


-- Create foreign key
ALTER TABLE Phieutietkiem
ADD CONSTRAINT FK_PTK_1
FOREIGN KEY (makh) REFERENCES Khachhang(makh);

ALTER TABLE Phieutietkiem
ADD CONSTRAINT FK_PTK_2
FOREIGN KEY (maltk) REFERENCES Loaitietkiem(maltk);

ALTER TABLE Phieuruttien
ADD CONSTRAINT FK_PRT_1
FOREIGN KEY (makh) REFERENCES Khachhang(makh);

ALTER TABLE Phieuruttien
ADD CONSTRAINT FK_PRT_2
FOREIGN KEY (maptk) REFERENCES Phieutietkiem(maptk);

ALTER TABLE Baocaothang
ADD CONSTRAINT FK_BCT
FOREIGN KEY (maltk) REFERENCES Loaitietkiem(maltk);

ALTER TABLE Baocaongay
ADD CONSTRAINT FK_BCN
FOREIGN KEY (maltk) REFERENCES Loaitietkiem(maltk);

-- Create privilege tables
create table Nguoidung 
( tendn varchar(50) not null,
matkhau varchar(50) not null,
manhom varchar(10) not null,
primary key (tendn));

create table Phanquyen
( macn varchar(10) not null,
manhom varchar(10) not null,
primary key (macn,manhom));

create table Nhomnguoidung
( tennhom varchar(50) not null,
manhom varchar(10) not null,
primary key (manhom));

create table Chucnang
( macn varchar(10) not null,
tencn varchar(20) not null,
tenmanhinhduocloat varchar(20) not null,
primary key (macn));

-- Create thamso table
create table thamso
( tenthamso varchar(20) not null,
giatri varchar(10) not null,
primary key (tenthamso));


-- Create foreign key of privilege tables
ALTER TABLE Phanquyen
ADD CONSTRAINT FK_PQ_1
FOREIGN KEY (macn) REFERENCES Chucnang(macn);

ALTER TABLE Phanquyen
ADD CONSTRAINT FK_PQ_2
FOREIGN KEY (manhom) REFERENCES Nhomnguoidung(manhom);

-- Insert dữ liệu
-- Bảng khách hàng
INSERT INTO KhachHang (makh, tenkh, diachi,cccd) VALUES ('KH1','Nguyen Thi Mai Phuong','Nghe An', '012345678');
INSERT INTO KhachHang (makh, tenkh, diachi,cccd) VALUES ('KH2','Tran Van Huynh','Binh Dinh', '013678562');
INSERT INTO KhachHang (makh, tenkh, diachi,cccd) VALUES ('KH3','Nguyen Minh Hieu','Da Nang', '123456789');
INSERT INTO KhachHang (makh, tenkh, diachi,cccd) VALUES ('KH4','Truong Ngoc Nguyen','Ha Noi', '654789456');
INSERT INTO KhachHang (makh, tenkh, diachi,cccd) VALUES ('KH5','Vo Chi cong','Quang Tri', '657904356');
INSERT INTO KhachHang (makh, tenkh, diachi,cccd) VALUES ('KH6','Le Huong Ly','Dong Nai', '897654234');
INSERT INTO KhachHang (makh, tenkh, diachi,cccd) VALUES ('KH7','Truong Hong Ngoc','Binh Phuoc', '145678903');
INSERT INTO KhachHang (makh, tenkh, diachi,cccd) VALUES ('KH8','Tran Minh Hong','Phu Yen', '038714337');
INSERT INTO KhachHang (makh, tenkh, diachi,cccd) VALUES ('KH9','Pham Van Anh','Ha Tinh', '033520978');
INSERT INTO KhachHang (makh, tenkh, diachi,cccd) VALUES ('KH10','Nguyen Thi Ngoc Bich','Ninh Binh', '123657908');
INSERT INTO KhachHang (makh, tenkh, diachi,cccd) VALUES ('KH11','Pham Cong Hai','Nghe An', '098923434');
INSERT INTO KhachHang (makh, tenkh, diachi,cccd) VALUES ('KH12','Luong The Vinh','Tp.HCM', '687456908');
INSERT INTO KhachHang (makh, tenkh, diachi,cccd) VALUES ('KH13','Nguyen Thi Huyen','Long an', '012345679');
INSERT INTO KhachHang (makh, tenkh, diachi,cccd) VALUES ('KH14','Tran Hue Linh','Ca Mau', '012345987');
INSERT INTO KhachHang (makh, tenkh, diachi,cccd) VALUES ('KH15','Pham Van Hung','Tp.HCM', '134798567');

select * from khachhang;

-- Loại tiết kiệm
INSERT INTO loaitietkiem(maltk,ltk,kyhan,sotiengoitoithieu,thoigiangoitoithieu,laisuat) VALUES ('LTK1','Khong ky han',0,'100000',15,'0.5'); 
INSERT INTO loaitietkiem(maltk,ltk,kyhan,sotiengoitoithieu,thoigiangoitoithieu,laisuat) VALUES ('LTK2','3 thang ',3,'100000',90,'5.0');
INSERT INTO loaitietkiem(maltk,ltk,kyhan,sotiengoitoithieu,thoigiangoitoithieu,laisuat) VALUES ('LTK3','6 thang ',6,'100000',180,'5.5');

-- Phieutietkiem
INSERT INTO Phieutietkiem (maptk,makh,maltk,sotiengoi,ngaymophieu,ngaydongphieu,sodu,tinhtrang) VALUES ('PTK1','KH1','LTK3','100000000',STR_TO_DATE('01-04-2022', '%d-%m-%Y'),Null,'100000000','1');
INSERT INTO Phieutietkiem (maptk,makh,maltk,sotiengoi,ngaymophieu,ngaydongphieu,sodu,tinhtrang) VALUES ('PTK2','KH2','LTK2','250000000',STR_TO_DATE('10-05-2022', '%d-%m-%Y'),Null,'250000000','1');
INSERT INTO Phieutietkiem (maptk,makh,maltk,sotiengoi,ngaymophieu,ngaydongphieu,sodu,tinhtrang) VALUES ('PTK3','KH3','LTK1','200000000',STR_TO_DATE('09-02-2022', '%d-%m-%Y'),STR_TO_DATE('07-05-2022', '%d-%m-%Y'),'0','0');
INSERT INTO Phieutietkiem (maptk,makh,maltk,sotiengoi,ngaymophieu,ngaydongphieu,sodu,tinhtrang) VALUES ('PTK4','KH4','LTK2','50000000',STR_TO_DATE('14-01-2022', '%d-%m-%Y'),STR_TO_DATE('14-05-2022', '%d-%m-%Y'),'0','0');
INSERT INTO Phieutietkiem (maptk,makh,maltk,sotiengoi,ngaymophieu,ngaydongphieu,sodu,tinhtrang) VALUES ('PTK5','KH5','LTK3','150000000',STR_TO_DATE('17-04-2022', '%d-%m-%Y'),Null,'150000000','1');
INSERT INTO Phieutietkiem (maptk,makh,maltk,sotiengoi,ngaymophieu,ngaydongphieu,sodu,tinhtrang) VALUES ('PTK6','KH6','LTK1','500000000',STR_TO_DATE('06-04-2021', '%d-%m-%Y'),STR_TO_DATE('06-10-2021', '%d-%m-%Y'),'0','0');
INSERT INTO Phieutietkiem (maptk,makh,maltk,sotiengoi,ngaymophieu,ngaydongphieu,sodu,tinhtrang) VALUES ('PTK7','KH7','LTK2','350000000',STR_TO_DATE('17-07-2021', '%d-%m-%Y'),STR_TO_DATE('17-11-2021', '%d-%m-%Y'),'0','0');
INSERT INTO Phieutietkiem (maptk,makh,maltk,sotiengoi,ngaymophieu,ngaydongphieu,sodu,tinhtrang) VALUES ('PTK8','KH8','LTK1','600000000',STR_TO_DATE('08-04-2022', '%d-%m-%Y'),Null,'600000000','1');
INSERT INTO Phieutietkiem (maptk,makh,maltk,sotiengoi,ngaymophieu,ngaydongphieu,sodu,tinhtrang) VALUES ('PTK9','KH9','LTK3','100000000',STR_TO_DATE('06-04-2022', '%d-%m-%Y'),Null,'100000000','1');
INSERT INTO Phieutietkiem (maptk,makh,maltk,sotiengoi,ngaymophieu,ngaydongphieu,sodu,tinhtrang) VALUES ('PTK10','KH10','LTK2','780000000',STR_TO_DATE('24-05-2022', '%d-%m-%Y'),Null,'780000000','1');
INSERT INTO Phieutietkiem (maptk,makh,maltk,sotiengoi,ngaymophieu,ngaydongphieu,sodu,tinhtrang) VALUES ('PTK11','KH11','LTK3','100000000',STR_TO_DATE('01-04-2022', '%d-%m-%Y'),Null,'100000000','1');
INSERT INTO Phieutietkiem (maptk,makh,maltk,sotiengoi,ngaymophieu,ngaydongphieu,sodu,tinhtrang) VALUES ('PTK12','KH12','LTK1','800000000',STR_TO_DATE('01-03-2022', '%d-%m-%Y'),Null,'800000000','1');
INSERT INTO Phieutietkiem (maptk,makh,maltk,sotiengoi,ngaymophieu,ngaydongphieu,sodu,tinhtrang) VALUES ('PTK13','KH13','LTK2','130000000',STR_TO_DATE('05-01-2022', '%d-%m-%Y'),STR_TO_DATE('05-05-2022', '%d-%m-%Y'),'0','0');
INSERT INTO Phieutietkiem (maptk,makh,maltk,sotiengoi,ngaymophieu,ngaydongphieu,sodu,tinhtrang) VALUES ('PTK14','KH1','LTK3','440000000',STR_TO_DATE('11-01-2022', '%d-%m-%Y'),Null,'440000000','1');
INSERT INTO Phieutietkiem (maptk,makh,maltk,sotiengoi,ngaymophieu,ngaydongphieu,sodu,tinhtrang) VALUES ('PTK15','KH1','LTK2','550000000',STR_TO_DATE('23-04-2022', '%d-%m-%Y'),Null,'550000000','1');
INSERT INTO Phieutietkiem (maptk,makh,maltk,sotiengoi,ngaymophieu,ngaydongphieu,sodu,tinhtrang) VALUES ('PTK16','KH1','LTK2','160000000',STR_TO_DATE('21-04-2022', '%d-%m-%Y'),Null,'160000000','1');
INSERT INTO Phieutietkiem (maptk,makh,maltk,sotiengoi,ngaymophieu,ngaydongphieu,sodu,tinhtrang) VALUES ('PTK17','KH2','LTK2','600000000',STR_TO_DATE('09-01-2022', '%d-%m-%Y'),STR_TO_DATE('09-05-2022', '%d-%m-%Y'),'0','0');


-- Phiếu rút tiền
INSERT INTO Phieuruttien (maprt,makh,maptk,ngayrut,sotienrut) VALUES ('PRT1','KH3','PTK3',STR_TO_DATE('07-05-2022', '%d-%m-%Y'),'200238356');
INSERT INTO Phieuruttien (maprt,makh,maptk,ngayrut,sotienrut) VALUES ('PRT2','KH4','PTK4',STR_TO_DATE('14-05-2022', '%d-%m-%Y'),'50637239.6322');
INSERT INTO Phieuruttien (maprt,makh,maptk,ngayrut,sotienrut) VALUES ('PRT3','KH6','PTK6',STR_TO_DATE('06-10-2021', '%d-%m-%Y'),'501253424.658');
INSERT INTO Phieuruttien (maprt,makh,maptk,ngayrut,sotienrut) VALUES ('PRT4','KH7','PTK7',STR_TO_DATE('17-11-2021', '%d-%m-%Y'),'354475238.319');
INSERT INTO Phieuruttien (maprt,makh,maptk,ngayrut,sotienrut) VALUES ('PRT5','KH13','PTK13',STR_TO_DATE('05-05-2021', '%d-%m-%Y'),'131638795.271');
INSERT INTO Phieuruttien (maprt,makh,maptk,ngayrut,sotienrut) VALUES ('PRT6','KH2','PTK17',STR_TO_DATE('09-05-2021', '%d-%m-%Y'),'607646875.586');
select * from Phieuruttien;

-- bangthamso
Insert into thamso (tenthamso, giatri) values ('SLNguoiDung','0');
Insert into thamso (tenthamso, giatri) values ('SLKhachHang','15');
Insert into thamso (tenthamso, giatri) values ('SLPhieuTietKiem','17');
Insert into thamso (tenthamso, giatri) values ('SLPhieuRutTien','6');
Insert into thamso (tenthamso, giatri) values ('SLLoaiTietKiem','3');
