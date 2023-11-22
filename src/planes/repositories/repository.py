from django.db import transaction

from planes.models import Plane, Plane_Value, Plane_Attribute


class PLaneRepository:

    
    def create_plane(self, code: str|None) -> dict[str,str]|None:
        with transaction.atomic():
            if code:
                plane = Plane.objects.create(code=code)
                return {'id': plane.id, 'code': plane.code}
            return
    
    def create_atribute(self, attribute: str|None) -> dict[str,str]|None:
        with transaction.atomic():
            if attribute:
                plane_attribute = Plane_Attribute.objects.create(attribute=attribute)
                return {'id': plane_attribute.id, 'attribute': plane_attribute.attribute}
            return
    
    def set_value(self, plane_id: int|None, attribute_id: int|None, value: str|None) -> dict[str,str]|None:
        with transaction.atomic():
            if plane_id and attribute_id and value:
                plane_value = Plane_Value.objects.create(plane_id=plane_id, attribute_id=attribute_id, value=value)
                return {'id': plane_value.id, 'plane_id': plane_value.plane_id, 'value': plane_value.value, 'attribute_id': plane_value.attribute_id}
            return
