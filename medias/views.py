import requests
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from .models import Photo

# for test modules
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


class PhotoDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise NotFound

    def delete(self, request, pk):
        photo = self.get_object(pk)
        if (photo.room and photo.room.owner != request.user) or (
            photo.experience and photo.experience.host != request.user
        ):
            raise PermissionDenied
        photo.delete()
        return Response(status=HTTP_200_OK)


class GetUploadURL(APIView):
    def post(self, request):
        url = f"https://api.cloudflare.com/client/v4/accounts/{settings.CF_ID}/images/v2/direct_upload"
        on_time_url = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {settings.CF_TOKEN}",
            },
        )
        on_time_url = on_time_url.json()
        result = on_time_url.get("result")
        if result:
            return Response({"uploadURL": result.get("uploadURL")})
        else:
            return Response(
                {
                    "id": "0000",
                    "uploadURL": "http://127.0.0.1:8000/api/v1/medias/photos/upload-photo",
                }
            )


# testing views
class UploadPhoto(APIView):
    def post(self, request):
        image_data = request.FILES["file"]
        path = default_storage.save(image_data, ContentFile(image_data.read()))
        return Response({"result": {"id": path}})
