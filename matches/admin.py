from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


from . import models


# Register your models here.
class DoublesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
class MixedDoublesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
class DoublesWithNoPartnerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
class SinglesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass



admin.site.register(models.Doubles, DoublesAdmin)
admin.site.register(models.MixedDoubles, MixedDoublesAdmin)
admin.site.register(models.DoublesWithNoPartner, DoublesWithNoPartnerAdmin)
admin.site.register(models.Singles, SinglesAdmin)




