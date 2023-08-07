import django_filters

from admin_site import models 

def get_to_ltk (Loaitietkiem):
        ltk=list(Loaitietkiem.objects.all().values_list('ltk',flat=True))
        ltk_list_of_tupple = []
        for i in ltk:
            ltk_list_of_tupple.append((i,i))
        
        return ltk_list_of_tupple

class PhieutietkiemFilter(django_filters.FilterSet):

    maptk = django_filters.CharFilter(field_name='maptk',label='Mã Phiếu Tiết Kiệm')
    makh = django_filters.CharFilter(field_name='makh__makh',label='Mã Khách Hàng')
    tenkh = django_filters.CharFilter(field_name='makh__tenkh',label='Tên Khách Hàng',lookup_expr='icontains')
    ltk = django_filters.ChoiceFilter(field_name='maltk__ltk',label='Loại Tiết Kiệm',choices = get_to_ltk(models.Loaitietkiem),lookup_expr='icontains')

    class Meta:
        model = models.Phieutietkiem
        fields = ['maptk','makh','tenkh','ltk']