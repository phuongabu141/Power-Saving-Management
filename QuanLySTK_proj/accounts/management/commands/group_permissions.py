from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
# import tất cả các model trong project
from django.apps import apps

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        pass

# Clear all instances of the model (không nên làm như vậy)
Permission.objects.all().delete()
Group.objects.all().delete()



# Create all permissions of all tables in the project
admin_site_models = apps.get_app_config('admin_site').get_models() 

for model in admin_site_models:
    for type in ['view','change','add','delete']:
        content_type = ContentType.objects.get_for_model(model)
        permission = Permission.objects.create(
            codename='{}_{}'.format(type, model._meta.model_name),
            name='Can {} {}'.format(type, model._meta.model_name),
            content_type=content_type
        )

# Grant permission to group
# NhanVien
new_group, created = Group.objects.get_or_create(name='NhanVien')
permissions_nv = ['view','add']
models_nv_view = ['phieutietkiem','phieuruttien','loaitietkiem']
models_nv_add = ['phieutietkiem','phieuruttien','khachhang']

for permission in permissions_nv:
    if permission == 'view':
        for model in models_nv_view:
            content_type = ContentType.objects.get(app_label='admin_site', model=model)
            permission = Permission.objects.get(codename='view_{}'.format(model), content_type=content_type)
            new_group.permissions.add(permission)
            print('{} {}'.format(permission, new_group))

    if permission == 'add':
        for model in models_nv_add:    
            content_type = ContentType.objects.get(app_label='admin_site', model=model)
            permission = Permission.objects.get(codename='add_{}'.format(model), content_type=content_type)
            new_group.permissions.add(permission)
            print('{} {}'.format(permission, new_group))

# NhanVienPhanTichDuLieu
new_group, created = Group.objects.get_or_create(name='NhanVienPhanTichDuLieu')
permissions_nvptdl = ['view','add']
models_nvptdl_view = ['phieutietkiem','phieuruttien','loaitietkiem','baocaongay','baocaothang']
models_nvptdl_add = ['baocaongay','baocaothang']

for permission in permissions_nvptdl:
    if permission == 'view':
        for model in models_nvptdl_view:
            content_type = ContentType.objects.get(app_label='admin_site', model=model)
            permission = Permission.objects.get(codename='view_{}'.format(model), content_type=content_type)
            new_group.permissions.add(permission)
            print('{} {}'.format(permission, new_group))

    if permission == 'add':
        for model in models_nvptdl_add:        
            content_type = ContentType.objects.get(app_label='admin_site', model=model)
            permission = Permission.objects.get(codename='add_{}'.format(model), content_type=content_type)
            new_group.permissions.add(permission)
            print('{} {}'.format(permission, new_group))

# GiamDoc
new_group, created = Group.objects.get_or_create(name='GiamDoc')
permissions_gd = 'view'
models_gd_view = ['phieutietkiem','phieuruttien','loaitietkiem','baocaongay','baocaothang','khachhang']

for model in models_gd_view:
    content_type = ContentType.objects.get(app_label='admin_site', model=model)
    permission = Permission.objects.get(codename='view_{}'.format(model), content_type=content_type)
    new_group.permissions.add(permission)
    print('{} {}'.format(permission, new_group))

# # NhanVien
# new_group, created = Group.objects.get_or_create(name='NhanVien')
# permissions_nv = ['view','add']
# models_nv_view = ['phieutietkiem','phieuruttien','loaitietkiem']
# models_nv_add = ['phieutietkiem','phieuruttien','khachhang']

# for permission in permissions_nv:
#     if permission == 'view':
#         for model in models_nv_view:
#             ct=ContentType.objects.get(app_label='admin_site', model=model)
#             permission = Permission.objects.create(codename=f'view {model}',
#                                        name=f'Can view {model}',
#                                        content_type=ct)
#             new_group.permissions.add(permission)
#     elif permission == 'add':
#         for model in models_nv_add:
#             ct=ContentType.objects.get(app_label='admin_site', model=model)
#             permission = Permission.objects.create(codename=f'add {model}',
#                                        name=f'Can add {model}',
#                                        content_type=ct)
#             new_group.permissions.add(permission)

# # GiamDoc

