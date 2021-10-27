from cid.locals import get_cid
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloApiView(APIView):
    @staticmethod
    def get(request):
        print(request.correlation_id)
        return Response({
            "success": True,
            "request.correlation_id": request.correlation_id,
            "get_cid": get_cid()
        })
