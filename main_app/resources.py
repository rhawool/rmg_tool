from main_app.models import Associate
from import_export import resources


class AssociateResource(resources.ModelResource):
    class Meta:
        model = Associate