# new_group, created = Group.objects.get_or_create(name='GiamDoc')
# permissions_gd = 'view'
# models_gd_view = ['phieutietkiem','phieuruttien','loaitietkiem','baocaongay','baocaothang','khachhang']

# for model in models_gd_view:
#     ct=ContentType.objects.get(app_label='admin_site', model=model)
#     permission = Permission.objects.create(codename=f'Can view {model}',
#                                 name=f'Can view {model}',
#                                 content_type=ct)
#     new_group.permissions.add(permission)

# # NhanVienPhanTichDuLieu
# new_group, created = Group.objects.get_or_create(name='NhanVienPhanTichDuLieu')
# permissions_nvptdl = ['view','add']
# models_nvptdl_view = ['phieutietkiem','phieuruttien','loaitietkiem','baocaongay','baocaothang']
# models_nvptdl_add = ['baocaongay','baocaothang']

# for permission in permissions_nvptdl:
#     if permission == 'view':
#         for model in models_nvptdl_view:
#             ct=ContentType.objects.get(app_label='admin_site', model=model)
#             permission = Permission.objects.create(codename=f'can_view_{model}',
#                                        name=f'Can view {model}',
#                                        content_type=ct)
#             new_group.permissions.add(permission)
#     elif permission == 'add':
#         for model in models_nvptdl_add:
#             ct=ContentType.objects.get(app_label='admin_site', model=model)
#             permission = Permission.objects.create(codename=f'can_add_{model}',
#                                        name=f'Can add {model}',
#                                        content_type=ct)
#             new_group.permissions.add(permission)

# # declare permission of group (block code)
# Nhan_Vien_Giao_Dich = ['view','add']
# Nhan_Vien_Phan_Tich_Du_Lieu =['view','add']
# Giam_Doc = ['view']

# # declare models are used by group
# Nhan_Vien_Giao_Dich_view = ['Phieutietkiem','Phieuruttien','LoaiTietKiem']
# Nhan_Vien_Giao_Dich_add = ['Phieutietkiem','Phieuruttien','KhachHang']
# Nhan_Vien_Phan_Tich_Du_Lieu_view = ['Phieutietkiem','Phieuruttien','LoaiTietKiem','Baocaongay','Baocaothang']
# Nhan_Vien_Phan_Tich_Du_Lieu_add = ['BaoCaoNgay','BaoCaoThang']
# Giam_Doc_view = ['Phieutietkiem','Phieuruttien','LoaiTietKiem','Baocaongay','Baocaothang','Khachhang']

# # define group permission
# def add_group_permission(group_names,model_natural_keys, permissions): # model_natural_keys is known list of ordered list by group name 
#     model_natural_keys_count=0
#     for group_name in range(0, len(group_names)):
#         group,created = Group.objects.get_or_create(name=group_names[group_name])
#         for permission in range(0,len(permissions[group_name])):
#             perm_to_add = []
#             for key in range (0,len(model_natural_keys[model_natural_keys_count])):
#                 permission_codename = f"{permissions[group_name][permission]}_{model_natural_keys[model_natural_keys_count][key]}"
#                 try: 
#                     perm_to_add.append(Permission.objects.get_by_natural_key(codename=permission_codename,app_label='admin_site', model=model_natural_keys[model_natural_keys_count][key]))
#                 except Permission.DoesNotExist:
#                     print(f"Permission {permission_codename} does not exist")
#                 except ContentType.DoesNotExist:
#                     print(f"ContentType {model_natural_keys[model_natural_keys_count][key]} does not exist")
#             model_natural_keys_count = model_natural_keys_count + 1
#             group.permissions.add(*perm_to_add)

        

# # call function
# group_names = ['Nhan_Vien_Giao_Dich','Nhan_Vien_Phan_Tich_Du_Lieu','Giam_Doc']
# model_natural_keys = [Nhan_Vien_Giao_Dich_view,Nhan_Vien_Giao_Dich_add,Nhan_Vien_Phan_Tich_Du_Lieu_view,Nhan_Vien_Phan_Tich_Du_Lieu_add,Giam_Doc_view]
# permissions = [Nhan_Vien_Giao_Dich,Nhan_Vien_Phan_Tich_Du_Lieu,Giam_Doc]
# add_group_permission(group_names,model_natural_keys,permissions)