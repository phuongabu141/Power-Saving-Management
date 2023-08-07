# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User, Group

class UsersExtendClass(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    manv = models.CharField(max_length=12)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Baocaongay(models.Model):
    ngay = models.DateField(primary_key=True)
    maltk = models.ForeignKey('Loaitietkiem', models.DO_NOTHING, db_column='maltk')
    tongthu = models.DecimalField(max_digits=13, decimal_places=2)
    tongchi = models.DecimalField(max_digits=13, decimal_places=2)
    chechlechthuchi = models.DecimalField(max_digits=13, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'baocaongay'
        unique_together = (('ngay', 'maltk'),)


class Baocaothang(models.Model):
    ngaythang = models.DateField(primary_key=True)
    maltk = models.ForeignKey('Loaitietkiem', models.DO_NOTHING, db_column='maltk')
    phieugoi = models.IntegerField()
    phieudong = models.IntegerField()
    chenhlechdonggoi = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'baocaothang'
        unique_together = (('ngaythang', 'maltk'),)


class Chucnang(models.Model):
    macn = models.CharField(primary_key=True, max_length=10)
    tencn = models.CharField(max_length=20)
    tenmanhinhduocloat = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'chucnang'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Khachhang(models.Model):
    makh = models.CharField(primary_key=True, max_length=10)
    tenkh = models.CharField(max_length=50)
    diachi = models.CharField(max_length=50)
    cccd = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'khachhang'


class Loaitietkiem(models.Model):
    maltk = models.CharField(primary_key=True, max_length=10)
    ltk = models.CharField(max_length=20)
    kyhan = models.IntegerField()
    sotiengoitoithieu = models.DecimalField(max_digits=13, decimal_places=2)
    thoigiangoitoithieu = models.IntegerField()
    laisuat = models.FloatField()

    class Meta:
        managed = False
        db_table = 'loaitietkiem'


class Nguoidung(models.Model):
    tendn = models.CharField(primary_key=True, max_length=50)
    matkhau = models.CharField(max_length=50)
    manhom = models.ForeignKey('Nhomnguoidung', models.DO_NOTHING, db_column='manhom')

    class Meta:
        managed = False
        db_table = 'nguoidung'


class Nhomnguoidung(models.Model):
    tennhom = models.CharField(max_length=50)
    manhom = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'nhomnguoidung'


class Phanquyen(models.Model):
    macn = models.OneToOneField(Chucnang, models.DO_NOTHING, db_column='macn', primary_key=True)
    manhom = models.ForeignKey(Nhomnguoidung, models.DO_NOTHING, db_column='manhom')

    class Meta:
        managed = False
        db_table = 'phanquyen'
        unique_together = (('macn', 'manhom'),)


class Phieuruttien(models.Model):
    maprt = models.CharField(primary_key=True, max_length=10)
    makh = models.ForeignKey(Khachhang, models.DO_NOTHING, db_column='makh')
    maptk = models.ForeignKey('Phieutietkiem', models.DO_NOTHING, db_column='maptk')
    ngayrut = models.DateField(blank=True, null=True)
    sotienrut = models.DecimalField(max_digits=13, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'phieuruttien'


class Phieutietkiem(models.Model):
    maptk = models.CharField(primary_key=True, max_length=10)
    makh = models.ForeignKey(Khachhang, models.DO_NOTHING, db_column='makh')
    maltk = models.ForeignKey(Loaitietkiem, models.DO_NOTHING, db_column='maltk')
    sotiengoi = models.DecimalField(max_digits=13, decimal_places=2)
    ngaydongphieu = models.DateField(blank=True, null=True)
    ngaymophieu = models.DateField()
    sodu = models.DecimalField(max_digits=13, decimal_places=2)
    tinhtrang = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phieutietkiem'


class Thamso(models.Model):
    tenthamso = models.CharField(primary_key=True, max_length=20)
    giatri = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'thamso'
