from django.contrib import admin
from .models import Moviedata

# Register your models here.

admin.sites.AdminSite.site_header = "Movies"
admin.sites.AdminSite.site_title = "MovieAdminPanel"
admin.sites.AdminSite.index_title = "MoviesIndexList"


class MovieAdmin(admin.ModelAdmin):

    def change_typ_to_default(self, request, queryset):
        queryset.update(typ='default')

    change_typ_to_default.short_description = "typ-change"
    list_display = ('name', 'rating', 'duration', 'typ')
    list_editable = ('duration', 'typ')
    fields = ('name',)
    actions = ('change_typ_to_default',)


admin.site.register(Moviedata, MovieAdmin)
