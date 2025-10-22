from rest_framework import generics


class BaseGenericView(generics.GenericAPIView):
    service_class = None

    def get_validated_data(self):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data

    def get_service(self, **kwargs):
        return self.service_class(**kwargs)
